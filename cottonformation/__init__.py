# -*- coding: utf-8 -*-

"""
Copyright (c) 2021-Current, Sanhe Hu <husanhe@gmail.com> https://github.com/MacHu-GWU/cottonformation-project
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

Modern CloudFormation Python tool with Type hint, Parameter hint, Doc hint +
Auto Validation in Real Objective Programming Style
"""


from ._version import __version__

__short_description__ = (
    "Modern CloudFormation Python tool with Type hint, Parameter hint, "
    "Doc hint + Auto Validation in Real Objective Programming Style."
)
__license__ = "BSD License"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"
__fingerprint_of_license_file = "e5834e80c86c4898dd9f1462a2349cbf"


try:
    from .core import constant, helpers, exc
    from .core.constant import DeletionPolicy, UpdateReplacePolicy
    from .core.model import (
        # data model
        Parameter, Property, Resource, Output, Export,
        Rule, Mapping, Condition, Transform,
        ResourceGroup, Tag,

        # intrinsic function
        Ref, Base64, Cidr, FindInMap, GetAtt, GetAZs,
        ImportValue, Join, Select, Split, Sub,

        # pseudo parameter
        AWS_ACCOUNT_ID,
        AWS_NOTIFICATION_ARNS,
        AWS_NO_VALUE,
        AWS_PARTITION,
        AWS_REGION,
        AWS_STACK_ID,
        AWS_STACK_NAME,
        AWS_URL_SURFIX,
    )
    from .core.config import CtfConfig
    from .core.template import Template
    from .core.stack import Stack
    from .core.env import Env
except ImportError as e:
    pass
