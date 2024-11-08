"""support objects and logging procedures for ix framework."""

from blake3 import blake3
import datetime as dt
import json
import logging
import os
import tempfile
import time
import warnings
import xml.etree.ElementTree as ET
from functools import wraps
from hashlib import md5
from io import StringIO
from itertools import chain
from pathlib import Path
import re
from sys import stdout
from typing import (
    Callable, Collection, Mapping, MutableMapping, Sequence, Optional
)
from urllib.parse import urlparse

from hostess.aws.s3 import Bucket
from hostess.directory import index_breadth_first
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
from pdr.pdr import Data
from pdr.parselabel.pds3 import read_pvl
from pdr.utils import check_cases

import pdr_tests
from pdr_tests.definitions import RULES_MODULES
from pdr_tests.utilz.dev_utilz import Stopwatch


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


def find_manifest(fn: str, manifest_dir: Path):
    name = Path(fn).with_suffix(".parquet").name
    if (op := manifest_dir / name).exists():
        return op
    if (op := manifest_dir / name.replace("_coverage", "")).exists():
        return op
    if (
        op := manifest_dir / name.replace(".parquet", "_coverage.parquet")
    ).exists():
        return op
    raise FileNotFoundError(f"no file matching {fn} found in {manifest_dir}")


def checksum_object(obj, hash_function=blake3):
    """
    make stable byte array from python object. the general case of this is
    impossible, or at least implementation-dependent, so this just
    attempts to cover the cases we actually have.
    """
    hasher = hash_function(usedforsecurity=False)
    if isinstance(obj, np.ndarray):
        hasher.update(np.frombuffer(obj.data, dtype='uint8'))
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
                contiguous = np.ascontiguousarray(blocks[dtype].values)
                hasher.update(np.frombuffer(contiguous, dtype=np.uint8))
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


class HTTPSessionWrapper:
    def __init__(self, add_req_headers={}, retries=5, timeout=4, backoff=2):
        self.session = None
        self.session_count = 0
        self.add_req_headers = add_req_headers
        self.retries = retries
        self.timeout = timeout
        self.backoff = backoff

    def reset(self):
        if self.session is not None:
            self.session.close()
        self.session = requests.Session()
        self.session.headers.update(self.add_req_headers)
        self.session_count += 1

    @wraps(requests.Session.close)
    def close(self):
        self.session.close()
        self.session = None

    def get_with_retries(self, url: str):
        if self.session is None:
            self.reset()
        for _ in range(self.retries):
            try:
                return self.session.get(
                    url, stream=True, timeout=self.timeout
                )
            except requests.ReadTimeout:
                console_and_log(
                    f"slow response on {url}; reestablishing session"
                )
                time.sleep(self.backoff)
                self.reset()
        return None

    @property
    def cookies(self):
        return self.session.cookies


BUCKETNAME_PAT = re.compile(r"^(?:(http(s)?|s3)://)?(?P<name>(\w|-)+)")
ISBUCKET_PAT = re.compile(r"(^s3://)|(\.amazonaws\.com)")


def _expand_index_table(filelist, data_path):
    recs = []
    for _, row in filelist.iterrows():
        baserec = row.to_dict()
        files = json.loads(row['files'])
        for f in files:
            rec = baserec | {'url': f"{row['url_stem']}/{f}"}
            rec['dest'] = data_path / Path(rec['url']).name
            rec['exists'] = _casecheck_wrap(rec['dest'])
            recs.append(rec)
    filelist = pd.DataFrame(recs)
    if len(extant := filelist.loc[filelist['exists']]) > 0:
        print("The following files already exist in the filesystem, skipping:")
        for _, e in extant.iterrows():
            print(e['dest'])
    return filelist.loc[~filelist.exists].reset_index(drop=True).copy()


def verbose_temp_download(filelist, data_path, full_lower=False,
                          add_req_headers={}):
    if 'url_stem' in filelist.columns:
        filelist = _expand_index_table(filelist, data_path)
        isbucket_target = 'url'
    else:
        isbucket_target = 'domain'
    if len(filelist) == 0:
        return
    if ISBUCKET_PAT.search(filelist[isbucket_target].iloc[0]):
        bucketname = BUCKETNAME_PAT.search(
            filelist[isbucket_target].iloc[0]
        ).groupdict()['name']
        _verbose_s3_download_filelist(
            filelist, data_path, bucketname, full_lower,
        )
    else:
        _verbose_web_temp_download_filelist(
            filelist, data_path, full_lower, add_req_headers
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
    console_and_log(f"downloading {len(filelist)} files...")
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
                bucket, filelist, [ixchunk[i] for i, _ in bad], extlower=True
            )
            good += lowergood
        for g in good:
            console_and_log(f"successfully downloaded {g}")
        for i, b in bad:
            console_and_log(f"failed to download {filelist.loc[ixchunk[i], 'targ']}: {b}")


