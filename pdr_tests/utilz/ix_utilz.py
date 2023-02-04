"""support objects and logging procedures for ix framework."""
import datetime as dt
import json
import logging
import os
import shutil
import time
import warnings
import xml.etree.ElementTree as ET
from hashlib import md5
from pathlib import Path
from typing import Mapping, Sequence, MutableMapping, Collection, Callable

import numpy as np
import pandas as pd
import pyarrow as pa
import requests
from dustgoggles.func import disjoint, intersection
from dustgoggles.structures import dig_for_values
from multidict import MultiDict

import pdr
from pdr.utils import check_cases, decompress
from pdr.parselabel.pds3 import get_pds3_pointers, read_pvl_label
from pdr.parselabel.utils import trim_label
from pdr_tests.settings import headers
from pdr_tests.utilz.dev_utilz import Stopwatch

REF_ROOT = Path(Path(__file__).parent.parent, "reference")
DATA_ROOT = Path(Path(__file__).parent.parent, "data")

pdrtestlog = logging.getLogger()
pdrtestlog.addHandler(logging.FileHandler("pdrtests.log"))
pdrtestlog.setLevel("INFO")


def stamp() -> str:
    return f"{dt.datetime.utcnow().isoformat()[:-7]}: "


def console_and_log(message, level="info", do_stamp=True, quiet=False):
    stamp_txt = stamp() if do_stamp is True else ""
    getattr(pdrtestlog, level)(f"{stamp_txt}{message}")
    if not quiet:
        print(f"{stamp_txt}{message}")


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
        blocks = obj._to_dict_of_blocks(copy=False)
        # sorting to improve consistency between pandas versions
        for dtype in sorted(blocks.keys()):
            if dtype == 'object':
                try:
                    json_repr = blocks[dtype].to_json()
                except UnicodeDecodeError:
                    # if there are very weird bytes, to_json will break
                    json_repr = blocks[dtype].astype(str).to_json()
                hasher.update(json_repr.encode('utf-8'))
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
    metadata = pdr.Metadata(read_pvl_label(check_cases(local_path)))
    files = [local_path.name]
    for target in dig_for_values(
        metadata,
        "^",
        mtypes=(MultiDict, dict),
        base_pred=lambda a, b: b.startswith(a)
    ):
        target = metadata.formatter(target)
        if isinstance(target, str):
            files.append(target)
        elif isinstance(target, Sequence):
            files.append(target[0])
        elif isinstance(target, int):
            continue
        elif isinstance(target, set):
            continue
        else:
            raise TypeError("what is this?")
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
    data_path, temp_path, row, skip_files=(), session=None
):
    files = json.loads(row["files"])
    session = session if session is not None else requests.Session()
    for file in files:
        if Path(data_path, file).exists():
            console_and_log(f"... {file} present, skipping ...")
            continue
        if any((file == skip_file for skip_file in skip_files)):
            continue
        url = f"{row['url_stem']}/{file}"
        session = verbose_temp_download(data_path, temp_path, url, session)
    return session


# TODO / note: this is yet one more download
#  thing that we should somehow unify and consolidate
def verbose_temp_download(
    data_path, temp_path, url, skip_quietly=True, session=None
):
    try:
        check_cases(Path(data_path, Path(url).name))
        if skip_quietly is False:
            console_and_log(
                f"{Path(url).name} already present, skipping download."
            )
        return session
    except FileNotFoundError:
        pass
    session = session if session is not None else requests.Session()
    console_and_log(f"attempting to download {url}.")
    response, session = get_response(session, url)
    if response is None:
        console_and_log(f"Download of {url} timed out.")
        return
    if not response.ok:
        urlsplit = url.split('.')
        url = url.split(urlsplit[-1])[0]+urlsplit[-1].lower()
        response = session.get(url, stream=True, headers=headers)
        if not response.ok:
            console_and_log(f"Download of {url} failed.")
            return session
        # TODO: is this still necessary? I think we fixed this.
        warnings.warn('File ending was changed to lowercase to complete download. '
                      'Please update "label" in selection rules to allow index to write and rerun.')
    with open(Path(temp_path, Path(url).name), "wb+") as fp:
        for ix, chunk in enumerate(response.iter_content(chunk_size=10**7)):
            print(f"getting chunk {ix} ({len(chunk)} bytes)")
            fp.write(chunk)
    shutil.move(
        Path(temp_path, Path(url).name), Path(data_path, Path(url).name)
    )
    console_and_log(f"completed download of {url}.")
    return session


def get_response(session, url):
    for _ in range(5):
        try:
            response = session.get(
                url, stream=True, headers=headers, timeout=4
            )
            return response, session
        except requests.ReadTimeout:
            console_and_log(
                f"slow response on {url}; pausing and reestablishing session"
            )
            time.sleep(1)
            session = requests.Session()
    return None, None


# noinspection HttpUrlsUsage
def assemble_urls(subset: pd.DataFrame):
    return "http://" + subset.domain + "/" + subset.url + "/" + subset.filename


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
    skiphash: bool
) -> tuple[pdr.Data, dict[str, str], dict[str, str]]:
    """
    read a product at a specified path, compute hashes from its data objects,
    log appropriately
    """
    watch, runtimes = Stopwatch(digits=3, silent=True), {}
    with warnings.catch_warnings():
        # We don't want to hear about UserWarnings we're intentionally raising
        # inside pdr (for things like unsupported object types, etc.)
        warnings.filterwarnings("ignore", category=UserWarning, module="pdr")
        watch.start()
        data = pdr.read(str(path), debug=debug)
        data.load("all")
        runtimes["readtime"] = watch.peek()
    console_and_log(
        f"Opened {product['product_id']} ({runtimes['readtime']} s)", quiet=quiet
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
