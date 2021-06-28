# -*- coding: utf-8 -*-

import pytest
import attr
from pytest import raises, approx
from cottonformation.core.model import (
    get_id, get_key_value_dict, remove_id_and_empty,
)


def test_get_key_value_dict():
    @attr.s
    class Credential:
        username: str = attr.ib()
        password: str = attr.ib()

    @attr.s
    class Person:
        name: str = attr.ib()
        cred: Credential = attr.ib()

    p = Person(name="Alice", cred=Credential(username="user", password="pass"))
    assert isinstance(get_key_value_dict(p)["cred"], Credential)


def test_remove_id_and_empty():
    before_data = {
        "id": 1,
        "key": "good_key",
        "good_value": False,
        "bad_value": None,
        "good_list": [1, 2, 3],
        "bad_list": [],
        "good_dict": {"a": 1},
        "bad_dict": {},
    }
    after_data = remove_id_and_empty(before_data)
    assert set(after_data) == {
        "key",
        "good_value",
        "good_list",
        "good_dict",
    }


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
