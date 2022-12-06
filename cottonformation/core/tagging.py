# -*- coding: utf-8 -*-

"""
This module implements the AWS CloudFormation resource tags handling logics.

Due to the historical reason, the AWS CloudFormation resource tags
type definition is not consistent, we have to add more logic to handle both
old tag type and new tag type.
"""

import typing as T
import attr

from .constant import AttrMeta

if T.TYPE_CHECKING:  # pragma: no cover
    from .model import Resource


def get_tags_attribute_property_data(res_class: T.Type["Resource"]) -> dict:
    return attr.fields_dict(res_class)[AttrMeta.TAGS].metadata[AttrMeta.DATA]


def get_tag_type_hash_key(res_class: T.Type["Resource"]) -> str:
    data = get_tags_attribute_property_data(res_class)
    type = data.get("Type")
    item_type = data.get("ItemType")
    primitive_type = data.get("PrimitiveType")
    primitive_item_type = data.get("PrimitiveItemType")
    return f"{type}-{item_type}-{primitive_type}-{primitive_item_type}"


def get_tags_if_list_tag(res: "Resource") -> T.Dict[str, str]:
    if res.p_Tags is None:  # pragma: no cover
        return dict()
    else:
        dct = dict()
        for tag in res.p_Tags:
            data = tag.serialize()
            dct[data["Key"]] = data["Value"]
        return dct


def put_tags_if_list_tag(res: "Resource", tags: T.Dict[str, str]):
    if len(tags) == 0:  # pragma: no cover
        res.p_Tags = None
    else:
        converter = attr.fields_dict(res.__class__)[AttrMeta.TAGS].converter

        # special handling
        if res.AWS_OBJECT_TYPE == "AWS::AutoScaling::AutoScalingGroup":
            res.p_Tags = converter(
                [
                    {"rp_Key": key, "rp_Value": value, "rp_PropagateAtLaunch": True}
                    for key, value in tags.items()
                ]
            )
            return

        try:
            data = [{"p_Key": key, "p_Value": value} for key, value in tags.items()]
            res.p_Tags = converter(data)
        except TypeError:
            data = [{"rp_Key": key, "rp_Value": value} for key, value in tags.items()]
            converter = attr.fields_dict(res.__class__)[AttrMeta.TAGS].converter
            res.p_Tags = converter(data)


def get_tags_if_list_json(res: "Resource") -> T.Dict[str, str]:
    if res.p_Tags is None:  # pragma: no cover
        return dict()
    else:
        return {dct["Key"]: dct["Value"] for dct in res.p_Tags}


def put_tags_if_list_json(res: "Resource", tags: T.Dict[str, str]):
    if len(tags) == 0:  # pragma: no cover
        res.p_Tags = None
    else:
        res.p_Tags = [{"Key": key, "Value": value} for key, value in tags.items()]


def get_tags_if_map(res: "Resource") -> T.Dict[str, str]:
    if res.p_Tags is None:  # pragma: no cover
        return dict()
    else:
        return res.p_Tags.copy()


def put_tags_if_map(res: "Resource", tags: T.Dict[str, str]):
    if len(tags) == 0:  # pragma: no cover
        res.p_Tags = None
    else:
        res.p_Tags = tags


def get_tags_if_tags(res: "Resource") -> T.Dict[str, str]:
    """
    The aws cft definition is wrong, see
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html
    """
    return dict()


def put_tags_if_tags(res: "Resource", tags: T.Dict[str, str]):
    """
    The aws cft definition is wrong, see
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-insightrule-tags.html
    """
    return


getter_putter_mapper = {
    "List-None-None-Json": {
        "getter": get_tags_if_list_json,
        "putter": put_tags_if_list_json,
    },
    "List-PolicyTag-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-Tag-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-TagEntry-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-TagFormat-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-TagProperty-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-Tags-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "List-TagsEntry-None-None": {
        "getter": get_tags_if_list_tag,
        "putter": put_tags_if_list_tag,
    },
    "Map-None-None-String": {"getter": get_tags_if_map, "putter": put_tags_if_map},
    "None-None-Json-None": {"getter": get_tags_if_map, "putter": put_tags_if_map},
    "Tags-None-None-None": {
        "getter": get_tags_if_tags,
        "putter": put_tags_if_tags,
    },
}


def get_tags(res: "Resource") -> T.Dict[str, str]:
    hash_key = get_tag_type_hash_key(res.__class__)
    getter = getter_putter_mapper[hash_key]["getter"]
    return getter(res)


def put_tags(res: "Resource", tags: T.Dict[str, str]):
    hash_key = get_tag_type_hash_key(res.__class__)
    putter = getter_putter_mapper[hash_key]["putter"]
    return putter(res, tags)


def update_tags(
    res: "Resource",
    tags: T.Dict[str, str],
    mode_skip: bool = False,
    mode_overwrite: bool = False,
    mode_raise: bool = False,
) -> T.Tuple[T.Dict[str, str], T.Dict[str, str]]:
    """
    Update CloudFormation resource tags.

    :param res: the :class:`~cottonformation.core.model.Resource` object
    :param tags: key value tags in python dictionary
    :param mode_skip: if the key already exists, then skip it
    :param mode_overwrite: if the key already exists, then overwrite it with new value
    :param mode_raise: if the key already exists, then raise error

    :return: the before and after tags in python dictionary.
    """
    flag_sum = sum([mode_skip, mode_overwrite, mode_raise])
    if flag_sum == 0:
        mode_raise = True
    elif flag_sum > 1:
        raise ValueError(
            "only one of the 'mode_skip', 'mode_overwrite', 'mode_raise' "
            "can be True!"
        )
    existing_tags = get_tags(res)
    if len(tags) == 0:
        return existing_tags, existing_tags.copy()

    new_tags = existing_tags.copy()
    if mode_skip:
        for k, v in tags.items():
            new_tags.setdefault(k, v)
    elif mode_overwrite:
        new_tags.update(tags)
    elif mode_raise:
        for k, v in tags.items():
            if k not in new_tags:
                new_tags[k] = v
            else:
                raise KeyError(
                    f"{k!r} already exists in Tags! "
                    f"Maybe you want to set on the ``mode_overwrite = True``."
                )

    put_tags(res, new_tags)

    return existing_tags, new_tags
