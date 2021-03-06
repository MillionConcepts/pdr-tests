"""support objects and logging procedures for ix framework."""
import datetime as dt
import json
import logging
import os
import shutil
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
    make stable byte array from python object. the general case of this is,
    I think, impossible, or at least implementation-dependent, so I am
    attempting to cover the specific cases we have...this is a first pass.
    """
    hasher = hash_function(usedforsecurity=False)
    if isinstance(obj, np.ndarray):
        for line in obj:
            hasher.update(line)
    elif isinstance(obj, pd.DataFrame):
        # TODO: I am not sure why object ('O') dtypes do not appear to
        #  have stable byte-level representations without first converting to
        #  python objects. something strange is happening
        #  behind the numpy API. this plausibly also affects ndarrays, but
        #  I don't know if we're ever working with ndarrays with object dtypes.
        blocks = obj._to_dict_of_blocks(copy=False)
        # sorting to improve consistency between pandas versions
        for dtype in sorted(blocks.keys()):
            # TODO, maybe: going by row or column is stunningly slow for
            #  really long or wide tables. trying this and seeing if it takes
            #  too much memory.
            if dtype == 'object':
                # for ix in block.index:
                #     hasher.update(str(block.loc[ix].tolist()).encode('utf-8'))
                hasher.update(blocks[dtype].to_string().encode('utf-8'))
            else:
                # TODO, maybe: the arrays underlying dataframes are
                #  typically not stored in C-contiguous order. copying the
                #  array is somewhat memory-inefficient. another solution is
                #  to dump each line as string or bytes -- like we do for
                #  object dtypes above -- which would be slower but smaller.
                # for ix in block.index:
                #     hasher.update(block.loc[ix].values.copy())
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
        # ignore text-type objects for now
        if isinstance(data[key], (MultiDict, str)):
            continue
        hashes[key] = checksum_object(data[key])
    return hashes


def get_nodelist(xmlfile):
    return ET.parse(xmlfile).getroot().findall(".//*")


def make_pds4_row(xmlfile):
    nodelist = get_nodelist(xmlfile)
    return {
        "label_file": str(xmlfile).split('/')[-1],
        "product_id": next(
            node for node in nodelist if "logical_identifier" in node.tag
        ).text,
        "files": json.dumps(
            [node.text for node in nodelist if "file_name" in node.tag]
            + [str(xmlfile)]
        ),
    }


def make_pds3_row(local_path):
    metadata = pdr.Metadata(read_pvl_label(str(local_path)))
    pointers = get_pds3_pointers(metadata)
    files = [local_path.name]
    for pointer in pointers:
        target = metadata.metaget_(pointer)
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


def download_product_row(data_path, temp_path, row, skip_files=()):
    files = json.loads(row["files"])
    for file in files:
        if Path(data_path, file).exists():
            console_and_log(f"... {file} present, skipping ...")
            continue
        if any((file == skip_file for skip_file in skip_files)):
            continue
        url = f"{row['url_stem']}/{file}"
        verbose_temp_download(data_path, temp_path, url)


# TODO / note: this is yet one more download
#  thing that we should somehow unify and consolidate
def verbose_temp_download(data_path, temp_path, url, skip_quietly=True):
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
    response = requests.get(url, stream=True, headers=headers)
    if not response.ok:
        urlsplit = url.split('.')
        url = url.split(urlsplit[-1])[0]+urlsplit[-1].lower()
        response = requests.get(url, stream=True, headers=headers)
        if not response.ok:
            console_and_log(f"Download of {url} failed.")
            return
        warnings.warn('File ending was changed to lowercase to complete download. '
                      'Please update "label" in selection rules to allow index to write and rerun.')
    with open(Path(temp_path, Path(url).name), "wb+") as fp:
        for chunk in response.iter_content(chunk_size=10**7):
            fp.write(chunk)
    shutil.move(
        Path(temp_path, Path(url).name), Path(data_path, Path(url).name)
    )
    console_and_log(f"completed download of {url}.")


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
