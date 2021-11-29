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
class PropProjectGitSubmodulesConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.GitSubmodulesConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html

    Property Document:
    
    - ``rp_FetchSubmodules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html#cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.GitSubmodulesConfig"
    
    rp_FetchSubmodules: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "FetchSubmodules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-gitsubmodulesconfig.html#cfn-codebuild-project-gitsubmodulesconfig-fetchsubmodules"""

@attr.s
class PropProjectVpcConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.VpcConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html

    Property Document:
    
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-securitygroupids
    - ``p_Subnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-subnets
    - ``p_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-vpcid
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.VpcConfig"
    
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-securitygroupids"""
    p_Subnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Subnets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-subnets"""
    p_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-vpcconfig.html#cfn-codebuild-project-vpcconfig-vpcid"""

@attr.s
class PropProjectArtifacts(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.Artifacts"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-type
    - ``p_ArtifactIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-artifactidentifier
    - ``p_EncryptionDisabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-encryptiondisabled
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-location
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-name
    - ``p_NamespaceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-namespacetype
    - ``p_OverrideArtifactName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-overrideartifactname
    - ``p_Packaging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-packaging
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-path
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.Artifacts"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-type"""
    p_ArtifactIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ArtifactIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-artifactidentifier"""
    p_EncryptionDisabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionDisabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-encryptiondisabled"""
    p_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-location"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-name"""
    p_NamespaceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "NamespaceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-namespacetype"""
    p_OverrideArtifactName: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "OverrideArtifactName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-overrideartifactname"""
    p_Packaging: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Packaging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-packaging"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html#cfn-codebuild-project-artifacts-path"""

@attr.s
class PropProjectRegistryCredential(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.RegistryCredential"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html

    Property Document:
    
    - ``rp_Credential``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credential
    - ``rp_CredentialProvider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credentialprovider
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.RegistryCredential"
    
    rp_Credential: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Credential"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credential"""
    rp_CredentialProvider: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CredentialProvider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-registrycredential.html#cfn-codebuild-project-registrycredential-credentialprovider"""

@attr.s
class PropReportGroupS3ReportExportConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::ReportGroup.S3ReportExportConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html

    Property Document:
    
    - ``rp_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucket
    - ``p_BucketOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucketowner
    - ``p_EncryptionDisabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptiondisabled
    - ``p_EncryptionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptionkey
    - ``p_Packaging``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-packaging
    - ``p_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-path
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::ReportGroup.S3ReportExportConfig"
    
    rp_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucket"""
    p_BucketOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BucketOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-bucketowner"""
    p_EncryptionDisabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionDisabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptiondisabled"""
    p_EncryptionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-encryptionkey"""
    p_Packaging: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Packaging"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-packaging"""
    p_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-s3reportexportconfig.html#cfn-codebuild-reportgroup-s3reportexportconfig-path"""

@attr.s
class PropProjectCloudWatchLogsConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.CloudWatchLogsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html

    Property Document:
    
    - ``rp_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-status
    - ``p_GroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-groupname
    - ``p_StreamName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-streamname
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.CloudWatchLogsConfig"
    
    rp_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-status"""
    p_GroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-groupname"""
    p_StreamName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-cloudwatchlogsconfig.html#cfn-codebuild-project-cloudwatchlogsconfig-streamname"""

@attr.s
class PropProjectProjectCache(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.ProjectCache"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-type
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-location
    - ``p_Modes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-modes
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.ProjectCache"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-type"""
    p_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-location"""
    p_Modes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Modes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectcache.html#cfn-codebuild-project-projectcache-modes"""

@attr.s
class PropProjectFilterGroup(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.FilterGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-filtergroup.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.FilterGroup"
    

@attr.s
class PropProjectBatchRestrictions(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.BatchRestrictions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html

    Property Document:
    
    - ``p_ComputeTypesAllowed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-computetypesallowed
    - ``p_MaximumBuildsAllowed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-maximumbuildsallowed
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.BatchRestrictions"
    
    p_ComputeTypesAllowed: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ComputeTypesAllowed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-computetypesallowed"""
    p_MaximumBuildsAllowed: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaximumBuildsAllowed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-batchrestrictions.html#cfn-codebuild-project-batchrestrictions-maximumbuildsallowed"""

@attr.s
class PropProjectProjectTriggers(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.ProjectTriggers"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html

    Property Document:
    
    - ``p_BuildType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-buildtype
    - ``p_FilterGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-filtergroups
    - ``p_Webhook``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-webhook
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.ProjectTriggers"
    
    p_BuildType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-buildtype"""
    p_FilterGroups: typing.List[typing.Union['PropProjectFilterGroup', dict]] = attr.ib(
        default=None,
        converter=PropProjectFilterGroup.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectFilterGroup), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FilterGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-filtergroups"""
    p_Webhook: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Webhook"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projecttriggers.html#cfn-codebuild-project-projecttriggers-webhook"""

@attr.s
class PropProjectProjectSourceVersion(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.ProjectSourceVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html

    Property Document:
    
    - ``rp_SourceIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceidentifier
    - ``p_SourceVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceversion
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.ProjectSourceVersion"
    
    rp_SourceIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceidentifier"""
    p_SourceVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectsourceversion.html#cfn-codebuild-project-projectsourceversion-sourceversion"""

@attr.s
class PropProjectSourceAuth(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.SourceAuth"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-type
    - ``p_Resource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-resource
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.SourceAuth"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-type"""
    p_Resource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Resource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-sourceauth.html#cfn-codebuild-project-sourceauth-resource"""

@attr.s
class PropProjectProjectFileSystemLocation(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.ProjectFileSystemLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html

    Property Document:
    
    - ``rp_Identifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-identifier
    - ``rp_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-location
    - ``rp_MountPoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountpoint
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-type
    - ``p_MountOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountoptions
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.ProjectFileSystemLocation"
    
    rp_Identifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Identifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-identifier"""
    rp_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-location"""
    rp_MountPoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MountPoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountpoint"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-type"""
    p_MountOptions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MountOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectfilesystemlocation.html#cfn-codebuild-project-projectfilesystemlocation-mountoptions"""

@attr.s
class PropProjectS3LogsConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.S3LogsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html

    Property Document:
    
    - ``rp_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-status
    - ``p_EncryptionDisabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-encryptiondisabled
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-location
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.S3LogsConfig"
    
    rp_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-status"""
    p_EncryptionDisabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionDisabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-encryptiondisabled"""
    p_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-s3logsconfig.html#cfn-codebuild-project-s3logsconfig-location"""

@attr.s
class PropProjectWebhookFilter(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.WebhookFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html

    Property Document:
    
    - ``rp_Pattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-pattern
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-type
    - ``p_ExcludeMatchedPattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-excludematchedpattern
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.WebhookFilter"
    
    rp_Pattern: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Pattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-pattern"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-type"""
    p_ExcludeMatchedPattern: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ExcludeMatchedPattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-webhookfilter.html#cfn-codebuild-project-webhookfilter-excludematchedpattern"""

@attr.s
class PropProjectBuildStatusConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.BuildStatusConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html

    Property Document:
    
    - ``p_Context``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-context
    - ``p_TargetUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-targeturl
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.BuildStatusConfig"
    
    p_Context: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Context"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-context"""
    p_TargetUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-buildstatusconfig.html#cfn-codebuild-project-buildstatusconfig-targeturl"""

@attr.s
class PropProjectEnvironmentVariable(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.EnvironmentVariable"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-name
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-value
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-type
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.EnvironmentVariable"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-name"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-value"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environmentvariable.html#cfn-codebuild-project-environmentvariable-type"""

@attr.s
class PropProjectEnvironment(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html

    Property Document:
    
    - ``rp_ComputeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-computetype
    - ``rp_Image``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-image
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-type
    - ``p_Certificate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-certificate
    - ``p_EnvironmentVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-environmentvariables
    - ``p_ImagePullCredentialsType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-imagepullcredentialstype
    - ``p_PrivilegedMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-privilegedmode
    - ``p_RegistryCredential``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-registrycredential
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.Environment"
    
    rp_ComputeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComputeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-computetype"""
    rp_Image: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Image"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-image"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-type"""
    p_Certificate: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Certificate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-certificate"""
    p_EnvironmentVariables: typing.List[typing.Union['PropProjectEnvironmentVariable', dict]] = attr.ib(
        default=None,
        converter=PropProjectEnvironmentVariable.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectEnvironmentVariable), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-environmentvariables"""
    p_ImagePullCredentialsType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ImagePullCredentialsType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-imagepullcredentialstype"""
    p_PrivilegedMode: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PrivilegedMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-privilegedmode"""
    p_RegistryCredential: typing.Union['PropProjectRegistryCredential', dict] = attr.ib(
        default=None,
        converter=PropProjectRegistryCredential.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectRegistryCredential)),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryCredential"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-environment.html#cfn-codebuild-project-environment-registrycredential"""

@attr.s
class PropReportGroupReportExportConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::ReportGroup.ReportExportConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html

    Property Document:
    
    - ``rp_ExportConfigType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype
    - ``p_S3Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-s3destination
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::ReportGroup.ReportExportConfig"
    
    rp_ExportConfigType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ExportConfigType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-exportconfigtype"""
    p_S3Destination: typing.Union['PropReportGroupS3ReportExportConfig', dict] = attr.ib(
        default=None,
        converter=PropReportGroupS3ReportExportConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReportGroupS3ReportExportConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-reportgroup-reportexportconfig.html#cfn-codebuild-reportgroup-reportexportconfig-s3destination"""

@attr.s
class PropProjectProjectBuildBatchConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.ProjectBuildBatchConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html

    Property Document:
    
    - ``p_BatchReportMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-batchreportmode
    - ``p_CombineArtifacts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-combineartifacts
    - ``p_Restrictions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-restrictions
    - ``p_ServiceRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-servicerole
    - ``p_TimeoutInMins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-timeoutinmins
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.ProjectBuildBatchConfig"
    
    p_BatchReportMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BatchReportMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-batchreportmode"""
    p_CombineArtifacts: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CombineArtifacts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-combineartifacts"""
    p_Restrictions: typing.Union['PropProjectBatchRestrictions', dict] = attr.ib(
        default=None,
        converter=PropProjectBatchRestrictions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectBatchRestrictions)),
        metadata={AttrMeta.PROPERTY_NAME: "Restrictions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-restrictions"""
    p_ServiceRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-servicerole"""
    p_TimeoutInMins: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInMins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-projectbuildbatchconfig.html#cfn-codebuild-project-projectbuildbatchconfig-timeoutinmins"""

@attr.s
class PropProjectSource(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.Source"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-type
    - ``p_Auth``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-auth
    - ``p_BuildSpec``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildspec
    - ``p_BuildStatusConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildstatusconfig
    - ``p_GitCloneDepth``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitclonedepth
    - ``p_GitSubmodulesConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitsubmodulesconfig
    - ``p_InsecureSsl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-insecuressl
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-location
    - ``p_ReportBuildStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-reportbuildstatus
    - ``p_SourceIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-sourceidentifier
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.Source"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-type"""
    p_Auth: typing.Union['PropProjectSourceAuth', dict] = attr.ib(
        default=None,
        converter=PropProjectSourceAuth.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectSourceAuth)),
        metadata={AttrMeta.PROPERTY_NAME: "Auth"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-auth"""
    p_BuildSpec: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildSpec"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildspec"""
    p_BuildStatusConfig: typing.Union['PropProjectBuildStatusConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectBuildStatusConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectBuildStatusConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildStatusConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-buildstatusconfig"""
    p_GitCloneDepth: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "GitCloneDepth"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitclonedepth"""
    p_GitSubmodulesConfig: typing.Union['PropProjectGitSubmodulesConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectGitSubmodulesConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectGitSubmodulesConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "GitSubmodulesConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-gitsubmodulesconfig"""
    p_InsecureSsl: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InsecureSsl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-insecuressl"""
    p_Location: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-location"""
    p_ReportBuildStatus: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportBuildStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-reportbuildstatus"""
    p_SourceIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-source.html#cfn-codebuild-project-source-sourceidentifier"""

@attr.s
class PropProjectLogsConfig(Property):
    """
    AWS Object Type = "AWS::CodeBuild::Project.LogsConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html

    Property Document:
    
    - ``p_CloudWatchLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-cloudwatchlogs
    - ``p_S3Logs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-s3logs
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project.LogsConfig"
    
    p_CloudWatchLogs: typing.Union['PropProjectCloudWatchLogsConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectCloudWatchLogsConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectCloudWatchLogsConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-cloudwatchlogs"""
    p_S3Logs: typing.Union['PropProjectS3LogsConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectS3LogsConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectS3LogsConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Logs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-logsconfig.html#cfn-codebuild-project-logsconfig-s3logs"""


#--- Resource declaration ---

@attr.s
class SourceCredential(Resource):
    """
    AWS Object Type = "AWS::CodeBuild::SourceCredential"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html

    Property Document:
    
    - ``rp_AuthType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-authtype
    - ``rp_ServerType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-servertype
    - ``rp_Token``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-token
    - ``p_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-username
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::SourceCredential"

    
    rp_AuthType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AuthType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-authtype"""
    rp_ServerType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServerType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-servertype"""
    rp_Token: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Token"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-token"""
    p_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html#cfn-codebuild-sourcecredential-username"""

    

@attr.s
class ReportGroup(Resource):
    """
    AWS Object Type = "AWS::CodeBuild::ReportGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html

    Property Document:
    
    - ``rp_ExportConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-exportconfig
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-type
    - ``p_DeleteReports``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-deletereports
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::ReportGroup"

    
    rp_ExportConfig: typing.Union['PropReportGroupReportExportConfig', dict] = attr.ib(
        default=None,
        converter=PropReportGroupReportExportConfig.from_dict,
        validator=attr.validators.instance_of(PropReportGroupReportExportConfig),
        metadata={AttrMeta.PROPERTY_NAME: "ExportConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-exportconfig"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-type"""
    p_DeleteReports: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteReports"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-deletereports"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#cfn-codebuild-reportgroup-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html#aws-resource-codebuild-reportgroup-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Project(Resource):
    """
    AWS Object Type = "AWS::CodeBuild::Project"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html

    Property Document:
    
    - ``rp_Artifacts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-artifacts
    - ``rp_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-environment
    - ``rp_ServiceRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-servicerole
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-source
    - ``p_BadgeEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-badgeenabled
    - ``p_BuildBatchConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-buildbatchconfig
    - ``p_Cache``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-cache
    - ``p_ConcurrentBuildLimit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-concurrentbuildlimit
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-description
    - ``p_EncryptionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-encryptionkey
    - ``p_FileSystemLocations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-filesystemlocations
    - ``p_LogsConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-logsconfig
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-name
    - ``p_QueuedTimeoutInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-queuedtimeoutinminutes
    - ``p_ResourceAccessRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-resourceaccessrole
    - ``p_SecondaryArtifacts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondaryartifacts
    - ``p_SecondarySourceVersions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysourceversions
    - ``p_SecondarySources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysources
    - ``p_SourceVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-sourceversion
    - ``p_TimeoutInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-timeoutinminutes
    - ``p_Triggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-triggers
    - ``p_Visibility``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-visibility
    - ``p_VpcConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-vpcconfig
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-tags
    """
    AWS_OBJECT_TYPE = "AWS::CodeBuild::Project"

    
    rp_Artifacts: typing.Union['PropProjectArtifacts', dict] = attr.ib(
        default=None,
        converter=PropProjectArtifacts.from_dict,
        validator=attr.validators.instance_of(PropProjectArtifacts),
        metadata={AttrMeta.PROPERTY_NAME: "Artifacts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-artifacts"""
    rp_Environment: typing.Union['PropProjectEnvironment', dict] = attr.ib(
        default=None,
        converter=PropProjectEnvironment.from_dict,
        validator=attr.validators.instance_of(PropProjectEnvironment),
        metadata={AttrMeta.PROPERTY_NAME: "Environment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-environment"""
    rp_ServiceRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-servicerole"""
    rp_Source: typing.Union['PropProjectSource', dict] = attr.ib(
        default=None,
        converter=PropProjectSource.from_dict,
        validator=attr.validators.instance_of(PropProjectSource),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-source"""
    p_BadgeEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "BadgeEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-badgeenabled"""
    p_BuildBatchConfig: typing.Union['PropProjectProjectBuildBatchConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectProjectBuildBatchConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectProjectBuildBatchConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "BuildBatchConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-buildbatchconfig"""
    p_Cache: typing.Union['PropProjectProjectCache', dict] = attr.ib(
        default=None,
        converter=PropProjectProjectCache.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectProjectCache)),
        metadata={AttrMeta.PROPERTY_NAME: "Cache"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-cache"""
    p_ConcurrentBuildLimit: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ConcurrentBuildLimit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-concurrentbuildlimit"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-description"""
    p_EncryptionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-encryptionkey"""
    p_FileSystemLocations: typing.List[typing.Union['PropProjectProjectFileSystemLocation', dict]] = attr.ib(
        default=None,
        converter=PropProjectProjectFileSystemLocation.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectProjectFileSystemLocation), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FileSystemLocations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-filesystemlocations"""
    p_LogsConfig: typing.Union['PropProjectLogsConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectLogsConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectLogsConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "LogsConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-logsconfig"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-name"""
    p_QueuedTimeoutInMinutes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "QueuedTimeoutInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-queuedtimeoutinminutes"""
    p_ResourceAccessRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceAccessRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-resourceaccessrole"""
    p_SecondaryArtifacts: typing.List[typing.Union['PropProjectArtifacts', dict]] = attr.ib(
        default=None,
        converter=PropProjectArtifacts.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectArtifacts), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecondaryArtifacts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondaryartifacts"""
    p_SecondarySourceVersions: typing.List[typing.Union['PropProjectProjectSourceVersion', dict]] = attr.ib(
        default=None,
        converter=PropProjectProjectSourceVersion.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectProjectSourceVersion), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecondarySourceVersions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysourceversions"""
    p_SecondarySources: typing.List[typing.Union['PropProjectSource', dict]] = attr.ib(
        default=None,
        converter=PropProjectSource.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropProjectSource), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecondarySources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-secondarysources"""
    p_SourceVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-sourceversion"""
    p_TimeoutInMinutes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TimeoutInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-timeoutinminutes"""
    p_Triggers: typing.Union['PropProjectProjectTriggers', dict] = attr.ib(
        default=None,
        converter=PropProjectProjectTriggers.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectProjectTriggers)),
        metadata={AttrMeta.PROPERTY_NAME: "Triggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-triggers"""
    p_Visibility: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Visibility"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-visibility"""
    p_VpcConfig: typing.Union['PropProjectVpcConfig', dict] = attr.ib(
        default=None,
        converter=PropProjectVpcConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropProjectVpcConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-vpcconfig"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#cfn-codebuild-project-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html#aws-resource-codebuild-project-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
