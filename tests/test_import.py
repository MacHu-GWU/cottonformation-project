# -*- coding: utf-8 -*-

import pytest


def test():
    import cottonformation as cf

    _ = cf.Template
    _ = cf.Parameter
    _ = cf.Resource
    _ = cf.Output
    _ = cf.Rule
    _ = cf.Mapping
    _ = cf.Condition
    _ = cf.ResourceGroup
    _ = cf.Tag
    _ = cf.Ref
    _ = cf.GetAtt
    _ = cf.ImportValue
    _ = cf.Env
    _ = cf.Stack

    _ = cf.DeletionPolicyEnum
    _ = cf.UpdateReplacePolicyEnum

    _ = cf.Ref
    _ = cf.Base64
    _ = cf.Cidr
    _ = cf.FindInMap
    _ = cf.GetAtt
    _ = cf.GetAZs
    _ = cf.ImportValue
    _ = cf.Join
    _ = cf.Select
    _ = cf.Split
    _ = cf.Sub

    _ = cf.Equals
    _ = cf.If
    _ = cf.Not
    _ = cf.And
    _ = cf.Or

    _ = cf.AWS_ACCOUNT_ID
    _ = cf.AWS_NOTIFICATION_ARNS
    _ = cf.AWS_NO_VALUE
    _ = cf.AWS_PARTITION
    _ = cf.AWS_REGION
    _ = cf.AWS_STACK_ID
    _ = cf.AWS_STACK_NAME
    _ = cf.AWS_URL_SUFFIX

    from cottonformation.res import _imp

    _ = _imp


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
