"""support objects and logging procedures for ix framework."""
import datetime as dt
import json
import logging
import os
import shutil
import time
import warnings
import xml.etree.ElementTree as ET
from functools import wraps
from hashlib import md5
from io import StringIO
from itertools import chain
from pathlib import Path
from sys import stdout
from typing import Mapping, Sequence, MutableMapping, Collection, Callable, \
    Optional
import re
from urllib.parse import urlparse

from hostess.aws.s3 import Bucket
import numpy as np
import pandas as pd
import pyarrow as pa
import requests
from dustgoggles.func import disjoint, intersection
from dustgoggles.structures import dig_for_values
from dustgoggles.tracker import TrivialTracker
from more_itertools import chunked
from multidict import MultiDict

import pdr
from pdr.parselabel.pds3 import read_pvl
from pdr.utils import check_cases
from pdr_tests.settings.base import HEADERS, MANIFEST_DIR
from pdr_tests.utilz.dev_utilz import Stopwatch
from pdr.pdr import Data

REF_ROOT = Path(Path(__file__).parent.parent, "reference")
DATA_ROOT = Path(Path(__file__).parent.parent, "data")

PDRTESTLOG = logging.getLogger()
if len(PDRTESTLOG.handlers) == 0:
    PDRTESTLOG.addHandler(logging.FileHandler("pdrtests.log"))
PDRTESTLOG.setLevel("INFO")


def stamp() -> str:
    return f"{dt.datetime.utcnow().isoformat()[:-7]}: "


def console_and_log(message, level="info", do_stamp=True, quiet=False):
    stamp_txt = stamp() if do_stamp is True else ""
    getattr(PDRTESTLOG, level)(f"{stamp_txt}{message}")
    if not quiet:
        print(f"{stamp_txt}{message}")


def find_manifest(fn):
    path = Path(fn).with_suffix(".parquet")
    if (MANIFEST_DIR / path.name).exists():
        return MANIFEST_DIR / path
    if (op := MANIFEST_DIR / path.name.replace("_coverage", "")).exists():
        return op
    if (
        op := MANIFEST_DIR / path.name.replace(".parquet", "_coverage.parquet")
    ).exists():
        return op
    raise FileNotFoundError(f"no file matching {fn} found in {MANIFEST_DIR}")


def checksum_object(obj, hash_function=md5):
    """
    make stable byte array from python object. the general case of this is
    impossible, or at least implementation-dependent, so this just
    attempts to cover the cases we actually have.
    """
    hasher = hash_function(usedforsecurity=False)
    if isinstance(obj, np.ndarray):
        hasher.update(obj)
    elif isinstance(obj, pd.DataFrame):
        # note that object ('O') dtypes do not, by design, have stable
        # byte-level representations.
        blocks = obj._to_dict_of_blocks()
        # sorting to improve consistency between pandas versions
        for dtype in sorted(blocks.keys()):
            if dtype == 'object':
                for c in blocks[dtype].columns:
                    exploded = blocks[dtype][c].explode()
                    stringified = StringIO()
                    for i, v in exploded.items():
                        # add 分 separator character to reduce chance of hash
                        # collisions from very unlikely to vanishingly so
                        stringified.write(f"{i} {v}分")
                    stringified.seek(0)
                    stringified = stringified.read().encode('utf-8')
                    hasher.update(stringified)
            else:
                # TODO, maybe: the arrays underlying dataframes are
                #  typically not stored in C-contiguous order. copying the
                #  array is somewhat memory-inefficient. another solution is
                #  to dump each line as string or bytes -- like we do for
                #  object dtypes above -- which would be slower but smaller.
                hasher.update(blocks[dtype].values.copy())
    else:
        # TODO: determine when this is and is not actually stable
        hasher.update(obj.__repr__().encode("utf-8"))
    return hasher.hexdigest()


def just_hash(data):
    hashes = {}
    for key in data.keys():
        # objects not loaded by default, whether due to lazy-loading or
        # membership in OBJECTS_IGNORED_BY_DEFAULT (like MODEL_DESC)
        if key not in dir(data):
            continue
        # pds4_tools label object
        if '_convenient_root' in dir(data[key]):
            continue
        # ignore text-type objects for now (but not FITS headers)
        if isinstance(data[key], MultiDict) and ("HEADER" not in key):
            continue
        if isinstance(data[key], str):
            continue
        hashes[key] = checksum_object(data[key])
    return hashes


