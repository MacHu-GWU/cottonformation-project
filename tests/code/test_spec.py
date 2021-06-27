# -*- coding: utf-8 -*-

import pytest

from cottonformation.code import spec


class TestCftSpec:
    def test_new(self):
        cft_spec = spec.CftSpec.new()

def test_order_by_dependencies():
    dependency_mapper = {
        6: {5, 4, 3, 2, 1},
        5: {4, 1},
        4: {3, 2},
        3: {1, 2},
        2: {1,},
        1: {},
    }
    assert spec.order_by_dependencies(dependency_mapper) == ([1, 2, 3, 4, 5, 6], [])

    dependency_mapper = {
        3: {},
        2: {},
        1: {},
    }
    assert spec.order_by_dependencies(dependency_mapper) == ([3, 2, 1], [])

    dependency_mapper = {
        3: {2,},
        2: {},
        1: {},
    }
    assert spec.order_by_dependencies(dependency_mapper) == ([2, 1, 3], [])

    dependency_mapper = {
        3: {2,},
        2: {1,},
        1: {3,},
    }
    assert spec.order_by_dependencies(dependency_mapper) == ([3, 2, 1], [3, 2, 1])


# def test_find_type_hint_and_validator():
#     test_cases = [
#         (
#             None,  # type
#             "Integer",  # primitive_type
#             None,  # item_type
#             None,  # primitive_item_type
#             "int",  # exp_type_hint
#             "attr.validators.instance_of(int)",  # exp_validator
#         ),
#         (
#             "Data",  # type
#             None,  # primitive_type
#             None,  # item_type
#             None,  # primitive_item_type
#             "Data",  # exp_type_hint
#             "attr.validators.instance_of(Data)",  # exp_validator
#         ),
#         (
#             "List",  # type
#             None,  # primitive_type
#             None,  # item_type
#             "String",  # primitive_item_type
#             "typing.List[str]",  # exp_type_hint
#             "attr.validators.deep_iterable(member_validator=attr.validators.instance_of(str), iterable_validator=attr.validators.instance_of(list))",
#         # exp_validator
#         ),
#         (
#             "List",  # type
#             None,  # primitive_type
#             "Data",  # item_type
#             None,  # primitive_item_type
#             "typing.List[Data]",  # exp_type_hint
#             "attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Data), iterable_validator=attr.validators.instance_of(list))",
#         # exp_validator
#         ),
#     ]
#
#     for tp in test_cases:
#         (
#             type_,
#             primitive_type,
#             item_type,
#             primitive_item_type,
#             exp_type_hint,
#             exp_validator,
#         ) = tp
#         type_hint, validator = find_type_hint_and_validator(
#             type_, primitive_type, item_type, primitive_item_type)
#         assert type_hint == type_hint
#         assert validator == validator


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
