from functools import reduce
from pyarrow import parquet
import pyarrow.compute
import pyarrow as pa
from pathlib import Path
from importlib import import_module
import pdr_tests


def the_main_function(input_manifest):
    input_manifest = Path(Path(Path(pdr_tests.__file__).parent, "node_manifests"), input_manifest)
    rules_modules = load_all_rules()
    relevant_rules = find_relevant_rules(rules_modules, input_manifest)
    check_coverage_in_chunks(input_manifest, relevant_rules)


def load_all_rules():
    """goes into every folder in definitions and pull in the rules for each product type."""
    definitions_dir = Path(Path(pdr_tests.__file__).parent, "definitions")
    rules_modules = {}
    for entry in definitions_dir.iterdir():
        if entry.is_dir():
            try:
                selection_rules = import_module(f'pdr_tests.definitions.{entry.name}.selection_rules')
            except ModuleNotFoundError:
                continue
            rules_modules[entry.name] = getattr(selection_rules, "file_information")
    return rules_modules


def find_relevant_rules(rules_modules, input_manifest):
    """check the manifest key for each rule to see if the match the input manifest"""
    relevant_rules = {}
    for key in rules_modules.keys():
        for subkey in rules_modules[key].keys():
            if str(rules_modules[key][subkey]["manifest"]).split('/')[-1] == str(input_manifest).split('/')[-1]:
                relevant_rules[key+'|'+subkey] = rules_modules[key][subkey]
    return relevant_rules


def check_coverage_in_chunks(
    input_file,
    relevant_rules,
    row_group_size=None,
    use_dictionary=None,
    version="2.6"
):
    output_file = Path(str(input_file).split('.parquet')[0]+'_coverage.parquet')
    write_kwargs, open_kwargs = {}, {}
    if row_group_size is not None:
        write_kwargs["row_group_size"] = row_group_size
    if use_dictionary is not None:
        open_kwargs["use_dictionary"] = use_dictionary
    sort_reader = parquet.ParquetFile(input_file)
    schema = sort_reader.read_row_group(0).schema
    schemadict = {
        name: type_ for name, type_ in zip(schema.names, schema.types)
    } | {'covered_by': pa.string()}
    sort_writer = parquet.ParquetWriter(
        output_file,
        version=version,
        schema=pa.schema(schemadict, schema.metadata),
        **open_kwargs
    )
    try:
        for group_ix in range(sort_reader.num_row_groups):
            chunk = sort_reader.read_row_group(group_ix)
            sort_writer.write_table(add_rule_labels(relevant_rules, chunk), **write_kwargs)
            del chunk
    finally:
        sort_writer.close()


def add_rule_labels(relevant_rules, table: pa.Table) -> pa.Table:
    """
    intakes a dictionary of relevant rules, for each rule make a list of boolean
    masks for each criteria based on if each row of the input table meets each criteria
    separately. Then combine the masks so that the mask is only true when all criteria
    met for a given row. Add a column to the input table that labels which rule has a combined
    mask that is true for each row.
    """
    rows = table.num_rows
    rule_labels = [''] * rows
    for key in relevant_rules.keys():
        rule = relevant_rules[key]
        masks = []
        if "url_must_contain" in rule.keys():
            for string in rule["url_must_contain"]:
                masks.append(pa.compute.match_substring(table["url"], string))
        if "url_regex" in rule.keys():
            for string in rule["url_regex"]:
                masks.append(pa.compute.match_substring_regex(table["url"], string))
        if "fn_ends_with" in rule.keys():
            ends = rule["fn_ends_with"]
            assert len(ends) == 1, "only one filename ending may be specified"
            masks.append(pa.compute.ends_with(table["filename"], pattern=ends[0]))
        if "fn_must_contain" in rule.keys():
            for string in rule["fn_must_contain"]:
                masks.append(pa.compute.match_substring(table["filename"], string))
        if "fn_regex" in rule.keys():
            for string in rule["fn_regex"]:
                masks.append(pa.compute.match_substring_regex(table["filename"], string))
        combined_mask = reduce(pa.compute.and_, masks)
        for index, match in enumerate(combined_mask):
            if match.as_py():
                rule_labels[index] = key
    return table.append_column("covered_by", pa.array(rule_labels))