from pathlib import Path

import pandas as pd

import pdr


def dump_to_output(rec, output_path, prefix):
    data = pdr.read(rec['filename'])
    filestem = f"{Path(rec['filename']).stem}_{prefix}"
    for objname in rec['mismatches']:
        data.load(objname)
        if not isinstance((obj := getattr(data, objname)), pd.DataFrame):
            continue
        obj.dtypes.to_csv(
            Path(output_path) / (filestem + f"_{objname}_dtypes.csv")
        )
    data.dump_browse(f"{Path(rec['filename']).stem}_{prefix}", output_path)
