# -*- coding: utf-8 -*-

"""
This module
"""

import attr
import typing

from ..core.model import (
    Property, Resource, Tag, GetAtt, TypeHint, TypeCheck,
)
from ..core.constant import AttrMeta

#--- Property declaration ---


#--- Resource declaration ---

@attr.s
class Project(Resource):
    """
    AWS Object Type = "AWS::Rekognition::Project"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html

    Property Document:
    
    - ``rp_ProjectName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname
    """
    AWS_OBJECT_TYPE = "AWS::Rekognition::Project"

    
    rp_ProjectName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProjectName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#aws-resource-rekognition-project-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
