# -*- coding: utf-8 -*-

"""
The purpose of this script is to inspect the data schema, data value of the
json file download from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

I have to deeply understand the data in spec file, so I can generate cottonformation
code out of it.
"""

import json
from pathlib_mate import Path
from cottonformation.code.spec import (
    download_spec_file, read_spec_file,
)

download_spec_file()
spec_data = read_spec_file()


def inspect_resource_type():
    """
    Conclusion:

    - All resource key follow the format: SystemIdentifier::ProductIdentifier::ResourceType
    """
    resource_keys = list(spec_data["ResourceTypes"].keys())
    for k in resource_keys:
        # the key is like SystemIdentifier::ProductIdentifier::ResourceType
        # ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html
        system_name, service_name, resource_name = k.split("::")
        print(k, "|", system_name, service_name, resource_name)


def inspect_property_type():
    """
    Conclusion:

    - All resource key follow the format: SystemIdentifier::ProductIdentifier::ResourceType.PropertyName
        except one: ``Tag``
    """
    property_keys = list(spec_data["PropertyTypes"].keys())
    for k in property_keys:
        # the key is like SystemIdentifier::ProductIdentifier::ResourceType.PropertyName
        # ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html
        if k == "Tag":
            system_name, service_name, property_fullname = k.split("::")
            resource_name, property_name = property_fullname.split(".")
            print(k, "|", system_name, service_name, resource_name)
        else:
            print(k)


def inspect_types():
    type_set, primitive_type_set, item_type_set, primitive_item_type_set = (
        set(), set(), set(), set()
    )

    NA = "NotAvailable"

    def update_all_type_set(dct):
        type_set.add(dct.get("Type", NA))
        primitive_type_set.add(dct.get("PrimitiveType", NA))
        item_type_set.add(dct.get("ItemType", NA))
        primitive_item_type_set.add(dct.get("PrimitiveItemType", NA))

    for prop_type_dct in spec_data["PropertyTypes"].values():
        for prop_dct in prop_type_dct.get("Properties", {}).values():
            update_all_type_set(prop_dct)

    for resource_type_dct in spec_data["ResourceTypes"].values():
        for prop_dct in resource_type_dct.get("Properties", {}).values():
            update_all_type_set(prop_dct)

        for attr_dct in resource_type_dct.get("Attributes", {}).values():
            update_all_type_set(attr_dct)

    all_type_list = []
    all_type_set = [type_set, primitive_type_set, item_type_set, primitive_item_type_set]
    for ts in all_type_set:
        ts.remove(NA)
        all_type_list.append(list(ts))

    print(f"type: {all_type_list[0]}")
    print(f"primitive_type: {all_type_list[1]}")
    print(f"item_type: {all_type_list[2]}")
    print(f"primitive_item_type: {all_type_list[3]}")


def create_alfred_cloudformation_data_file():
    """
    Generate data file for alfred full text search anything:

    https://github.com/MacHu-GWU/afwf_fts_anything-project
    """
    spec_data = read_spec_file()

    alfred_data = list()

    for res_id, res_dct in spec_data["ResourceTypes"].items():
        if "Documentation" not in res_dct:
            continue
        print(res_id)
        _, service, resource = res_id.split("::")
        doc_link = res_dct["Documentation"]
        dct = dict(
            title=f"Resource: {service} | {resource}",
            subtitle=f"open {doc_link}",
            arg=doc_link,
        )
        alfred_data.append(dct)

    for prop_id, prop_dct in spec_data["PropertyTypes"].items():
        if "Documentation" not in prop_dct:
            continue
        if prop_id == "Tag":
            continue
        _, service, prop_full_name = prop_id.split("::")
        resource, prop_name = prop_full_name.split(".")

        doc_link = prop_dct["Documentation"]
        dct = dict(
            title=f"Property: {service} | {resource} - {prop_name}",
            subtitle=f"open {doc_link}",
            arg=doc_link,
        )
        alfred_data.append(dct)

    p = Path.home().append_parts(".alfred-fts", "cloudformation.json")
    p.write_text(json.dumps(alfred_data, indent=4))


if __name__ == "__main__":
    # inspect_resource_type()
    # inspect_property_type()
    # inspect_types()
    # print(len(spec_data["PropertyTypes"]))
    # print(len(spec_data["ResourceTypes"]))

    create_alfred_cloudformation_data_file()
