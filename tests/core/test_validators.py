# -*- coding: utf-8 -*-

import os
import pytest

import attr
from cottonformation.core.model import vali


@attr.s
class Data:
    value = attr.ib()


class TestValidators:
    def test(self):
        data = Data("a_str")
        vali._test(data, attr.fields(Data).value, data.value)

        data = Data(1)
        vali._test(data, attr.fields(Data).value, data.value)

        with pytest.raises(TypeError):
            data = Data(3.14)
            vali._test(data, attr.fields(Data).value, data.value)


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