# TODO: eww
def _extlower_series(series):
    return series.map(
        lambda p: str(Path(p).with_suffix(Path(p).suffix.lower()))
    )


def _bucketget(bucket: Bucket, targ, dest):
    results = bucket.get(targ, dest)
    good = [str(r) for r in results if isinstance(r, (str, Path))]
    bad = [(i, r) for i, r in enumerate(results) if isinstance(r, Exception)]
    return bad, good


def _s3_download_chunk(bucket, filelist, ixchunk, extlower=False):
    targ, dest = filelist.loc[ixchunk, 'targ'], filelist.loc[ixchunk, 'dest']
    if extlower is True:
        targ, dest = map(_extlower_series, (targ, dest))
    bad, good = _bucketget(bucket, targ, dest)
    return bad, good, ixchunk


def _verbose_web_temp_download_file(
    data_path,
    url,
    session,
    skip_quietly=True,
    full_lower=False,
):
    try:
        check_cases(Path(data_path, Path(url).name))
        if skip_quietly is False:
            console_and_log(
                f"{Path(url).name} already present, skipping download."
            )
            return
    except FileNotFoundError:
        pass
    console_and_log(f"attempting to download {url}.")
    try:
        response = session.get_with_retries(url)
        if response is None:
            console_and_log(f"Download of {url} timed out.")
            return
        if not response.ok:
            console_and_log(f"Download of {url} failed: {response.status_code} {response.reason}")
            response.close()
            if full_lower is True:
                urlsplit = url.split('/')
            else:
                urlsplit = url.split('.')
            url = url.split(urlsplit[-1])[0]+urlsplit[-1].lower()
            response = session.get_with_retries(url)

        if response is None:
            console_and_log(f"Download of {url} timed out.")
            return
        if not response.ok:
            console_and_log(f"Download of {url} failed: {response.status_code} {response.reason}")
            return

        _download_chunk(response, Path(data_path), Path(url).name)
        console_and_log(f"completed download of {url}.")
    finally:
        response.close()


def _download_chunk(response, data_path, data_name):
    tempfd, temp_name = tempfile.mkstemp(
        dir=data_path,
        prefix=data_name + "-part."
    )
    try:
        with os.fdopen(tempfd, "wb") as fp:
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
    except:
        os.remove(temp_name)
        raise
    os.rename(temp_name, data_path / data_name)


def _verbose_web_temp_download_filelist(
    filelist, data_path, full_lower=False, add_req_headers={}
):
    session = HTTPSessionWrapper(add_req_headers)
    for ix, row in filelist.iterrows():
        try:
            _verbose_web_temp_download_file(
                data_path,
                row["url"],
                session,
                skip_quietly=False,
                full_lower=full_lower
            )
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            console_and_log(f"download failed: {type(ex)}: {ex}")


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


def _memformat(memval: int):
    if memval is None:
        return "n/a"
    if memval == 0:
        return "~0 MB"
    return f"{round(memval / 1000 ** 2, 2)} MB"


def read_and_hash(
    path: Path,
    product: Mapping[str, str],
    pdr_debug: bool,
    quiet: bool,
    skiphash: bool,
    tracker: Optional[TrivialTracker] = None,
    check_memory: bool = False
) -> tuple[Data, dict[str, str], dict[str, str]]:
    """
    read a product at a specified path, compute hashes from its data objects,
    log appropriately
    """
    import astropy.io.fits.verify
    from pdr_tests.utilz.mem_utilz import Memwatcher

    memwatcher = Memwatcher(fake=not check_memory)
    watch, runstats = Stopwatch(digits=3, silent=True), {}
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
        with memwatcher.watch():
            data = pdr.read(str(path), debug=pdr_debug, tracker=tracker)
            data.load("all")
        runstats["readtime"] = watch.peek()
        runstats["readmem"] = memwatcher.peaks[-1]
    console_and_log(
        f"Opened {product['product_id']} ({runstats['readtime']} s, "
        f"{_memformat(memwatcher.peaks[-1])})",
        quiet=quiet
    )
    watch.click()
    runstats["prodsize"] = sum(
        os.stat(p).st_size for p in set(data.file_mapping.values())
    )
    if skiphash is True:
        return data, {}, runstats
    # with memwatcher.watch():
    hashes = just_hash(data)
    runstats['hashtime'] = watch.peek()
    runstats['hashmem'] = memwatcher.peaks[-1]
    console_and_log(
        f"Computed hashes for {product['product_id']} "
        f"({runstats['hashtime']} s, "
        f"{_memformat(memwatcher.peaks[-1])})",
        quiet=quiet
    )
    return data, hashes, runstats


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


