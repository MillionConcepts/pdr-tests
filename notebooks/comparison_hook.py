from pathlib import Path

import pandas as pd
from dustgoggles.tracker import TrivialTracker

import pdr
from pdr.func import softquery


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
        loader = data.loaders[objname]
        info = softquery(
            loader.loader_function,
            loader.queries,
            {'data': data, 'name': objname, 'tracker': TrivialTracker()}
        )
        info['fmtdef_dt'][0].to_csv(
            Path(output_path) / (filestem + f"_{objname}_fmtdef.csv")
        )
    data.dump_browse(f"{Path(rec['filename']).stem}_{prefix}", output_path)
