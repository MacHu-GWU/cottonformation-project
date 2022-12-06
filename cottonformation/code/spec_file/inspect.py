# -*- coding: utf-8 -*-

"""
This module provides lots of utility.
"""

import typing as T
from rich import print as rprint
from .downloader import read_spec_file


def see_top_level_fields(spec_file_data: dict):
    for key, value in spec_file_data.items():
        print(key, type(value))


def see_property_types(spec_file_data: dict):
    # ---
    property_types: T.Dict[str, dict] = spec_file_data["PropertyTypes"]
    print(f"\nnumber of items in PropertyTypes = {len(property_types)}")

    # ---
    property_type_object_field_set = set()
    property_type_object_fields_key_set = set()

    for property_type_name, property_type_object in property_types.items():
        fields = list(property_type_object)
        fields.sort()
        fields_key = ", ".join(fields)
        property_type_object_fields_key_set.add(fields_key)

        for field in fields:
            property_type_object_field_set.add(field)

    property_type_object_field_list = list(property_type_object_field_set)
    property_type_object_field_list.sort()
    property_type_object_fields_key_list = list(property_type_object_fields_key_set)
    property_type_object_fields_key_list.sort()

    print("\nproperty type object has following attributes:")
    rprint(property_type_object_field_list)

    print("\nproperty type object has following attributes combination:")
    rprint(property_type_object_fields_key_list)

    # ---
    watch_on_fields_list = [
        "ItemType",
        "PrimitiveType",
        "Required",
        "Type",
        "UpdateType",
    ]
    watch_on_fields_set = set(watch_on_fields_list)
    possible_values: T.Dict[str, set] = dict()
    value: dict
    for _, value in property_types.items():
        for k, v in value.items():
            if k in watch_on_fields_set:
                try:
                    possible_values[k].add(value)
                except:
                    possible_values[k] = {
                        v,
                    }

    print("\nkey and possible values:")
    for key in watch_on_fields_list:
        value_set = possible_values[key]
        value_list = list(value_set)
        value_list.sort()
        print(f"- {key}: {value_list}")


def see_resource_types(spec_file_data: dict):
    # ---
    resource_types: T.Dict[str, dict] = spec_file_data["ResourceTypes"]
    print(f"\nnumber of items in ResourceTypes = {len(resource_types)}")

    # ---
    resource_type_object_field_set = set()
    resource_type_object_fields_key_set = set()

    for resource_type_name, resource_type_object in resource_types.items():
        fields = list(resource_type_object)
        fields.sort()
        fields_key = ", ".join(fields)
        resource_type_object_fields_key_set.add(fields_key)

        for field in fields:
            resource_type_object_field_set.add(field)

    resource_type_object_field_list = list(resource_type_object_field_set)
    resource_type_object_field_list.sort()
    resource_type_object_fields_key_list = list(resource_type_object_fields_key_set)
    resource_type_object_fields_key_list.sort()

    print("\nresource type object has following attributes:")
    rprint(resource_type_object_field_list)

    print("\nresource type object has following attributes combination:")
    rprint(resource_type_object_fields_key_list)

    # ---
    property_fields_set = set()
    possible_values: T.Dict[str, set] = dict()
    ignored_property_name_list = [
        "Documentation",
    ]
    ignored_property_name_set = set(ignored_property_name_list)
    for resource_type_name, resource_type_object in resource_types.items():
        if "Properties" in resource_type_object:
            properties = resource_type_object["Properties"]
            for prop, dct in properties.items():
                for key, value in dct.items():
                    if key not in ignored_property_name_set:
                        property_fields_set.add(key)
                        try:
                            possible_values[key].add(value)
                        except:
                            possible_values[key] = {
                                value,
                            }

    property_fields_list = list(property_fields_set)
    property_fields_list.sort()

    print("\nproperty name list:")
    rprint(property_fields_list)

    print("\nproperty and possible values:")
    for key in property_fields_list:
        value_set = possible_values[key]
        value_list = list(value_set)
        value_list.sort()
        print(f"- {key}: {value_list}")

    # ---
    attribute_fields_set = set()
    possible_values: T.Dict[str, set] = dict()
    for resource_type_name, resource_type_object in resource_types.items():
        if "Attributes" in resource_type_object:
            attributes = resource_type_object["Attributes"]
            for attr, dct in attributes.items():
                for key, value in dct.items():
                    attribute_fields_set.add(key)
                    try:
                        possible_values[key].add(value)
                    except:
                        possible_values[key] = {
                            value,
                        }

    attribute_fields_list = list(attribute_fields_set)
    attribute_fields_list.sort()

    print("\nattribute name list:")
    rprint(attribute_fields_list)

    print("\nattribute and possible values:")
    for key in attribute_fields_list:
        value_set = possible_values[key]
        value_list = list(value_set)
        value_list.sort()
        rprint(f"- {key}: {value_list}")


def see_resource_tags(spec_file_data: dict):
    resource_types: T.Dict[str, dict] = spec_file_data["ResourceTypes"]
    # print(f"\nnumber of items in ResourceTypes = {len(resource_types)}")
    common_tag_type = [
        "List-None-Json",
        "List-Tag-None"
    ]
    type_key_set = set()
    for resource_type_name, resource_type_object in resource_types.items():
        if "Properties" in resource_type_object:
            properties = resource_type_object["Properties"]
            for prop, dct in properties.items():
                if prop == "Tags":
                    type = dct.get("Type")
                    item_type = dct.get("ItemType")
                    primitive_type = dct.get("PrimitiveType")
                    primitive_item_type = dct.get("PrimitiveItemType")
                    key = f"{type}-{item_type}-{primitive_type}-{primitive_item_type}"
                    type_key_set.add(key)
                    if key not in common_tag_type:
                        print(resource_type_name, key)

    type_key_list = list(type_key_set)
    type_key_list.sort()
    print("\nvalid type key includes:")
    rprint(type_key_list)


def see_property_prop_type_is_self(spec_file_data: dict):
    """
    Some property type is a property object. however, that property object
    is undefined in cft-spec.json, those are usually
    """
    property_types: T.Dict[str, dict] = spec_file_data["PropertyTypes"]
    for property_type_name, property_type_object in property_types.items():
        if "Properties" in property_type_object:
            properties = property_type_object["Properties"]
            for key, dct in properties.items():
                typ = dct.get("Type", "THIS-IS-NOT-POSSIBLE")
                if key == typ:
                    desired_property_type_name = "{}.{}".format(
                        property_type_name.split(".")[0],
                        key,
                    )
                    if desired_property_type_name not in property_types:
                        print(f"{property_type_name} | {key} | {typ}")
