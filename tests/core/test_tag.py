# -*- coding: utf-8 -*-

import pytest
from pytest import raises
from cottonformation.core.model import Tag, Parameter, constant


class TestTag:
    def test_init(self):
        with raises(TypeError):
            Tag()

        with raises(TypeError):
            Tag(1, 2)

        with raises(TypeError):
            Tag("k", 1)

        with raises(ValueError):
            Tag(p_Key="key" * 100, p_Value="value")

        with raises(ValueError):
            Tag(p_Key="key", p_Value="value" * 100)

        tags = Tag.make_many(
            dict_data=dict(name="ctf", stage="dev"),
            creator="alice@example.com",
        )
        assert tags[0].p_Key == "name"
        assert tags[1].p_Key == "stage"
        assert tags[2].p_Key == "creator"

        tags = Tag.make_many(
            dict_data=dict(name="ctf", stage="dev"),
        )
        assert tags[0].p_Key == "name"
        assert tags[0].p_Value == "ctf"
        assert tags[1].p_Key == "stage"
        assert tags[1].p_Value == "dev"

        tags = Tag.make_many(
            creator="alice@example.com",
        )
        assert tags[0].p_Key == "creator"
        assert tags[0].p_Value == "alice@example.com"

    def test_immutable(self):
        t = Tag("k", "v")
        # Tag is immutable
        with raises(Exception):
            t.p_Key = "k1"
        with raises(Exception):
            t.p_Value = "v1"

    def test_serialize(self):
        assert Tag("Name", "Alice").serialize() == {"Key": "Name", "Value": "Alice"}

        p = Parameter("Name", Type=Parameter.TypeEnum.String)
        assert Tag("Name", p.ref()).serialize() == {
            "Key": "Name",
            "Value": {constant.IntrinsicFunction.REF: "Name"},
        }


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
