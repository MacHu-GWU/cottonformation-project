# -*- coding: utf-8 -*-

import pytest


def test():
    import cottonformation as ctf

    _ = ctf.Template
    _ = ctf.Parameter
    _ = ctf.Resource
    _ = ctf.Output
    _ = ctf.Rule
    _ = ctf.Mapping
    _ = ctf.Condition
    _ = ctf.ResourceGroup
    _ = ctf.Tag
    _ = ctf.Ref
    _ = ctf.GetAtt
    _ = ctf.ImportValue
    _ = ctf.Env
    _ = ctf.Stack

    from cottonformation.res import _imp

    _ = _imp


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
