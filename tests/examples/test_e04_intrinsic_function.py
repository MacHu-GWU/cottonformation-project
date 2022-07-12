# -*- coding: utf-8 -*-

import pytest
from cottonformation.examples.s1_quick_start.e04_intrinsic_function import tpl


def test():
    tpl.to_json()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
