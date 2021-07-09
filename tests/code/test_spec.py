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


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
