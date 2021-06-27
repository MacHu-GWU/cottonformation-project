# -*- coding: utf-8 -*-

import pytest
from cottonformation.code.spec import gen_code


def test_import():
    gen_code(dry_run=True)
    import cottonformation.res._imp
    _ = cottonformation.res._imp


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
