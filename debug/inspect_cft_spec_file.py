# -*- coding: utf-8 -*-

"""
The purpose of this script is to inspect the data schema, data value of the
json file download from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

I have to deeply understand the data in spec file, so I can generate cottonformation
code out of it.
"""

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


if __name__ == "__main__":
    # inspect_resource_type()
    # inspect_property_type()
    # inspect_types()
    print(len(spec_data["PropertyTypes"]))
    print(len(spec_data["ResourceTypes"]))