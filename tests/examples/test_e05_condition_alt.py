# -*- coding: utf-8 -*-

import os
import pytest


def test():
    if "CI" not in os.environ:
        from cottonformation.examples.s1_quick_start.e05_condition_alt import tpl
        tpl.to_json()


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