def _casecheck_wrap(path):
    try:
        check_cases(path)
        return True
    except FileNotFoundError:
        return False


def list_datasets() -> list[str]:
    return sorted(RULES_MODULES.keys())


def _sync_chunks(bucket, tofetch, data_path):
    for chunk in chunked(tofetch, 20):
        chunk = tuple(chunk)
        bad, good = _bucketget(bucket, chunk, [data_path / f for f in chunk])
        for g in good:
            console_and_log(f"Successfully downloaded {g}")
        for i, b in bad:
            console_and_log(f"Failed to download {chunk[i]}: {type(b)}: {b}")


def _canonicalize_test_data_path(pathname: str) -> str:
    path = Path(pathname)
    return f"{path.parent.parent.name}/{path.parent.name}/{path.name}"


def download_datasets(
    datasets: list[str],
    bucket_name: str,
    clean: bool = False,
    force: bool = False,
    replace_newer: bool = False,
    replace_offsize: bool = True,
    dry_run: bool = False
):
    data_path = Path(pdr_tests.__file__).parent / "data"
    bucket = Bucket(bucket_name)
    local = pd.DataFrame(index_breadth_first(data_path))
    local['path'] = local['path'].map(_canonicalize_test_data_path)
    local = local.loc[
        local['directory'] == False
    ].sort_values(by='path').reset_index()
    console_and_log("indexing requested dataset prefixes in bucket")
    if len(datasets) > 1:
        remote = bucket.df()
    else:
        remote = bucket.ls(datasets[0], recursive=True, formatting='df')
    remote = remote.sort_values(by='Key').reset_index()
    console_and_log(f"indexing complete, {len(remote)} objects total")
    root_prefixes = remote['Key'].str.split('/', n=1, expand=True)[0].unique()
    if not set(root_prefixes).issuperset(datasets):
        missing_datasets = sorted(set(datasets).difference(root_prefixes))
        console_and_log(
            f"WARNING: The following requested datasets do not exist as "
            f"prefixes under the bucket root: {', '.join(missing_datasets)}. "
            # TODO, maybe: check these cases
            f"Possibly unfinalized or have no defined ptypes."
        )
    # TODO, maybe: actually check against the test product indices
    targets = remote.loc[
        remote['Key'].str.split("/", expand=True)[0].isin(datasets)
    ]
    if force is False:
        missing = targets.loc[~targets['Key'].isin(local['path'])]
        present_remote = targets.loc[
            targets['Key'].isin(local['path'])
        ].copy().reset_index()
        present_local = local.loc[
            local['path'].isin(present_remote['Key'])
        ].copy().reset_index()
        console_and_log(f"{len(missing)} files missing from local")
        fetchpaths = set(missing['Key'].tolist())
        # TODO, maybe: this is a hack and maybe indicates there should be an
        #  option in hostess to not return size in MB
        present_local['stsize'] = present_local['path'].map(
            lambda p: Path(data_path, p).stat().st_size
        )
        offsize = present_local['stsize'] != present_remote['Size']
        if replace_newer is True:
            tzlocal = dt.datetime.now().astimezone().tzinfo
            newer = present_remote.loc[
                present_local['MTIME'].dt.tz_localize(tzlocal)
                < present_remote['LastModified']
            ]
            if len(newer) > 0:
                console_and_log(
                    "replace_newer active, also downloading files more "
                    "recently modified on remote"
                )
                console_and_log(f"{len(newer)} are newer on remote")
                fetchpaths.update(newer['Key'].tolist())
        if replace_offsize is True and offsize.any():
            console_and_log(
                f"replace_offsize active, also downloading files of different "
                f"sizes on local and remote ({offsize.sum()} files)"
            )
            fetchpaths.update(present_remote['Key'].loc[offsize].tolist())

        if offsize.any() and replace_offsize is False:
            off = present_remote.loc[offsize]
            no_download_offsize = off.loc[~off['Key'].isin(fetchpaths), 'Key']
            if len(no_download_offsize) > 0:
                console_and_log(
                    "WARNING: the following files have different sizes "
                    "but are not being downloaded because they are newer "
                    "on local:"
                )
                for k in no_download_offsize:
                    console_and_log(k)
        fetchsize = remote.loc[
            remote['Key'].isin(fetchpaths), 'Size'
        ].sum() / 1000 ** 2
    else:
        console_and_log("force mode on, downloading all files")
        fetchpaths = targets['Key']
        fetchsize = targets['Size'].sum() / 1000 ** 2
    if len(fetchpaths) > 0:
        console_and_log(
            f"Downloading {len(fetchpaths)} files ({fetchsize} MB total)"
        )
        if dry_run is True:
            console_and_log("***dry-run mode active, not actually downloading***")
            for f in fetchpaths:
                console_and_log(f"Would download {f} to {data_path / f}")
        else:
            _sync_chunks(bucket, fetchpaths, data_path)
    else:
        console_and_log("No remote objects to fetch.")

    if clean:
        extra = local.loc[~local['path'].isin(remote['Key']), 'path']
        if len(extra) > 0:
            console_and_log(f"Deleting {len(extra)} files from local")
            if dry_run is True:
                console_and_log(f"***dry-run mode active, not actually deleting***")
                for e in extra:
                    console_and_log(f"Would delete {data_path / e}")
            else:
                for e in extra:
                    Path(data_path / e).unlink()
                    console_and_log(f"Successfully deleted {data_path / e}")
        else:
            console_and_log("No extra files to delete.")


