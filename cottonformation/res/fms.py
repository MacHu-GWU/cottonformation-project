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
class PropPolicyPolicyTag(Property):
    """
    AWS Object Type = "AWS::FMS::Policy.PolicyTag"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value
    """
    AWS_OBJECT_TYPE = "AWS::FMS::Policy.PolicyTag"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value"""

@attr.s
class PropPolicyResourceTag(Property):
    """
    AWS Object Type = "AWS::FMS::Policy.ResourceTag"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value
    """
    AWS_OBJECT_TYPE = "AWS::FMS::Policy.ResourceTag"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value"""

@attr.s
class PropPolicyIEMap(Property):
    """
    AWS Object Type = "AWS::FMS::Policy.IEMap"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html

    Property Document:
    
    - ``p_ACCOUNT``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
    - ``p_ORGUNIT``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit
    """
    AWS_OBJECT_TYPE = "AWS::FMS::Policy.IEMap"
    
    p_ACCOUNT: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ACCOUNT"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account"""
    p_ORGUNIT: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ORGUNIT"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit"""


#--- Resource declaration ---

@attr.s
class NotificationChannel(Resource):
    """
    AWS Object Type = "AWS::FMS::NotificationChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html

    Property Document:
    
    - ``rp_SnsRoleName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
    - ``rp_SnsTopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
    """
    AWS_OBJECT_TYPE = "AWS::FMS::NotificationChannel"

    
    rp_SnsRoleName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SnsRoleName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename"""
    rp_SnsTopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SnsTopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn"""

    

@attr.s
class Policy(Resource):
    """
    AWS Object Type = "AWS::FMS::Policy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html

    Property Document:
    
    - ``rp_ExcludeResourceTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
    - ``rp_PolicyName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
    - ``rp_RemediationEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
    - ``rp_ResourceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
    - ``rp_SecurityServicePolicyData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
    - ``p_DeleteAllPolicyResources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
    - ``p_ExcludeMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
    - ``p_IncludeMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
    - ``p_ResourceTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
    - ``p_ResourceTypeList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
    - ``p_ResourcesCleanUp``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
    """
    AWS_OBJECT_TYPE = "AWS::FMS::Policy"

    
    rp_ExcludeResourceTags: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeResourceTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags"""
    rp_PolicyName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PolicyName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname"""
    rp_RemediationEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "RemediationEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled"""
    rp_ResourceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype"""
    rp_SecurityServicePolicyData: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityServicePolicyData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata"""
    p_DeleteAllPolicyResources: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteAllPolicyResources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources"""
    p_ExcludeMap: typing.Union['PropPolicyIEMap', dict] = attr.ib(
        default=None,
        converter=PropPolicyIEMap.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPolicyIEMap)),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap"""
    p_IncludeMap: typing.Union['PropPolicyIEMap', dict] = attr.ib(
        default=None,
        converter=PropPolicyIEMap.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPolicyIEMap)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap"""
    p_ResourceTags: typing.List[typing.Union['PropPolicyResourceTag', dict]] = attr.ib(
        default=None,
        converter=PropPolicyResourceTag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPolicyResourceTag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags"""
    p_ResourceTypeList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceTypeList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist"""
    p_ResourcesCleanUp: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourcesCleanUp"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup"""
    p_Tags: typing.List[typing.Union['PropPolicyPolicyTag', dict]] = attr.ib(
        default=None,
        converter=PropPolicyPolicyTag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropPolicyPolicyTag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#aws-resource-fms-policy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#aws-resource-fms-policy-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
