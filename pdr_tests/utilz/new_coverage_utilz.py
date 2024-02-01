from ast import literal_eval
import re

from dustgoggles.structures import listify
import pandas as pd
from pyarrow import parquet as pq

MPIVOTS = ("dataset_pds", "dataset_ix", "ptype", "volume")
MFILTERS = ("cov", "ucov", "inc", "all") 
MTYPES = ("paths", "stats")
METRIC_FN_PATTERN = re.compile(
    rf"(?P<name>(\w|_)+?)_(?P<pivot>{'|'.join(MPIVOTS)})_"
    rf"((?P<filt>{'|'.join(MFILTERS)})_)?"
    rf"((?P<mtype>{'|'.join(MTYPES)})\.csv)"
)


def get_domain(manifest_fn):
    domains = set()
    meta = pq.read_metadata(manifest_fn)
    for n in range(meta.num_row_groups):
        rg = meta.row_group(n)
        domains.update(
            [rg.column(0).statistics.min, rg.column(0).statistics.max]
        )
    if len(domains) > 1:
        raise ValueError("multiple domains in this manifest.")
    return domains.pop()


def _maybeeval(x):
    try:
        return literal_eval(x)
    except ValueError:
        return x


class MetricLoader:
    def __init__(self, path):
        self.metric_path = path / "coverage_metrics"
        self.manifest_path = path / "coverage_manifests"

    @staticmethod
    def _compatible(match, filt, pivot, mtype):
        filt = None if mtype == "stats" else filt
        return all(
            match[t] == v 
            for t, v in zip(("pivot", "filt", "mtype"), (pivot, filt, mtype))
        )

    def make_urls(self, pathtable):
        domains = {}
        for manifest_name in pathtable['manifest'].unique():
            mpaths = [
                m for m in self.manifest_path.iterdir()
                if m.name.startswith(manifest_name)
            ]
            if len(mpaths) == 0:
                raise FileNotFoundError("no matching manifest found")
            domains[manifest_name] = get_domain(mpaths[0])
        wheredf = pathtable[['path', 'manifest']].copy()
        wheredf['domain'] = None
        for manifest, group in wheredf.groupby('manifest'):
            wheredf.loc[group.index, 'domain'] = domains[manifest]
        return "https://" + wheredf['domain'] + "/" + wheredf["path"]

    def load(self, names, pivot="dataset_pds", mtype="stats", filt="all"):
        if filt != "all" and mtype == "stats":
            raise ValueError(
                "filtered stats files do not exist. do not specify a value "
                "for the 'filt' parameter if 'mtype' is 'stats'."
            )
        names = listify(names)
        for name, val, opt in zip(
            ("pivot", "filt", "mtype"),
            (pivot, filt, mtype), 
            (MPIVOTS, MFILTERS, MTYPES)
        ):
            if val in opt:
                continue
            raise ValueError(f"invalid option: {name} must be one of {opt}.")
        dfs, unmatched = {}, set(names)
        for p in self.metric_path.iterdir():
            if (match := re.match(METRIC_FN_PATTERN, p.name)) is None:
                continue
            pmatch = {n for n in names if re.match(n, match['name'])}
            if len(pmatch) == 0:
                continue
            unmatched.difference_update(pmatch)
            if not self._compatible(match, filt, pivot, mtype):
                continue
            dfs[match['name']] = pd.read_csv(p)
        if len(unmatched) > 0:
            raise FileNotFoundError(
                f"no matching files found for the following names:"
                f"{', '.join(unmatched)}"
            )
        if len(dfs) == 1:
            df = tuple(dfs.values())[0]
            df['manifest'] = tuple(dfs.keys())[0]
        else:
            for k, v in dfs.items():
                v['manifest'] = k
            df = pd.concat(list(dfs.values()))
        for k, v in df.items():
            if isinstance((sv := v.iloc[0]), str) and sv.startswith("["):
                df[k] = v.map(_maybeeval)
        return df.reset_index(drop=True).copy()


def pathtable_to_treeframe(pathtable):
    from hostess.directory import make_treeframe
    
    pathtable = pathtable.copy()
    pathtable['directory'], pathtable['size'] = False, 0
    tf = make_treeframe(pathtable).drop(columns=['size', 'suffix'])
    tf['extension'] = pathtable['extension']
    return tf


def tf_pathcounts(tf, dropna=False):
    return tf.loc[
        :, [c for c in tf.columns if isinstance(c, int)]
    ].value_counts(dropna=dropna)
