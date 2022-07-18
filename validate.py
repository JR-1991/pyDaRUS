from re import sub
import yaml
import importlib
import json

from munch import Munch
from functions import validate_by_enum, validate_by_function

from pyDaRUS import Dataset

dataset = Dataset.from_dataverse_doi("doi:10.18419/darus-2340", filedir="example_data")
dataset.citation.add_grant_information(grant_number="14524", grant_agency="DFG")


scheme = yaml.safe_load(open("validation_scheme.yaml").read())
scheme = Munch.fromDict(scheme)

lib_name = scheme.get("lib_name")

total_report = {}

for name, fields in scheme.metadatablocks.items():

    # Get the block from dataset
    ds_block = dataset.metadatablocks.get(name)
    block_report = {}

    if not ds_block:
        print(f"Metadatablock {name} not present in dataset {dataset.p_id}")
        continue

    # Iterate over validation fields
    for field, config in fields.items():

        report = {}
        location = config.get("function")

        ds_field = getattr(ds_block, field)
        if config.get("mandatory") and not ds_field:
            block_report[field] = {
                "message": f"Mandatory field '{field}' is missing.",
            }
            continue

        if location:
            valid_function = validate_by_function(location, lib_name)

            if isinstance(ds_field, list):
                valids = []
                for index, sub_field in enumerate(ds_field):
                    sub_is_valid, sub_report = valid_function(sub_field)
                    valids.append(sub_is_valid)

                    if sub_report:
                        report[index] = sub_report

        # Add to general report
        if report:
            block_report[field] = report

    if block_report:
        total_report[name] = block_report


print(json.dumps(total_report, indent=2))
