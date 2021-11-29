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
class Workspace(Resource):
    """
    AWS Object Type = "AWS::APS::Workspace"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html

    Property Document:
    
    - ``p_AlertManagerDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition
    - ``p_Alias``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags
    """
    AWS_OBJECT_TYPE = "AWS::APS::Workspace"

    
    p_AlertManagerDefinition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AlertManagerDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition"""
    p_Alias: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Alias"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags"""

    
    @property
    def rv_WorkspaceId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#aws-resource-aps-workspace-return-values"""
        return GetAtt(resource=self, attr_name="WorkspaceId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#aws-resource-aps-workspace-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_PrometheusEndpoint(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#aws-resource-aps-workspace-return-values"""
        return GetAtt(resource=self, attr_name="PrometheusEndpoint")
    

@attr.s
class RuleGroupsNamespace(Resource):
    """
    AWS Object Type = "AWS::APS::RuleGroupsNamespace"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html

    Property Document:
    
    - ``rp_Data``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name
    - ``rp_Workspace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags
    """
    AWS_OBJECT_TYPE = "AWS::APS::RuleGroupsNamespace"

    
    rp_Data: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Data"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name"""
    rp_Workspace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Workspace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#aws-resource-aps-rulegroupsnamespace-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
