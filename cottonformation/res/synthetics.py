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
class PropCanaryS3Encryption(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.S3Encryption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html

    Property Document:
    
    - ``p_EncryptionMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-encryptionmode
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-kmskeyarn
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.S3Encryption"
    
    p_EncryptionMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-encryptionmode"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html#cfn-synthetics-canary-s3encryption-kmskeyarn"""

@attr.s
class PropCanaryVPCConfig(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.VPCConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html

    Property Document:
    
    - ``rp_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-securitygroupids
    - ``rp_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-subnetids
    - ``p_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-vpcid
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.VPCConfig"
    
    rp_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-securitygroupids"""
    rp_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-subnetids"""
    p_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html#cfn-synthetics-canary-vpcconfig-vpcid"""

@attr.s
class PropCanarySchedule(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.Schedule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html

    Property Document:
    
    - ``rp_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-expression
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.Schedule"
    
    rp_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-expression"""
    p_DurationInSeconds: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html#cfn-synthetics-canary-schedule-durationinseconds"""

@attr.s
class PropCanaryCode(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.Code"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html

    Property Document:
    
    - ``rp_Handler``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-handler
    - ``p_S3Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3bucket
    - ``p_S3Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3key
    - ``p_S3ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3objectversion
    - ``p_Script``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-script
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.Code"
    
    rp_Handler: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Handler"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-handler"""
    p_S3Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3bucket"""
    p_S3Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3key"""
    p_S3ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-s3objectversion"""
    p_Script: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Script"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html#cfn-synthetics-canary-code-script"""

@attr.s
class PropCanaryBaseScreenshot(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.BaseScreenshot"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html

    Property Document:
    
    - ``rp_ScreenshotName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-screenshotname
    - ``p_IgnoreCoordinates``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-ignorecoordinates
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.BaseScreenshot"
    
    rp_ScreenshotName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ScreenshotName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-screenshotname"""
    p_IgnoreCoordinates: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "IgnoreCoordinates"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html#cfn-synthetics-canary-basescreenshot-ignorecoordinates"""

@attr.s
class PropCanaryRunConfig(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.RunConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html

    Property Document:
    
    - ``p_ActiveTracing``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-activetracing
    - ``p_EnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-environmentvariables
    - ``p_MemoryInMB``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-memoryinmb
    - ``p_TimeoutInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-timeoutinseconds
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.RunConfig"
    
    p_ActiveTracing: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ActiveTracing"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-activetracing"""
    p_EnvironmentVariables: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-environmentvariables"""
    p_MemoryInMB: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MemoryInMB"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-memoryinmb"""
    p_TimeoutInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html#cfn-synthetics-canary-runconfig-timeoutinseconds"""

@attr.s
class PropCanaryArtifactConfig(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.ArtifactConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html

    Property Document:
    
    - ``p_S3Encryption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html#cfn-synthetics-canary-artifactconfig-s3encryption
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.ArtifactConfig"
    
    p_S3Encryption: typing.Union['PropCanaryS3Encryption', dict] = attr.ib(
        default=None,
        converter=PropCanaryS3Encryption.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCanaryS3Encryption)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Encryption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html#cfn-synthetics-canary-artifactconfig-s3encryption"""

@attr.s
class PropCanaryVisualReference(Property):
    """
    AWS Object Type = "AWS::Synthetics::Canary.VisualReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html

    Property Document:
    
    - ``rp_BaseCanaryRunId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basecanaryrunid
    - ``p_BaseScreenshots``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basescreenshots
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary.VisualReference"
    
    rp_BaseCanaryRunId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BaseCanaryRunId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basecanaryrunid"""
    p_BaseScreenshots: typing.List[typing.Union['PropCanaryBaseScreenshot', dict]] = attr.ib(
        default=None,
        converter=PropCanaryBaseScreenshot.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCanaryBaseScreenshot), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BaseScreenshots"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html#cfn-synthetics-canary-visualreference-basescreenshots"""


#--- Resource declaration ---

@attr.s
class Canary(Resource):
    """
    AWS Object Type = "AWS::Synthetics::Canary"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html

    Property Document:
    
    - ``rp_ArtifactS3Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location
    - ``rp_Code``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code
    - ``rp_ExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name
    - ``rp_RuntimeVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion
    - ``rp_Schedule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule
    - ``rp_StartCanaryAfterCreation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation
    - ``p_ArtifactConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifactconfig
    - ``p_FailureRetentionPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod
    - ``p_RunConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig
    - ``p_SuccessRetentionPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod
    - ``p_VPCConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig
    - ``p_VisualReference``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-visualreference
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags
    """
    AWS_OBJECT_TYPE = "AWS::Synthetics::Canary"

    
    rp_ArtifactS3Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ArtifactS3Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location"""
    rp_Code: typing.Union['PropCanaryCode', dict] = attr.ib(
        default=None,
        converter=PropCanaryCode.from_dict,
        validator=attr.validators.instance_of(PropCanaryCode),
        metadata={AttrMeta.PROPERTY_NAME: "Code"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code"""
    rp_ExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name"""
    rp_RuntimeVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimeVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion"""
    rp_Schedule: typing.Union['PropCanarySchedule', dict] = attr.ib(
        default=None,
        converter=PropCanarySchedule.from_dict,
        validator=attr.validators.instance_of(PropCanarySchedule),
        metadata={AttrMeta.PROPERTY_NAME: "Schedule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule"""
    rp_StartCanaryAfterCreation: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "StartCanaryAfterCreation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation"""
    p_ArtifactConfig: typing.Union['PropCanaryArtifactConfig', dict] = attr.ib(
        default=None,
        converter=PropCanaryArtifactConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCanaryArtifactConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ArtifactConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifactconfig"""
    p_FailureRetentionPeriod: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "FailureRetentionPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod"""
    p_RunConfig: typing.Union['PropCanaryRunConfig', dict] = attr.ib(
        default=None,
        converter=PropCanaryRunConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCanaryRunConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "RunConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig"""
    p_SuccessRetentionPeriod: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SuccessRetentionPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod"""
    p_VPCConfig: typing.Union['PropCanaryVPCConfig', dict] = attr.ib(
        default=None,
        converter=PropCanaryVPCConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCanaryVPCConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "VPCConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig"""
    p_VisualReference: typing.Union['PropCanaryVisualReference', dict] = attr.ib(
        default=None,
        converter=PropCanaryVisualReference.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCanaryVisualReference)),
        metadata={AttrMeta.PROPERTY_NAME: "VisualReference"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-visualreference"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#aws-resource-synthetics-canary-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_State(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#aws-resource-synthetics-canary-return-values"""
        return GetAtt(resource=self, attr_name="State")
    
