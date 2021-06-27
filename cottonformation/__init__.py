# -*- coding: utf-8 -*-

"""
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


from .core.model import (
    # data model
    Template,
    Parameter, Resource, Output, Export,
    Rule, Mapping, Condition, Transform,

    # intrinsic function
    Ref, Base64, Cidr, FindInMap, GetAtt, GetAZs,
    ImportValue, Join, Select, Split, Sub
)
from .core import constant, helpers
from .core.env import Env