def get_nodelist(xmlfile):
    return ET.parse(xmlfile).getroot().findall(".//*")


def make_pds4_row(xmlfile):
    nodelist = get_nodelist(xmlfile)
    return {
        "label_file": Path(xmlfile).name,
        "product_id": next(
            node for node in nodelist if "logical_identifier" in node.tag
        ).text,
        "files": json.dumps(
            [node.text for node in nodelist if "file_name" in node.tag]
            + [Path(xmlfile).name]
        ),
    }


def make_pds3_row(local_path):
    metadata = pdr.pdr.Metadata(read_pvl(check_cases(local_path)))
    files = [local_path.name]
    # TODO: use get_pds3_pointers here to decrease fragility
    targets = dig_for_values(
        metadata,
        "^",
        mtypes=(MultiDict, dict),
        base_pred=lambda a, b: b.startswith(a)
    )
    for target in targets:
        if isinstance(target, (int, set, dict)):
            continue
        if isinstance(target, Sequence):
            if not isinstance(target, str):
                target = target[0]
        if not isinstance(target, str):
            raise TypeError("what is this?")
        if (
            "COMPRESSED_FILE" in metadata.keys()
            and target in metadata["UNCOMPRESSED_FILE"].values()
        ):
            target = metadata["COMPRESSED_FILE"]["FILE_NAME"]
        files.append(target)
    files = list(set(files))
    row = {
        "label_file": local_path.name,
        "files": json.dumps(files),
    }
    if "PRODUCT_ID" in metadata.fieldcounts.keys():
        row["product_id"] = metadata.metaget_("PRODUCT_ID")
    else:
        row["product_id"] = local_path.stem
    return row


def get_product_row(label_path, url):
    if Path(label_path).suffix == ".xml":
        row = make_pds4_row(label_path)
    else:
        row = make_pds3_row(label_path)
    row["url_stem"] = os.path.dirname(url)
    return row


def download_product_row(
    data_path, temp_path, row, skip_files=(), session=None, full_lower=False
):
    files = json.loads(row["files"])
    session = session if session is not None else MaybeSession()
    for file in files:
        if Path(data_path, file).exists():
            console_and_log(f"... {file} present, skipping ...")
            continue
        if any((file == skip_file for skip_file in skip_files)):
            continue
        url = f"{row['url_stem']}/{file}"
        verbose_temp_download(data_path, temp_path, url, full_lower)
    return session


class MaybeSession:
    def __init__(self):
        self._is_closed = False
        self.session = requests.Session()
        self.session_count = 1

    def reset(self):
        self.session.close()
        self.session = requests.Session()
        self.session_count += 1

    def _tryit(self, method, *args, **kwargs):
        if self._is_closed:
            self.session = requests.Session()
        return getattr(self.session, method)(*args, **kwargs)

    @wraps(requests.Session.get)
    def get(self, *args, **kwargs):
        return self._tryit("get", *args, **kwargs)

    @wraps(requests.Session.put)
    def put(self, *args, **kwargs):
        return self._tryit("put", *args, **kwargs)

    @wraps(requests.Session.head)
    def head(self, *args, **kwargs):
        return self._tryit("head", *args, **kwargs)

    @wraps(requests.Session.close)
    def close(self):
        self.session.close()
        self._is_closed = True

    @wraps(requests.Session.__enter__)
    def __enter__(self):
        return self._tryit("__enter__")

    @wraps(requests.Session.__exit__)
    def __exit__(self, *args):
        return self._tryit("__exit__")

    @property
    def cookies(self):
        return self.session.cookies


BUCKETNAME_PAT = re.compile(r"^(?:(http(s)?|s3)://)?(?P<name>(\w|-)+)")
ISBUCKET_PAT = re.compile(r"(^s3://)|(\.amazonaws\.com)")


def _expand_index_table(filelist):
    recs = []
    for _, row in filelist.iterrows():
        baserec = row.to_dict()
        files = json.loads(row['files'])
        for f in files:
            recs.append(baserec | {'url': f"{row['url_stem']}/{f}"})
    return pd.DataFrame(recs)


def verbose_temp_download(filelist, data_path, temp_path, full_lower=False):
    if 'url_stem' in filelist.columns:
        filelist = _expand_index_table(filelist)
        isbucket_target = 'url'
    else:
        isbucket_target = 'domain'
    if ISBUCKET_PAT.search(filelist[isbucket_target].iloc[0]):
        bucketname = BUCKETNAME_PAT.search(
            filelist[isbucket_target].iloc[0]
        ).groupdict()['name']
        _verbose_s3_download_filelist(
            filelist, data_path, bucketname, full_lower
        )
    else:
        _verbose_web_temp_download_filelist(
            filelist, data_path, temp_path, full_lower
        )