def clean_logs():
    def_path = Path(pdr_tests.__file__).parent / "definitions"
    targets = []
    for mod in def_path.iterdir():
        if not mod.is_dir():
            continue
        if not (mod / "logs").exists() or not (mod / "logs").is_dir():
            continue
        targets += list(
            p for p in (mod / "logs").iterdir()
            if not p.name.endswith("_latest.csv")
        )
    if len(targets) > 0:
        console_and_log(f"Deleting {len(targets)} older logfiles")
        for t in targets:
            t.unlink()
    else:
        console_and_log("No older logfiles to delete")
    console_and_log("Deleting primary log")
    (Path(pdr_tests.__file__).parent / "pdrtests.log").unlink()


def print_rules_list(dataset: Optional[str] = None):
    rules = RULES_MODULES
    if dataset is not None:
        rules = {dataset: rules[dataset]}
    for ds, mod in sorted(rules.items(), key=lambda kv: kv[0]):
        print(f"- {ds}")
        for ptype in sorted(mod.file_information.keys()):
            print(f"  - {ptype} ({mod.file_information[ptype]['manifest']})")


def _find_in_row_group(meta, ix, rgix, reader, mrecs, urls):
    nrows = meta.row_group(rgix).num_rows
    minix = mrecs[0]['index']
    if minix > ix + nrows - 1:
        return ix + nrows, rgix + 1, mrecs, urls
    rg = reader.read_row_group(rgix)
    while minix <= ix + nrows - 1:
        # todo, maybe: pretty wasteful
        row = rg.take([minix - ix]).to_pylist()[0]
        urls.append('/'.join([row['domain'], row['url'], row['filename']]))
        mrecs = mrecs[1:]
        if len(mrecs) == 0:
            break
        minix = mrecs[0]['index']
    return ix + nrows, rgix + 1, mrecs, urls


def find_product(
    filename_table_path: Path, manifest_path: Path, pid: str
) -> list[str]:
    if not filename_table_path.exists():
        raise FileNotFoundError(
            f"Filename table not found at {filename_table_path}."
        )

    from cytoolz import groupby
    from pyarrow import parquet as pq

    res = pq.read_table(
        filename_table_path,
        filters=[('stem', '=', pid.split(".")[0].lower())]
    )
    if len(res) == 0:
        raise FileNotFoundError(f"No products found matching {pid}.")
    manifest_map = json.loads(res.schema.metadata[b'mcodes'].decode('ascii'))
    res = res.to_pylist()
    manifest_map = {int(k): v for k, v in manifest_map.items()}
    mgroups = groupby(lambda rec: rec['mcode'], res)
    urls = []
    for mcode, mrecs in mgroups.items():
        manifest = find_manifest(manifest_map[mcode], manifest_path)
        meta = pq.read_metadata(manifest)
        reader = pq.ParquetFile(manifest).reader
        mrecs = sorted(mrecs, key=lambda r: r['index'])
        ix, rgix = 0, 0
        while rgix < meta.num_row_groups and len(mrecs) > 0:
            ix, rgix, mrecs, urls = _find_in_row_group(
                meta, ix, rgix, reader, mrecs, urls
            )
    return sorted(set(urls))
