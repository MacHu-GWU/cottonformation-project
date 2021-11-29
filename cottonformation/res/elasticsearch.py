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
class PropDomainDomainEndpointOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.DomainEndpointOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html

    Property Document:
    
    - ``p_CustomEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpoint
    - ``p_CustomEndpointCertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointcertificatearn
    - ``p_CustomEndpointEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointenabled
    - ``p_EnforceHTTPS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-enforcehttps
    - ``p_TLSSecurityPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-tlssecuritypolicy
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.DomainEndpointOptions"
    
    p_CustomEndpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpoint"""
    p_CustomEndpointCertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpointCertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointcertificatearn"""
    p_CustomEndpointEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomEndpointEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-customendpointenabled"""
    p_EnforceHTTPS: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnforceHTTPS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-enforcehttps"""
    p_TLSSecurityPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TLSSecurityPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html#cfn-elasticsearch-domain-domainendpointoptions-tlssecuritypolicy"""

@attr.s
class PropDomainNodeToNodeEncryptionOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.NodeToNodeEncryptionOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.NodeToNodeEncryptionOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions-enabled"""

@attr.s
class PropDomainColdStorageOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.ColdStorageOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html#cfn-elasticsearch-domain-coldstorageoptions-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.ColdStorageOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html#cfn-elasticsearch-domain-coldstorageoptions-enabled"""

