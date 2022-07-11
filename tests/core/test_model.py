# -*- coding: utf-8 -*-

import pytest
import cottonformation as ctf


class TestAddable:
    def test_gid(self):
        assert ctf.Parameter("a", Type=ctf.Parameter.TypeEnum.String).gid == f"{ctf.Parameter.CLASS_TYPE}--a"
        assert ctf.Mapping("a").gid == f"{ctf.Mapping.CLASS_TYPE}--a"
        assert ctf.Equals("a", "v1", "v2").gid == f"{ctf.Condition.CLASS_TYPE}--a"
        assert ctf.Rule("a").gid == f"{ctf.Rule.CLASS_TYPE}--a"
        assert ctf.Resource("a").gid == f"{ctf.Resource.CLASS_TYPE}--a"
        assert ctf.Output("a", Value=1).gid == f"{ctf.Output.CLASS_TYPE}--a"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
