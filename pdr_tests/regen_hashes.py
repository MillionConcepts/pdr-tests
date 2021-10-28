"""
regenerate all test_hashes, optionally dumping browse files as well. this
writes hashes to reference/temp/hash/$MISSION/$DATASET and browse products to
reference/temp/browse/$MISSION/$DATASET. If you like the products you see,
you can replace the long-term hashes in reference/hash/$MISSION/$DATASET with
the ones in the temp directory.

by default, this will attempt to download all products referenced in the
product index to data/$MISSION/$DATASET if they are not present.
"""

from pdr_tests.definitions.datasets import DATASET_TESTING_RULES
from pdr_tests.utilz.test_utilz import regenerate_test_hashes

# "settings"
dump_browse = True

# regenerate hashes for a single set:
regenerate_test_hashes("lro", "lroc", dump_browse=dump_browse)

# regenerate hashes for all defined sets:
# for mission_name, datasets in DATASET_TESTING_RULES.items():
#     for dataset in datasets.keys():
#         print(mission_name, dataset)
#         regenerate_test_hashes(mission_name, dataset, dump_browse)