@attr.s
class PropDomainZoneAwarenessConfig(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.ZoneAwarenessConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html

    Property Document:
    
    - ``p_AvailabilityZoneCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html#cfn-elasticsearch-domain-zoneawarenessconfig-availabilityzonecount
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.ZoneAwarenessConfig"
    
    p_AvailabilityZoneCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZoneCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html#cfn-elasticsearch-domain-zoneawarenessconfig-availabilityzonecount"""

@attr.s
class PropDomainSnapshotOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.SnapshotOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html

    Property Document:
    
    - ``p_AutomatedSnapshotStartHour``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.SnapshotOptions"
    
    p_AutomatedSnapshotStartHour: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "AutomatedSnapshotStartHour"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour"""

@attr.s
class PropDomainCognitoOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.CognitoOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-enabled
    - ``p_IdentityPoolId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-identitypoolid
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-rolearn
    - ``p_UserPoolId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-userpoolid
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.CognitoOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-enabled"""
    p_IdentityPoolId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IdentityPoolId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-identitypoolid"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-rolearn"""
    p_UserPoolId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UserPoolId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html#cfn-elasticsearch-domain-cognitooptions-userpoolid"""

@attr.s
class PropDomainVPCOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.VPCOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html

    Property Document:
    
    - ``p_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-securitygroupids
    - ``p_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-subnetids
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.VPCOptions"
    
    p_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-securitygroupids"""
    p_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html#cfn-elasticsearch-domain-vpcoptions-subnetids"""

@attr.s
class PropDomainMasterUserOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.MasterUserOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html

    Property Document:
    
    - ``p_MasterUserARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserarn
    - ``p_MasterUserName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masterusername
    - ``p_MasterUserPassword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserpassword
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.MasterUserOptions"
    
    p_MasterUserARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserarn"""
    p_MasterUserName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masterusername"""
    p_MasterUserPassword: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserPassword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html#cfn-elasticsearch-domain-masteruseroptions-masteruserpassword"""

@attr.s
class PropDomainLogPublishingOption(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.LogPublishingOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html

    Property Document:
    
    - ``p_CloudWatchLogsLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-cloudwatchlogsloggrouparn
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-enabled
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.LogPublishingOption"
    
    p_CloudWatchLogsLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogsLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-cloudwatchlogsloggrouparn"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html#cfn-elasticsearch-domain-logpublishingoption-enabled"""

@attr.s
class PropDomainEBSOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.EBSOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html

    Property Document:
    
    - ``p_EBSEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled
    - ``p_Iops``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops
    - ``p_VolumeSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize
    - ``p_VolumeType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.EBSOptions"
    
    p_EBSEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled"""
    p_Iops: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Iops"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops"""
    p_VolumeSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize"""
    p_VolumeType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype"""

@attr.s
class PropDomainEncryptionAtRestOptions(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.EncryptionAtRestOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-enabled
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-kmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.EncryptionAtRestOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-enabled"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html#cfn-elasticsearch-domain-encryptionatrestoptions-kmskeyid"""

@attr.s
class PropDomainElasticsearchClusterConfig(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.ElasticsearchClusterConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html

    Property Document:
    
    - ``p_ColdStorageOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-coldstorageoptions
    - ``p_DedicatedMasterCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastercount
    - ``p_DedicatedMasterEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmasterenabled
    - ``p_DedicatedMasterType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastertype
    - ``p_InstanceCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instancecount
    - ``p_InstanceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instnacetype
    - ``p_WarmCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmcount
    - ``p_WarmEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmenabled
    - ``p_WarmType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmtype
    - ``p_ZoneAwarenessConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-zoneawarenessconfig
    - ``p_ZoneAwarenessEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-zoneawarenessenabled
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.ElasticsearchClusterConfig"
    
    p_ColdStorageOptions: typing.Union['PropDomainColdStorageOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainColdStorageOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainColdStorageOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "ColdStorageOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-coldstorageoptions"""
    p_DedicatedMasterCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastercount"""
    p_DedicatedMasterEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmasterenabled"""
    p_DedicatedMasterType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DedicatedMasterType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastertype"""
    p_InstanceCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instancecount"""
    p_InstanceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instnacetype"""
    p_WarmCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmcount"""
    p_WarmEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmenabled"""
    p_WarmType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WarmType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-warmtype"""
    p_ZoneAwarenessConfig: typing.Union['PropDomainZoneAwarenessConfig', dict] = attr.ib(
        default=None,
        converter=PropDomainZoneAwarenessConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainZoneAwarenessConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ZoneAwarenessConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticsearchclusterconfig-zoneawarenessconfig"""
    p_ZoneAwarenessEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ZoneAwarenessEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-zoneawarenessenabled"""

@attr.s
class PropDomainAdvancedSecurityOptionsInput(Property):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain.AdvancedSecurityOptionsInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled
    - ``p_InternalUserDatabaseEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled
    - ``p_MasterUserOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain.AdvancedSecurityOptionsInput"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled"""
    p_InternalUserDatabaseEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InternalUserDatabaseEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled"""
    p_MasterUserOptions: typing.Union['PropDomainMasterUserOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainMasterUserOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainMasterUserOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions"""


#--- Resource declaration ---

@attr.s
class Domain(Resource):
    """
    AWS Object Type = "AWS::Elasticsearch::Domain"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html

    Property Document:
    
    - ``p_AccessPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies
    - ``p_AdvancedOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions
    - ``p_AdvancedSecurityOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedsecurityoptions
    - ``p_CognitoOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-cognitooptions
    - ``p_DomainEndpointOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainendpointoptions
    - ``p_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname
    - ``p_EBSOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions
    - ``p_ElasticsearchClusterConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig
    - ``p_ElasticsearchVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion
    - ``p_EncryptionAtRestOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-encryptionatrestoptions
    - ``p_LogPublishingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-logpublishingoptions
    - ``p_NodeToNodeEncryptionOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions
    - ``p_SnapshotOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions
    - ``p_VPCOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-vpcoptions
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags
    """
    AWS_OBJECT_TYPE = "AWS::Elasticsearch::Domain"

    
    p_AccessPolicies: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies"""
    p_AdvancedOptions: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "AdvancedOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions"""
    p_AdvancedSecurityOptions: typing.Union['PropDomainAdvancedSecurityOptionsInput', dict] = attr.ib(
        default=None,
        converter=PropDomainAdvancedSecurityOptionsInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainAdvancedSecurityOptionsInput)),
        metadata={AttrMeta.PROPERTY_NAME: "AdvancedSecurityOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedsecurityoptions"""
    p_CognitoOptions: typing.Union['PropDomainCognitoOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainCognitoOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainCognitoOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CognitoOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-cognitooptions"""
    p_DomainEndpointOptions: typing.Union['PropDomainDomainEndpointOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainDomainEndpointOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainDomainEndpointOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainEndpointOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainendpointoptions"""
    p_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname"""
    p_EBSOptions: typing.Union['PropDomainEBSOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainEBSOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainEBSOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions"""
    p_ElasticsearchClusterConfig: typing.Union['PropDomainElasticsearchClusterConfig', dict] = attr.ib(
        default=None,
        converter=PropDomainElasticsearchClusterConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainElasticsearchClusterConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticsearchClusterConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig"""
    p_ElasticsearchVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticsearchVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion"""
    p_EncryptionAtRestOptions: typing.Union['PropDomainEncryptionAtRestOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainEncryptionAtRestOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainEncryptionAtRestOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionAtRestOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-encryptionatrestoptions"""
    p_LogPublishingOptions: typing.Union['PropDomainLogPublishingOption', dict] = attr.ib(
        default=None,
        converter=PropDomainLogPublishingOption.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainLogPublishingOption)),
        metadata={AttrMeta.PROPERTY_NAME: "LogPublishingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-logpublishingoptions"""
    p_NodeToNodeEncryptionOptions: typing.Union['PropDomainNodeToNodeEncryptionOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainNodeToNodeEncryptionOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainNodeToNodeEncryptionOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "NodeToNodeEncryptionOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-nodetonodeencryptionoptions"""
    p_SnapshotOptions: typing.Union['PropDomainSnapshotOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainSnapshotOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainSnapshotOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions"""
    p_VPCOptions: typing.Union['PropDomainVPCOptions', dict] = attr.ib(
        default=None,
        converter=PropDomainVPCOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDomainVPCOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "VPCOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-vpcoptions"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#aws-resource-elasticsearch-domain-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_DomainArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#aws-resource-elasticsearch-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainArn")
    
    @property
    def rv_DomainEndpoint(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#aws-resource-elasticsearch-domain-return-values"""
        return GetAtt(resource=self, attr_name="DomainEndpoint")
    
