# -*- coding: utf-8 -*-

import pytest
from pytest import raises
import cottonformation as ctf
from cottonformation.res import s3
from cottonformation.core.model import Tag


class TestResource:
    def test_ref(self):
        r = ctf.Resource(id="MyResource")
        assert isinstance(r.ref(), ctf.Ref)

    def test_tags(self):
        with raises(TypeError):
            s3.BucketPolicy("Res", p_Tags=Tag.make_many(k="v"))

        with raises(ValueError):
            b = s3.Bucket("Res", p_Tags=[Tag(p_Key="k", p_Value="v1"), Tag(p_Key="k", p_Value="v2")])
            _ = b.tags_dict

        b = s3.Bucket("Res", p_Tags=Tag.make_many(k1="v1"))
        assert b.tags_dict == dict(k1="v1")
        b.update_tags(k1="v1")
        assert b.tags_dict == dict(k1="v1")

        b.update_tags(k1="v11", overwrite=True)
        assert b.tags_dict == dict(k1="v11")

        b.update_tags(k1="v111", k2="v2")
        assert b.tags_dict == dict(k1="v11", k2="v2")

        b.update_tags(k1="v111", k2="v22", overwrite=True)
        assert b.tags_dict == dict(k1="v111", k2="v22")

    def test_serialize(self):
        p = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String)
        b1 = s3.Bucket(
            "b1",
            ra_DependsOn=p
        )
        b2 = s3.Bucket(
            "b2",
            ra_DependsOn=[p, b1],
        )

        assert b1.ra_Metadata == {}
        assert b1.ra_DependsOn == [p,]
        assert b1.serialize() == {'Type': 'AWS::S3::Bucket', 'Properties': {}}

        assert b2.ra_Metadata == {}
        assert b2.ra_DependsOn == [p, b1]
        assert b2.serialize() == {'Type': 'AWS::S3::Bucket', 'DependsOn': ['b1'], 'Properties': {}}

    def test_depends_on(self):
        p = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String)
        r1 = ctf.Resource("r1", ra_DependsOn=p)
        r2 = ctf.Resource("r2", ra_DependsOn=r1)
        r3 = ctf.Resource("r2", ra_DependsOn=r2)
        o1 = ctf.Output("o1", Value=0, DependsOn=r1)
        o2 = ctf.Output("o2", Value=0, DependsOn=r2)
        o3 = ctf.Output("o3", Value=0, DependsOn=r3)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
