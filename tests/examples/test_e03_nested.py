# -*- coding: utf-8 -*-

import pytest
from cottonformation.examples.s1_quick_start.e03_nested import (
    tpl_infra_tier, tpl_app_tier, tpl_app1, tpl_app2
)


def test():
    tpl_infra_tier.to_json()
    tpl_app_tier.to_json()
    tpl_app1.to_json()
    tpl_app2.to_json()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
