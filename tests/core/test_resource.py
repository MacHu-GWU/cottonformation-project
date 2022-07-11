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
        with raises(TypeError):  # some resources don't support Tags
            s3.BucketPolicy("Res", p_Tags=Tag.make_many(k="v"))

        with raises(ValueError):  # cannot have duplicate tag key
            b = s3.Bucket(
                "Res",
                p_Tags=[
                    Tag(p_Key="k", p_Value="v1"),
                    Tag(p_Key="k", p_Value="v2"),
                ],
            )
            _ = b.tags_dict

        b = s3.Bucket("Res", p_Tags=Tag.make_many(k1="v1"))
        assert b.tags_dict == dict(k1="v1")

    def test_update_tags(self):
        b = s3.Bucket("Res")
        b.update_tags(k1="v1")
        assert b.tags_dict == dict(k1="v1")

        with pytest.raises(KeyError):
            b.update_tags(k1="v2")

        b.update_tags(k1="v2", overwrite_existing=True)
        assert b.tags_dict == dict(k1="v2")

        b.update_tags(k1="v3", k2="v2", overwrite_existing=True)
        assert b.tags_dict == dict(k1="v3", k2="v2")

    def test_serialize(self):
        p = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String)
        b1 = s3.Bucket("b1", ra_DependsOn=p)
        b2 = s3.Bucket(
            "b2",
            ra_DependsOn=[p, b1],
        )

        assert b1.ra_Metadata == {}
        assert b1.ra_DependsOn == [
            p,
        ]
        assert b1.serialize() == {"Type": "AWS::S3::Bucket", "Properties": {}}

        assert b2.ra_Metadata == {}
        assert b2.ra_DependsOn == [p, b1]
        assert b2.serialize() == {
            "Type": "AWS::S3::Bucket",
            "DependsOn": ["b1"],
            "Properties": {},
        }

    def test_eval(self):
        b = s3.Bucket("MyBucket", p_BucketName="my-bucket")
        assert b.eval() == {"Ref": "MyBucket"}

    def test_depends_on(self):
        p = ctf.Parameter("p", Type=ctf.Parameter.TypeEnum.String)

        r1 = ctf.Resource("r1", ra_DependsOn=p)
        r2 = ctf.Resource("r2", ra_DependsOn=r1)
        r3 = ctf.Resource("r2", ra_DependsOn=r2)

        o1 = ctf.Output("o1", Value=0, DependsOn=r1)
        o2 = ctf.Output("o2", Value=0, DependsOn=r2)
        o3 = ctf.Output("o3", Value=0, DependsOn=r3)

    def test_support_tags(self):
        assert s3.BucketPolicy.support_tags() is False
        assert s3.Bucket.support_tags() is True


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
