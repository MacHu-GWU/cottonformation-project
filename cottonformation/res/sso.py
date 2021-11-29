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

@attr.s
class PropInstanceAccessControlAttributeConfigurationAccessControlAttributeValue(Property):
    """
    AWS Object Type = "AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html

    Property Document:
    
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source
    """
    AWS_OBJECT_TYPE = "AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributeValue"
    
    rp_Source: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source"""

@attr.s
class PropInstanceAccessControlAttributeConfigurationAccessControlAttribute(Property):
    """
    AWS Object Type = "AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value
    """
    AWS_OBJECT_TYPE = "AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttribute"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key"""
    rp_Value: typing.Union['PropInstanceAccessControlAttributeConfigurationAccessControlAttributeValue', dict] = attr.ib(
        default=None,
        converter=PropInstanceAccessControlAttributeConfigurationAccessControlAttributeValue.from_dict,
        validator=attr.validators.instance_of(PropInstanceAccessControlAttributeConfigurationAccessControlAttributeValue),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value"""


#--- Resource declaration ---

@attr.s
class Assignment(Resource):
    """
    AWS Object Type = "AWS::SSO::Assignment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html

    Property Document:
    
    - ``rp_InstanceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
    - ``rp_PermissionSetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
    - ``rp_PrincipalId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
    - ``rp_PrincipalType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
    - ``rp_TargetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
    - ``rp_TargetType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
    """
    AWS_OBJECT_TYPE = "AWS::SSO::Assignment"

    
    rp_InstanceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn"""
    rp_PermissionSetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PermissionSetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn"""
    rp_PrincipalId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrincipalId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid"""
    rp_PrincipalType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrincipalType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype"""
    rp_TargetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TargetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid"""
    rp_TargetType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TargetType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype"""

    

@attr.s
class InstanceAccessControlAttributeConfiguration(Resource):
    """
    AWS Object Type = "AWS::SSO::InstanceAccessControlAttributeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html

    Property Document:
    
    - ``rp_InstanceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
    - ``p_AccessControlAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
    """
    AWS_OBJECT_TYPE = "AWS::SSO::InstanceAccessControlAttributeConfiguration"

    
    rp_InstanceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn"""
    p_AccessControlAttributes: typing.List[typing.Union['PropInstanceAccessControlAttributeConfigurationAccessControlAttribute', dict]] = attr.ib(
        default=None,
        converter=PropInstanceAccessControlAttributeConfigurationAccessControlAttribute.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInstanceAccessControlAttributeConfigurationAccessControlAttribute), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AccessControlAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes"""

    

@attr.s
class PermissionSet(Resource):
    """
    AWS Object Type = "AWS::SSO::PermissionSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html

    Property Document:
    
    - ``rp_InstanceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
    - ``p_InlinePolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
    - ``p_ManagedPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
    - ``p_RelayStateType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
    - ``p_SessionDuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
    """
    AWS_OBJECT_TYPE = "AWS::SSO::PermissionSet"

    
    rp_InstanceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description"""
    p_InlinePolicy: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "InlinePolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy"""
    p_ManagedPolicies: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ManagedPolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies"""
    p_RelayStateType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RelayStateType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype"""
    p_SessionDuration: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SessionDuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags"""

    
    @property
    def rv_PermissionSetArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#aws-resource-sso-permissionset-return-values"""
        return GetAtt(resource=self, attr_name="PermissionSetArn")
    
