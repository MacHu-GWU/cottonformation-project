# -*- coding: utf-8 -*-

import pytest
from cottonformation.examples.e02_tagging import tpl


def test():
    _ = tpl


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