def _verbose_s3_download_filelist(
    filelist, data_path, bucketname, full_lower=False
):
    filelist = filelist.copy()
    filelist['targ'] = filelist['url'].map(
        lambda u: urlparse(u).path
    ).str.strip('/')
    if full_lower is True:
        filelist['targ'] = filelist['targ'].map(
            lambda p: str(Path(p).parent / Path(p).name.lower())
        )
    filelist['dest'] = filelist['targ'].map(
        lambda p: Path(data_path) / Path(p).name
    )
    exists = filelist['dest'].map(lambda p: p.exists())
    if len(extant := filelist['dest'].loc[exists]) > 0:
        print("The following files already exist in the filesystem, skipping:")
        for e in extant:
            print(e.name)
    filelist = filelist.loc[~exists]
    if len(filelist) == 0:
        return
    print(f"downloading {len(filelist)} files...")
    if 'size' in filelist.columns:
        big = filelist['size'] / 1000 ** 2 > 250
        small = filelist['size'] / 1000 ** 2 <= 250
        bigix, smallix = filelist.index[big], filelist.index[small]
        chunks = chain(chunked(smallix, 50), chunked(bigix, 10))
    else:
        chunks = chunked(filelist.index, 20)
    bucket = Bucket(bucketname)
    for ixchunk in map(list, chunks):
        bad, good, ixchunk = _s3_download_chunk(
            bucket, filelist, ixchunk, extlower=False
        )
        if len(bad) > 0:
            bad, lowergood, ixchunk = _s3_download_chunk(
                bucket, filelist, ixchunk, extlower=True
            )
            good += lowergood
        for g in good:
            print(f"successfully downloaded {g}")
        for i, b in bad:
            print(f"failed to download {filelist.loc[ixchunk[i], 'targ']}: {b}")


# TODO: eww
def _extlower_series(series):
    return series.map(
        lambda p: str(Path(p).with_suffix(Path(p).suffix.lower()))
    )


def _s3_download_chunk(bucket, filelist, ixchunk, extlower=False):
    targ, dest = filelist.loc[ixchunk, 'targ'], filelist.loc[ixchunk, 'dest']
    if extlower is True:
        targ, dest = map(_extlower_series, (targ, dest))
    results = bucket.get(targ, dest)
    good = [str(r) for r in results if isinstance(r, Path)]
    bad = [(i, r) for i, r in enumerate(results) if not isinstance(r, Path)]
    return bad, good, ixchunk


def _verbose_web_temp_download_file(
    data_path,
    temp_path,
    url,
    skip_quietly=True,
    session=None,
    full_lower=False
):
    session = session if session is not None else MaybeSession()
    try:
        check_cases(Path(data_path, Path(url).name))
        if skip_quietly is False:
            console_and_log(
                f"{Path(url).name} already present, skipping download."
            )
        return session
    except FileNotFoundError:
        pass
    console_and_log(f"attempting to download {url}.")
    response, session = get_response(session, url)
    try:
        if response is None:
            console_and_log(f"Download of {url} timed out.")
            return session
        if not response.ok:
            response.close()
            if full_lower is True:
                urlsplit = url.split('/')
            else:
                urlsplit = url.split('.')
            url = url.split(urlsplit[-1])[0]+urlsplit[-1].lower()
            response = session.get(url, stream=True, headers=HEADERS)
            if not response.ok:
                console_and_log(f"Download of {url} failed.")
                response.close()
                return session
        _download_chunk(response, temp_path, url)
        shutil.move(
            Path(temp_path, Path(url).name), Path(data_path, Path(url).name)
        )
        console_and_log(f"completed download of {url}.")
    finally:
        response.close()


def _download_chunk(response, temp_path, url):
    with open(Path(temp_path, Path(url).name), "wb+") as fp:
        size, fetched = response.headers.get('content-length'), 0
        size = (
            'unknown' if size is None else round(int(size) / 1000 ** 2, 2)
        )
        for ix, chunk in enumerate(response.iter_content(chunk_size=10 ** 7)):
            fetched += len(chunk)
            print_inline(
                f"getting chunk {ix} "
                f"({round(fetched / 1000 ** 2, 2)} / {size} MB)"
            )
            fp.write(chunk)


