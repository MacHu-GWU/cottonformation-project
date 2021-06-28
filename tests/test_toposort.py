# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from toposort import toposort, toposort_flatten


def test():
    # no mistake
    data = {
        1: {2, 3, 4},
        2: set(),
        3: {4,},
        4: {2, 5},
        5: {6,},
        6: set(),
        26: {1, 2, 3, 4},
    }
    assert list(toposort(data)) == [{2, 6}, {5}, {4}, {3}, {1}, {26}]

    # Two mistakes: (1) Y doesn't exist, and (2) circular dependency between E and A
    data = {
        1: {2, 3, 4},
        2: set(),
        3: {4, },
        4: {2, 5},
        5: {1, },
        6: set(),
        26: {1, 2, 3, 4, 25},
    }
    with raises(Exception):
        list(toposort(data))

    # One minor syntax mistakes: (1) Y doesn't exist
    data = {
        1: {2, 3, 4},
        2: set(),
        3: {4, },
        4: {2, 5},
        5: {6, },
        6: set(),
        26: {1, 2, 3, 4, 25},
    }
    assert list(toposort(data)) == [{25, 2, 6}, {5}, {4}, {3}, {1}, {26}]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
