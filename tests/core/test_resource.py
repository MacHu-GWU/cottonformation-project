# -*- coding: utf-8 -*-

import pytest
import cottonformation as ctf


class TestResource:
    def test_ref(self):
        r = ctf.Resource(id="MyResource")
        assert isinstance(r.ref(), ctf.Ref)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
