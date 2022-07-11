# -*- coding: utf-8 -*-

import pytest
from cottonformation.examples.e03_nested import tpl_infra_tier


def test():
    _ = tpl_infra_tier


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