def _verbose_web_temp_download_filelist(
    filelist, data_path, temp_path, full_lower=False
):
    session = MaybeSession()
    for ix, row in filelist.iterrows():
        try:
            session = _verbose_web_temp_download_file(
                data_path,
                temp_path,
                row["url"],
                skip_quietly=False,
                session=session,
                full_lower=full_lower
            )
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            console_and_log(f"download failed: {type(ex)}: {ex}")


def get_response(session: MaybeSession, url: str):
    for _ in range(5):
        try:
            response = session.get(
                url, stream=True, headers=HEADERS, timeout=4
            )
            return response, session
        except requests.ReadTimeout:
            console_and_log(f"slow response on {url}; reestablishing session")
            time.sleep(2)
            session.reset()
    return None, session


# noinspection HttpUrlsUsage
def assemble_urls(subset: pd.DataFrame):
    return 'http://' + subset.domain + '/' + subset.url + '/' + subset.filename


def record_mismatches(results, absent, novel):
    """
    Assigns strings of "missing from output" and "not found in reference" to
    the value of the missing and new keys in the results dictionary.
    """
    for key in absent:
        results[key] = "missing from output"
    for key in novel:
        results[key] = "not found in reference"
    return results


def compare_hashes(
    test: Mapping[str, str], reference: Mapping[str, str]
) -> Mapping[str, str]:
    """
    Compares two mappings, notionally from object name to hashed value of
    object.

    Returns a dictionary containing new keys, missing keys, and keys with
    mismatched hash values.
    """
    problems = {}
    new_keys, missing_keys = disjoint(test, reference)
    # note keys that are completely new or missing
    if len(new_keys + missing_keys):
        problems |= record_mismatches(problems, missing_keys, new_keys)
    # do comparisons between others
    for key in intersection(test, reference):
        if test[key] != reference[key]:
            problems[
                key
            ] = f"hashes !=; test: {test[key]}; reference: {reference[key]}"
    return problems


def flip_ends_with(strings: Collection[str], ending: str) -> Callable:
    """partially-evaluated form of pa.compute.ends_with"""
    return pa.compute.ends_with(strings, pattern=ending)


def read_and_hash(
    path: Path,
    product: Mapping[str, str],
    debug: bool,
    quiet: bool,
    skiphash: bool,
    tracker: Optional[TrivialTracker] = None
) -> tuple[Data, dict[str, str], dict[str, str]]:
    """
    read a product at a specified path, compute hashes from its data objects,
    log appropriately
    """
    import astropy.io.fits.verify
    watch, runtimes = Stopwatch(digits=3, silent=True), {}
    with warnings.catch_warnings():
        # We don't want to hear about UserWarnings we're intentionally raising
        # inside pdr (for things like unsupported object types, etc.)
        warnings.filterwarnings("ignore", category=UserWarning, module="pdr")
        warnings.filterwarnings(
            "ignore",
            message="non-ASCII characters",
            module="astropy.io.fits.util"
        )
        warnings.filterwarnings(
            "ignore",
            category=astropy.io.fits.verify.VerifyWarning
        )
        warnings.filterwarnings(
            "ignore",
            message="Unexpected bytes",
            module="astropy.io.fits.header"
        )
        watch.start()
        data = pdr.read(str(path), debug=debug, tracker=tracker)
        data.load("all")
        runtimes["readtime"] = watch.peek()
    console_and_log(
        f"Opened {product['product_id']} ({runtimes['readtime']} s)",
        quiet=quiet
    )
    watch.click()
    if skiphash is True:
        return data, {}, runtimes
    hashes = just_hash(data)
    runtimes['hashtime'] = watch.peek()
    console_and_log(
        f"Computed hashes for {product['product_id']} "
        f"({runtimes['hashtime']} s)", quiet=quiet
    )
    return data, hashes, runtimes


def record_comparison(
    test: Mapping[str, str],
    reference: Mapping[str, str],
    log_row: MutableMapping[str, str]
) -> MutableMapping[str, str]:
    """
    check product hashes against saved reference from hash file,
    record in log_row
    """
    result = compare_hashes(test, reference)
    if result != {}:
        log_row["status"] = "hash mismatch"
        log_row["error"] = str(result)
    return log_row


def print_inline(text: str, blanks: int = 60):
    """For updating text in place without a carriage return."""
    stdout.write(" "*blanks+"\r")
    stdout.write(str(str(text)+'\r'))
    stdout.flush()
    return
