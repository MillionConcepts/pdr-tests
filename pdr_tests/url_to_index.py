"""
script for transforming a list of label urls into an index formatted for
`regenerate_test_hashes()` (see regen_hashes.py) and `test_dataset()` (see
test_everything_gratuitously.py).

by default, it looks in reference/temp/index_label_cache/ for labels, and
downloads them if they're not present...which, if they're attached labels,
may be a lot of downloading. you can pass the argument `data_path` to
`label_urls_to_test_index()` to make it look somewhere else if you prefer. in
some cases, it might be most sensible just to aim it at the data directory
(data/$MISSION/$DATASET/), but we don't want this script to default to mucking
up the nice clean data directory if a url proves malformed or the downloader
gets confused or something.
"""
import pandas as pd

from pdr_tests.utilz.test_utilz import label_urls_to_test_index


test_case = "ch1"

label_urls = pd.read_csv(
    f"reference/url_lists/{test_case}.csv", header=None
).iloc[:, 0]
results = label_urls_to_test_index(label_urls)
results.to_csv(f"reference/index/{test_case}.csv", index=None)
