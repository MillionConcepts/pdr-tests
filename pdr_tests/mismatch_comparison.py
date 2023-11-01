from ast import literal_eval
from pathlib import Path
import sys

from hostess.caller import generic_python_endpoint
from hostess.shortcuts import chain
from hostess.subutils import run
import numpy as np
import pandas as pd

import pdr


SETTINGS = {}
PDRCD = f"cd {Path(pdr.__file__).parent}"


def make_checkout_cmds():
    return {
        "ref": chain([PDRCD, f"git checkout {SETTINGS['REF_BRANCH']}"]),
        "test": chain([PDRCD, f"git checkout {SETTINGS['TEST_BRANCH']}"]),
    }


def dump_data_subprocessed(rec, output_path, prefix):
    script = generic_python_endpoint(
        module="pdr_tests.comparison_hook",
        func="dump_to_output",
        payload=(rec, str(output_path.absolute()), prefix),
        argument_unpacking="*",
        interpreter=sys.executable,
    )
    run(script)


def get_outputs(rec, output_path, objname):
    ref_table, ref_dt = get_table(rec, output_path, objname, "ref")
    test_table, test_dt = get_table(rec, output_path, objname, "test")
    return ref_table, ref_dt, test_table, test_dt


def compare_values(r, t):
    value_mismatches = {}
    maxlen = min(len(r), len(t))
    for i in range(min(len(r.columns), len(t.columns))):
        rcol, tcol = r.iloc[:, i], t.iloc[:, i]
        rv, tv = rcol.values[:maxlen], tcol.values[:maxlen]
        val_mismatch = ~(rv == tv)
        try:
            val_mismatch = val_mismatch | (np.isnan(rv) & np.isnan(tv))
        except TypeError:
            pass
        if not val_mismatch.any():
            continue
        value_mismatches[i] = {
            "ref": rv[val_mismatch],
            "test": tv[val_mismatch],
        }
    return value_mismatches


def compare_outputs(r, r_dt, t, t_dt):
    comparison = {}
    if len(r) != len(t):
        comparison["row_count"] = {"ref": len(r), "test": len(t)}
    if len(r.columns) != len(t.columns):
        comparison["column_count"] = {"ref": len(r), "test": len(t)}
    missing_cols = set(r.columns).difference(t.columns)
    new_cols = set(t.columns.difference(r.columns))
    if len(missing_cols) + len(new_cols) > 0:
        comparison["column_names"] = {"new": new_cols, "missing": missing_cols}
    value_mismatches = compare_values(r, t)
    if len(value_mismatches) > 0:
        comparison["values"] = value_mismatches
    dtype_mismatches = compare_values(r_dt, t_dt)
    if len(dtype_mismatches) > 0:
        comparison["in_memory_dtypes"] = dtype_mismatches
    comparison["issues"] = list(comparison.keys())
    if len(comparison["issues"]) == 0:
        print(
            "No differences found, hash mismatch likely in-memory...", end=""
        )
    else:
        print(f"Issues found: {comparison['issues']}...", end="")
    return comparison


def get_table(rec, output_path, objname, pre):
    refname = f"{Path(rec['filename']).stem}_{pre}_{objname}"
    matches = [f for f in output_path.iterdir() if f.name == refname + ".csv"]
    if len(matches) > 1:
        raise OSError("Too many matches found.")
    if not matches[0].name.endswith(".csv"):
        raise NotATableError("Not a table, skipping.")
    dtype_path = output_path / (refname + "_dtypes.csv")
    return pd.read_csv(matches[0]), pd.read_csv(dtype_path)


class NotATableError(ValueError):
    pass


def check_mismatch(rec):
    checkout = make_checkout_cmds()
    print(f"checking {rec['filename']}...", end="")
    output_path = (SETTINGS["ROOT"] / rec["dataset"] / rec["product_type"])
    output_path.mkdir(exist_ok=True, parents=True)
    print("dumping ref...", end="")
    run(checkout["ref"])
    dump_data_subprocessed(rec, output_path, "ref")
    print("dumping test...", end="")
    run(checkout["test"])
    dump_data_subprocessed(rec, output_path, "test")
    print("loading outputs...", end="")
    comparisons = {}
    for objname in rec["mismatches"]:
        try:
            print(f"comparing outputs for {objname}...", end="")
            r, r_dt, t, t_dt = get_outputs(rec, output_path, objname)
            comparisons["objname"] = compare_outputs(r, r_dt, t, t_dt)
        except NotATableError:
            print("skipping non-table object...", end="")
    print("...done")
    return comparisons


def get_mismatches():
    testlog = pd.read_csv("combined_test_log_latest.csv")
    mismatches = testlog.loc[testlog["status"] == "hash mismatch"]
    recs = mismatches[
        ["filename", "dataset", "error", "product_type"]
    ].to_dict("records")
    for rec in recs:
        rec["mismatches"] = tuple(literal_eval(rec.pop("error")).keys())
    return recs
