from pathlib import Path

from pdr_tests.utilz.coverage_utilz import the_main_function

for manifest in Path('pdr_tests/node_manifests').iterdir():
    if not manifest.name.endswith('parquet'):
        continue
    if 'coverage' in manifest.name:
        continue
    if Path(
        'pdr_tests/node_manifests', f"{manifest.stem}_coverage.parquet"
    ).exists():
        continue
    print(manifest)
    the_main_function(manifest.name)

