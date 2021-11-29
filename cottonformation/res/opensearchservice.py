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
class PropDomainZoneAwarenessConfig(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.ZoneAwarenessConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html

    Property Document:
    
    - ``p_AvailabilityZoneCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.ZoneAwarenessConfig"
    
    p_AvailabilityZoneCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZoneCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-zoneawarenessconfig.html#cfn-opensearchservice-domain-zoneawarenessconfig-availabilityzonecount"""

@attr.s
class PropDomainNodeToNodeEncryptionOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.NodeToNodeEncryptionOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions-enabled
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.NodeToNodeEncryptionOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-nodetonodeencryptionoptions.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions-enabled"""

@attr.s
class PropDomainSnapshotOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.SnapshotOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html

    Property Document:
    
    - ``p_AutomatedSnapshotStartHour``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.SnapshotOptions"
    
    p_AutomatedSnapshotStartHour: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AutomatedSnapshotStartHour"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-snapshotoptions.html#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour"""

@attr.s
class PropDomainEBSOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.EBSOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html

    Property Document:
    
    - ``p_EBSEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-ebsenabled
    - ``p_Iops``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-iops
    - ``p_VolumeSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumesize
    - ``p_VolumeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumetype
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.EBSOptions"
    
    p_EBSEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-ebsenabled"""
    p_Iops: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Iops"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-iops"""
    p_VolumeSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumesize"""
    p_VolumeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-ebsoptions.html#cfn-opensearchservice-domain-ebsoptions-volumetype"""

@attr.s
class PropDomainLogPublishingOption(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.LogPublishingOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html

    Property Document:
    
    - ``p_CloudWatchLogsLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-cloudwatchlogsloggrouparn
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-enabled
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.LogPublishingOption"
    
    p_CloudWatchLogsLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogsLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-cloudwatchlogsloggrouparn"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-logpublishingoption.html#cfn-opensearchservice-domain-logpublishingoption-enabled"""

@attr.s
class PropDomainEncryptionAtRestOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.EncryptionAtRestOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-enabled
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.EncryptionAtRestOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-enabled"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-encryptionatrestoptions.html#cfn-opensearchservice-domain-encryptionatrestoptions-kmskeyid"""

@attr.s
class PropDomainDomainEndpointOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.DomainEndpointOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html

    Property Document:
    
    - ``p_CustomEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpoint
    - ``p_CustomEndpointCertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn
    - ``p_CustomEndpointEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled
    - ``p_EnforceHTTPS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps
    - ``p_TLSSecurityPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.DomainEndpointOptions"
    
    p_CustomEndpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpoint"""
    p_CustomEndpointCertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpointCertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointcertificatearn"""
    p_CustomEndpointEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpointEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-customendpointenabled"""
    p_EnforceHTTPS: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnforceHTTPS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-enforcehttps"""
    p_TLSSecurityPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TLSSecurityPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-domainendpointoptions.html#cfn-opensearchservice-domain-domainendpointoptions-tlssecuritypolicy"""

@attr.s
class PropDomainCognitoOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.CognitoOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-enabled
    - ``p_IdentityPoolId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-identitypoolid
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-rolearn
    - ``p_UserPoolId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-userpoolid
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.CognitoOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-enabled"""
    p_IdentityPoolId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IdentityPoolId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-identitypoolid"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-rolearn"""
    p_UserPoolId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UserPoolId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-cognitooptions.html#cfn-opensearchservice-domain-cognitooptions-userpoolid"""

@attr.s
class PropDomainVPCOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.VPCOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html

    Property Document:
    
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-securitygroupids
    - ``p_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-subnetids
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.VPCOptions"
    
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-securitygroupids"""
    p_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-vpcoptions.html#cfn-opensearchservice-domain-vpcoptions-subnetids"""

@attr.s
class PropDomainMasterUserOptions(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.MasterUserOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html

    Property Document:
    
    - ``p_MasterUserARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserarn
    - ``p_MasterUserName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masterusername
    - ``p_MasterUserPassword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.MasterUserOptions"
    
    p_MasterUserARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserarn"""
    p_MasterUserName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masterusername"""
    p_MasterUserPassword: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserPassword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-masteruseroptions.html#cfn-opensearchservice-domain-masteruseroptions-masteruserpassword"""

@attr.s
class PropDomainClusterConfig(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.ClusterConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html

    Property Document:
    
    - ``p_DedicatedMasterCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastercount
    - ``p_DedicatedMasterEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmasterenabled
    - ``p_DedicatedMasterType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastertype
    - ``p_InstanceCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancecount
    - ``p_InstanceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancetype
    - ``p_WarmCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmcount
    - ``p_WarmEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmenabled
    - ``p_WarmType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmtype
    - ``p_ZoneAwarenessConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessconfig
    - ``p_ZoneAwarenessEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessenabled
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.ClusterConfig"
    
    p_DedicatedMasterCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastercount"""
    p_DedicatedMasterEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmasterenabled"""
    p_DedicatedMasterType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-dedicatedmastertype"""
    p_InstanceCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancecount"""
    p_InstanceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-instancetype"""
    p_WarmCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmcount"""
    p_WarmEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmenabled"""
    p_WarmType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-warmtype"""
    p_ZoneAwarenessConfig: typing.Union['PropDomainZoneAwarenessConfig', dict] = attr.ib(
        default=None,
        converter=PropDomainZoneAwarenessConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainZoneAwarenessConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ZoneAwarenessConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessconfig"""
    p_ZoneAwarenessEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ZoneAwarenessEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-clusterconfig.html#cfn-opensearchservice-domain-clusterconfig-zoneawarenessenabled"""

@attr.s
class PropDomainAdvancedSecurityOptionsInput(Property):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain.AdvancedSecurityOptionsInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-enabled
    - ``p_InternalUserDatabaseEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled
    - ``p_MasterUserOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-masteruseroptions
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain.AdvancedSecurityOptionsInput"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-enabled"""
    p_InternalUserDatabaseEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InternalUserDatabaseEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled"""
    p_MasterUserOptions: typing.Union['PropDomainMasterUserOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainMasterUserOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainMasterUserOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opensearchservice-domain-advancedsecurityoptionsinput.html#cfn-opensearchservice-domain-advancedsecurityoptionsinput-masteruseroptions"""


#--- Resource declaration ---

@attr.s
class Domain(Resource):
    """
    AWS Object Type = "AWS::OpenSearchService::Domain"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html

    Property Document:
    
    - ``p_AccessPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-accesspolicies
    - ``p_AdvancedOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedoptions
    - ``p_AdvancedSecurityOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedsecurityoptions
    - ``p_ClusterConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-clusterconfig
    - ``p_CognitoOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-cognitooptions
    - ``p_DomainEndpointOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainendpointoptions
    - ``p_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainname
    - ``p_EBSOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-ebsoptions
    - ``p_EncryptionAtRestOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-encryptionatrestoptions
    - ``p_EngineVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-engineversion
    - ``p_LogPublishingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-logpublishingoptions
    - ``p_NodeToNodeEncryptionOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions
    - ``p_SnapshotOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-snapshotoptions
    - ``p_VPCOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-vpcoptions
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-tags
    """
    AWS_OBJECT_TYPE = "AWS::OpenSearchService::Domain"

    
    p_AccessPolicies: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-accesspolicies"""
    p_AdvancedOptions: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "AdvancedOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedoptions"""
    p_AdvancedSecurityOptions: typing.Union['PropDomainAdvancedSecurityOptionsInput', dict] = attr.ib(
        default=None,
        converter=PropDomainAdvancedSecurityOptionsInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainAdvancedSecurityOptionsInput)),
        metadata={AttrMeta.PROPERTY_NAME: "AdvancedSecurityOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-advancedsecurityoptions"""
    p_ClusterConfig: typing.Union['PropDomainClusterConfig', dict] = attr.ib(
        default=None,
        converter=PropDomainClusterConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainClusterConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-clusterconfig"""
    p_CognitoOptions: typing.Union['PropDomainCognitoOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainCognitoOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainCognitoOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CognitoOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-cognitooptions"""
    p_DomainEndpointOptions: typing.Union['PropDomainDomainEndpointOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainDomainEndpointOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainDomainEndpointOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainEndpointOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainendpointoptions"""
    p_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-domainname"""
    p_EBSOptions: typing.Union['PropDomainEBSOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainEBSOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainEBSOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-ebsoptions"""
    p_EncryptionAtRestOptions: typing.Union['PropDomainEncryptionAtRestOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainEncryptionAtRestOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainEncryptionAtRestOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionAtRestOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-encryptionatrestoptions"""
    p_EngineVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EngineVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-engineversion"""
    p_LogPublishingOptions: typing.Union['PropDomainLogPublishingOption', dict] = attr.ib(
        default=None,
        converter=PropDomainLogPublishingOption.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainLogPublishingOption)),
        metadata={AttrMeta.PROPERTY_NAME: "LogPublishingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-logpublishingoptions"""
    p_NodeToNodeEncryptionOptions: typing.Union['PropDomainNodeToNodeEncryptionOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainNodeToNodeEncryptionOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainNodeToNodeEncryptionOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "NodeToNodeEncryptionOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-nodetonodeencryptionoptions"""
    p_SnapshotOptions: typing.Union['PropDomainSnapshotOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainSnapshotOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainSnapshotOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-snapshotoptions"""
    p_VPCOptions: typing.Union['PropDomainVPCOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainVPCOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainVPCOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "VPCOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-vpcoptions"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#cfn-opensearchservice-domain-tags"""

    
    @property
    def rv_DomainEndpoint(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainEndpoint")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_DomainArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html#aws-resource-opensearchservice-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainArn")
    
