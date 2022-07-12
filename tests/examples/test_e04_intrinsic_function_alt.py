# -*- coding: utf-8 -*-

import os
import pytest
from cottonformation.examples.s1_quick_start.e04_intrinsic_function_alt import tpl


def test():
    if "CI" not in os.environ:
        tpl.to_json()


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
