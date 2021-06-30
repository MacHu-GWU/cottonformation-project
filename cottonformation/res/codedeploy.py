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
class PropDeploymentGroupTargetGroupInfo(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.TargetGroupInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html#cfn-codedeploy-deploymentgroup-targetgroupinfo-name
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.TargetGroupInfo"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html#cfn-codedeploy-deploymentgroup-targetgroupinfo-name"""

@attr.s
class PropDeploymentGroupDeploymentStyle(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.DeploymentStyle"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html

    Property Document:
    
    - ``p_DeploymentOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption
    - ``p_DeploymentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.DeploymentStyle"
    
    p_DeploymentOption: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption"""
    p_DeploymentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype"""

@attr.s
class PropDeploymentGroupEC2TagFilter(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.EC2TagFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.EC2TagFilter"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value"""

@attr.s
class PropDeploymentGroupTriggerConfig(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.TriggerConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html

    Property Document:
    
    - ``p_TriggerEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggerevents
    - ``p_TriggerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggername
    - ``p_TriggerTargetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggertargetarn
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.TriggerConfig"
    
    p_TriggerEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggerevents"""
    p_TriggerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggername"""
    p_TriggerTargetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerTargetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggertargetarn"""

@attr.s
class PropDeploymentConfigMinimumHealthyHosts(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type"""
    rp_Value: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value"""

@attr.s
class PropDeploymentGroupAutoRollbackConfiguration(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.AutoRollbackConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-enabled
    - ``p_Events``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-events
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.AutoRollbackConfiguration"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-enabled"""
    p_Events: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Events"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-events"""

@attr.s
class PropDeploymentGroupS3Location(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.S3Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bucket
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-key
    - ``p_BundleType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bundletype
    - ``p_ETag``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-etag
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-value
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.S3Location"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bucket"""
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-key"""
    p_BundleType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BundleType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bundletype"""
    p_ETag: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ETag"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-etag"""
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-value"""

@attr.s
class PropDeploymentGroupTagFilter(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.TagFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html

    Property Document:
    
    - ``p_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-key
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-type
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-value
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.TagFilter"
    
    p_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-key"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-type"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-value"""

@attr.s
class PropDeploymentGroupGitHubLocation(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.GitHubLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html

    Property Document:
    
    - ``rp_CommitId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-commitid
    - ``rp_Repository``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-repository
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.GitHubLocation"
    
    rp_CommitId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CommitId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-commitid"""
    rp_Repository: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Repository"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-repository"""

@attr.s
class PropDeploymentGroupELBInfo(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.ELBInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html#cfn-codedeploy-deploymentgroup-elbinfo-name
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.ELBInfo"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html#cfn-codedeploy-deploymentgroup-elbinfo-name"""

@attr.s
class PropDeploymentGroupAlarm(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.Alarm"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html#cfn-codedeploy-deploymentgroup-alarm-name
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.Alarm"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html#cfn-codedeploy-deploymentgroup-alarm-name"""

@attr.s
class PropDeploymentGroupEC2TagSetListObject(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.EC2TagSetListObject"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html

    Property Document:
    
    - ``p_Ec2TagGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html#cfn-codedeploy-deploymentgroup-ec2tagsetlistobject-ec2taggroup
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.EC2TagSetListObject"
    
    p_Ec2TagGroup: typing.List[typing.Union['PropDeploymentGroupEC2TagFilter', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupEC2TagFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupEC2TagFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2TagGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html#cfn-codedeploy-deploymentgroup-ec2tagsetlistobject-ec2taggroup"""

@attr.s
class PropDeploymentGroupOnPremisesTagSetListObject(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSetListObject"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html

    Property Document:
    
    - ``p_OnPremisesTagGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSetListObject"
    
    p_OnPremisesTagGroup: typing.List[typing.Union['PropDeploymentGroupTagFilter', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupTagFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupTagFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OnPremisesTagGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup"""

@attr.s
class PropDeploymentGroupOnPremisesTagSet(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html

    Property Document:
    
    - ``p_OnPremisesTagSetList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html#cfn-codedeploy-deploymentgroup-onpremisestagset-onpremisestagsetlist
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSet"
    
    p_OnPremisesTagSetList: typing.List[typing.Union['PropDeploymentGroupOnPremisesTagSetListObject', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupOnPremisesTagSetListObject.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupOnPremisesTagSetListObject), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OnPremisesTagSetList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html#cfn-codedeploy-deploymentgroup-onpremisestagset-onpremisestagsetlist"""

@attr.s
class PropDeploymentGroupLoadBalancerInfo(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html

    Property Document:
    
    - ``p_ElbInfoList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist
    - ``p_TargetGroupInfoList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo"
    
    p_ElbInfoList: typing.List[typing.Union['PropDeploymentGroupELBInfo', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupELBInfo.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupELBInfo), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ElbInfoList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist"""
    p_TargetGroupInfoList: typing.List[typing.Union['PropDeploymentGroupTargetGroupInfo', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupTargetGroupInfo.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupTargetGroupInfo), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TargetGroupInfoList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist"""

@attr.s
class PropDeploymentGroupRevisionLocation(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.RevisionLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html

    Property Document:
    
    - ``p_GitHubLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation
    - ``p_RevisionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-revisiontype
    - ``p_S3Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.RevisionLocation"
    
    p_GitHubLocation: typing.Union['PropDeploymentGroupGitHubLocation', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupGitHubLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupGitHubLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "GitHubLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation"""
    p_RevisionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RevisionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-revisiontype"""
    p_S3Location: typing.Union['PropDeploymentGroupS3Location', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupS3Location.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupS3Location)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location"""

@attr.s
class PropDeploymentGroupEC2TagSet(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.EC2TagSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html

    Property Document:
    
    - ``p_Ec2TagSetList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.EC2TagSet"
    
    p_Ec2TagSetList: typing.List[typing.Union['PropDeploymentGroupEC2TagSetListObject', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupEC2TagSetListObject.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupEC2TagSetListObject), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2TagSetList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist"""

@attr.s
class PropDeploymentGroupAlarmConfiguration(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.AlarmConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html

    Property Document:
    
    - ``p_Alarms``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-alarms
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-enabled
    - ``p_IgnorePollAlarmFailure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-ignorepollalarmfailure
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.AlarmConfiguration"
    
    p_Alarms: typing.List[typing.Union['PropDeploymentGroupAlarm', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupAlarm.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupAlarm), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Alarms"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-alarms"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-enabled"""
    p_IgnorePollAlarmFailure: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IgnorePollAlarmFailure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-ignorepollalarmfailure"""

@attr.s
class PropDeploymentGroupDeployment(Property):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup.Deployment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html

    Property Document:
    
    - ``rp_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-description
    - ``p_IgnoreApplicationStopFailures``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-ignoreapplicationstopfailures
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup.Deployment"
    
    rp_Revision: typing.Union['PropDeploymentGroupRevisionLocation', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupRevisionLocation.from_dict,
        validator=attr.validators.instance_of(PropDeploymentGroupRevisionLocation),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-description"""
    p_IgnoreApplicationStopFailures: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IgnoreApplicationStopFailures"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-ignoreapplicationstopfailures"""


#--- Resource declaration ---

@attr.s
class DeploymentConfig(Resource):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html

    Property Document:
    
    - ``p_DeploymentConfigName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname
    - ``p_MinimumHealthyHosts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentConfig"

    
    p_DeploymentConfigName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentConfigName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname"""
    p_MinimumHealthyHosts: typing.Union['PropDeploymentConfigMinimumHealthyHosts', dict] = attr.ib(
        default=None,
        converter=PropDeploymentConfigMinimumHealthyHosts.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentConfigMinimumHealthyHosts)),
        metadata={AttrMeta.PROPERTY_NAME: "MinimumHealthyHosts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts"""

    

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::CodeDeploy::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html

    Property Document:
    
    - ``p_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname
    - ``p_ComputePlatform``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::Application"

    
    p_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname"""
    p_ComputePlatform: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComputePlatform"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform"""

    

@attr.s
class DeploymentGroup(Resource):
    """
    AWS Object Type = "AWS::CodeDeploy::DeploymentGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname
    - ``rp_ServiceRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn
    - ``p_AlarmConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration
    - ``p_AutoRollbackConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration
    - ``p_AutoScalingGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups
    - ``p_Deployment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment
    - ``p_DeploymentConfigName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname
    - ``p_DeploymentGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname
    - ``p_DeploymentStyle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle
    - ``p_Ec2TagFilters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters
    - ``p_Ec2TagSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset
    - ``p_LoadBalancerInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo
    - ``p_OnPremisesInstanceTagFilters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters
    - ``p_OnPremisesTagSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset
    - ``p_TriggerConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations
    """
    AWS_OBJECT_TYPE = "AWS::CodeDeploy::DeploymentGroup"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname"""
    rp_ServiceRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn"""
    p_AlarmConfiguration: typing.Union['PropDeploymentGroupAlarmConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupAlarmConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupAlarmConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration"""
    p_AutoRollbackConfiguration: typing.Union['PropDeploymentGroupAutoRollbackConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupAutoRollbackConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupAutoRollbackConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoRollbackConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration"""
    p_AutoScalingGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScalingGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups"""
    p_Deployment: typing.Union['PropDeploymentGroupDeployment', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupDeployment.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupDeployment)),
        metadata={AttrMeta.PROPERTY_NAME: "Deployment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment"""
    p_DeploymentConfigName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentConfigName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname"""
    p_DeploymentGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname"""
    p_DeploymentStyle: typing.Union['PropDeploymentGroupDeploymentStyle', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupDeploymentStyle.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupDeploymentStyle)),
        metadata={AttrMeta.PROPERTY_NAME: "DeploymentStyle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle"""
    p_Ec2TagFilters: typing.List[typing.Union['PropDeploymentGroupEC2TagFilter', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupEC2TagFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupEC2TagFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2TagFilters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters"""
    p_Ec2TagSet: typing.Union['PropDeploymentGroupEC2TagSet', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupEC2TagSet.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupEC2TagSet)),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2TagSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset"""
    p_LoadBalancerInfo: typing.Union['PropDeploymentGroupLoadBalancerInfo', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupLoadBalancerInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupLoadBalancerInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "LoadBalancerInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo"""
    p_OnPremisesInstanceTagFilters: typing.List[typing.Union['PropDeploymentGroupTagFilter', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupTagFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupTagFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "OnPremisesInstanceTagFilters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters"""
    p_OnPremisesTagSet: typing.Union['PropDeploymentGroupOnPremisesTagSet', dict] = attr.ib(
        default=None,
        converter=PropDeploymentGroupOnPremisesTagSet.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeploymentGroupOnPremisesTagSet)),
        metadata={AttrMeta.PROPERTY_NAME: "OnPremisesTagSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset"""
    p_TriggerConfigurations: typing.List[typing.Union['PropDeploymentGroupTriggerConfig', dict]] = attr.ib(
        default=None,
        converter=PropDeploymentGroupTriggerConfig.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeploymentGroupTriggerConfig), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations"""

    
