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
class PropClusterS3(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.S3"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled
    - ``p_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.S3"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled"""
    p_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix"""

@attr.s
class PropClusterCloudWatchLogs(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.CloudWatchLogs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled
    - ``p_LogGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.CloudWatchLogs"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled"""
    p_LogGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup"""

@attr.s
class PropClusterPublicAccess(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.PublicAccess"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html

    Property Document:
    
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html#cfn-msk-cluster-publicaccess-type
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.PublicAccess"
    
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html#cfn-msk-cluster-publicaccess-type"""

@attr.s
class PropClusterEncryptionAtRest(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EncryptionAtRest"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html

    Property Document:
    
    - ``rp_DataVolumeKMSKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EncryptionAtRest"
    
    rp_DataVolumeKMSKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataVolumeKMSKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid"""

@attr.s
class PropClusterUnauthenticated(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Unauthenticated"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html#cfn-msk-cluster-unauthenticated-enabled
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Unauthenticated"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html#cfn-msk-cluster-unauthenticated-enabled"""

@attr.s
class PropClusterEncryptionInTransit(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EncryptionInTransit"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html

    Property Document:
    
    - ``p_ClientBroker``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker
    - ``p_InCluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EncryptionInTransit"
    
    p_ClientBroker: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientBroker"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker"""
    p_InCluster: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "InCluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster"""

@attr.s
class PropClusterProvisionedThroughput(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.ProvisionedThroughput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-enabled
    - ``p_VolumeThroughput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-volumethroughput
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.ProvisionedThroughput"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-enabled"""
    p_VolumeThroughput: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeThroughput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-volumethroughput"""

@attr.s
class PropClusterEncryptionInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EncryptionInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html

    Property Document:
    
    - ``p_EncryptionAtRest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest
    - ``p_EncryptionInTransit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EncryptionInfo"
    
    p_EncryptionAtRest: typing.Union['PropClusterEncryptionAtRest', dict] = attr.ib(
        default=None,
        converter=PropClusterEncryptionAtRest.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterEncryptionAtRest)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionAtRest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest"""
    p_EncryptionInTransit: typing.Union['PropClusterEncryptionInTransit', dict] = attr.ib(
        default=None,
        converter=PropClusterEncryptionInTransit.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterEncryptionInTransit)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionInTransit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit"""

@attr.s
class PropClusterIam(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Iam"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html#cfn-msk-cluster-iam-enabled
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Iam"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html#cfn-msk-cluster-iam-enabled"""

@attr.s
class PropClusterConfigurationInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.ConfigurationInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html

    Property Document:
    
    - ``rp_Arn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn
    - ``rp_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.ConfigurationInfo"
    
    rp_Arn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Arn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn"""
    rp_Revision: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision"""

@attr.s
class PropClusterScram(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Scram"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html#cfn-msk-cluster-scram-enabled
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Scram"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html#cfn-msk-cluster-scram-enabled"""

@attr.s
class PropClusterJmxExporter(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.JmxExporter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html

    Property Document:
    
    - ``rp_EnabledInBroker``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.JmxExporter"
    
    rp_EnabledInBroker: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "EnabledInBroker"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker"""

@attr.s
class PropClusterConnectivityInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.ConnectivityInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html

    Property Document:
    
    - ``p_PublicAccess``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-publicaccess
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.ConnectivityInfo"
    
    p_PublicAccess: typing.Union['PropClusterPublicAccess', dict] = attr.ib(
        default=None,
        converter=PropClusterPublicAccess.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterPublicAccess)),
        metadata={AttrMeta.PROPERTY_NAME: "PublicAccess"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-publicaccess"""

@attr.s
class PropClusterNodeExporter(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.NodeExporter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html

    Property Document:
    
    - ``rp_EnabledInBroker``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.NodeExporter"
    
    rp_EnabledInBroker: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "EnabledInBroker"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker"""

@attr.s
class PropClusterEBSStorageInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EBSStorageInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html

    Property Document:
    
    - ``p_ProvisionedThroughput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-provisionedthroughput
    - ``p_VolumeSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EBSStorageInfo"
    
    p_ProvisionedThroughput: typing.Union['PropClusterProvisionedThroughput', dict] = attr.ib(
        default=None,
        converter=PropClusterProvisionedThroughput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterProvisionedThroughput)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedThroughput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-provisionedthroughput"""
    p_VolumeSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize"""

@attr.s
class PropClusterFirehose(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Firehose"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled
    - ``p_DeliveryStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Firehose"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled"""
    p_DeliveryStream: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStream"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream"""

@attr.s
class PropClusterTls(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Tls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html

    Property Document:
    
    - ``p_CertificateAuthorityArnList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-enabled
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Tls"
    
    p_CertificateAuthorityArnList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateAuthorityArnList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-enabled"""

@attr.s
class PropClusterBrokerLogs(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.BrokerLogs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html

    Property Document:
    
    - ``p_CloudWatchLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs
    - ``p_Firehose``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose
    - ``p_S3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.BrokerLogs"
    
    p_CloudWatchLogs: typing.Union['PropClusterCloudWatchLogs', dict] = attr.ib(
        default=None,
        converter=PropClusterCloudWatchLogs.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterCloudWatchLogs)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs"""
    p_Firehose: typing.Union['PropClusterFirehose', dict] = attr.ib(
        default=None,
        converter=PropClusterFirehose.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterFirehose)),
        metadata={AttrMeta.PROPERTY_NAME: "Firehose"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose"""
    p_S3: typing.Union['PropClusterS3', dict] = attr.ib(
        default=None,
        converter=PropClusterS3.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterS3)),
        metadata={AttrMeta.PROPERTY_NAME: "S3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3"""

@attr.s
class PropClusterPrometheus(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Prometheus"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html

    Property Document:
    
    - ``p_JmxExporter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter
    - ``p_NodeExporter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Prometheus"
    
    p_JmxExporter: typing.Union['PropClusterJmxExporter', dict] = attr.ib(
        default=None,
        converter=PropClusterJmxExporter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterJmxExporter)),
        metadata={AttrMeta.PROPERTY_NAME: "JmxExporter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter"""
    p_NodeExporter: typing.Union['PropClusterNodeExporter', dict] = attr.ib(
        default=None,
        converter=PropClusterNodeExporter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterNodeExporter)),
        metadata={AttrMeta.PROPERTY_NAME: "NodeExporter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter"""

@attr.s
class PropClusterLoggingInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.LoggingInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html

    Property Document:
    
    - ``rp_BrokerLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.LoggingInfo"
    
    rp_BrokerLogs: typing.Union['PropClusterBrokerLogs', dict] = attr.ib(
        default=None,
        converter=PropClusterBrokerLogs.from_dict,
        validator=attr.validators.instance_of(PropClusterBrokerLogs),
        metadata={AttrMeta.PROPERTY_NAME: "BrokerLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs"""

@attr.s
class PropClusterSasl(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Sasl"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html

    Property Document:
    
    - ``p_Iam``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam
    - ``p_Scram``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Sasl"
    
    p_Iam: typing.Union['PropClusterIam', dict] = attr.ib(
        default=None,
        converter=PropClusterIam.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterIam)),
        metadata={AttrMeta.PROPERTY_NAME: "Iam"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam"""
    p_Scram: typing.Union['PropClusterScram', dict] = attr.ib(
        default=None,
        converter=PropClusterScram.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterScram)),
        metadata={AttrMeta.PROPERTY_NAME: "Scram"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram"""

@attr.s
class PropClusterStorageInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.StorageInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html

    Property Document:
    
    - ``p_EBSStorageInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.StorageInfo"
    
    p_EBSStorageInfo: typing.Union['PropClusterEBSStorageInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterEBSStorageInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterEBSStorageInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSStorageInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo"""

@attr.s
class PropClusterClientAuthentication(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.ClientAuthentication"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html

    Property Document:
    
    - ``p_Sasl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl
    - ``p_Tls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls
    - ``p_Unauthenticated``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-unauthenticated
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.ClientAuthentication"
    
    p_Sasl: typing.Union['PropClusterSasl', dict] = attr.ib(
        default=None,
        converter=PropClusterSasl.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterSasl)),
        metadata={AttrMeta.PROPERTY_NAME: "Sasl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl"""
    p_Tls: typing.Union['PropClusterTls', dict] = attr.ib(
        default=None,
        converter=PropClusterTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterTls)),
        metadata={AttrMeta.PROPERTY_NAME: "Tls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls"""
    p_Unauthenticated: typing.Union['PropClusterUnauthenticated', dict] = attr.ib(
        default=None,
        converter=PropClusterUnauthenticated.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterUnauthenticated)),
        metadata={AttrMeta.PROPERTY_NAME: "Unauthenticated"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-unauthenticated"""

@attr.s
class PropClusterOpenMonitoring(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.OpenMonitoring"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html

    Property Document:
    
    - ``rp_Prometheus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.OpenMonitoring"
    
    rp_Prometheus: typing.Union['PropClusterPrometheus', dict] = attr.ib(
        default=None,
        converter=PropClusterPrometheus.from_dict,
        validator=attr.validators.instance_of(PropClusterPrometheus),
        metadata={AttrMeta.PROPERTY_NAME: "Prometheus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus"""

@attr.s
class PropClusterBrokerNodeGroupInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.BrokerNodeGroupInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html

    Property Document:
    
    - ``rp_ClientSubnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets
    - ``rp_InstanceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype
    - ``p_BrokerAZDistribution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution
    - ``p_ConnectivityInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo
    - ``p_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups
    - ``p_StorageInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.BrokerNodeGroupInfo"
    
    rp_ClientSubnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientSubnets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets"""
    rp_InstanceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype"""
    p_BrokerAZDistribution: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BrokerAZDistribution"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution"""
    p_ConnectivityInfo: typing.Union['PropClusterConnectivityInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterConnectivityInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterConnectivityInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectivityInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo"""
    p_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups"""
    p_StorageInfo: typing.Union['PropClusterStorageInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterStorageInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterStorageInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "StorageInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo"""


#--- Resource declaration ---

@attr.s
class BatchScramSecret(Resource):
    """
    AWS Object Type = "AWS::MSK::BatchScramSecret"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html

    Property Document:
    
    - ``rp_ClusterArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn
    - ``p_SecretArnList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist
    """
    AWS_OBJECT_TYPE = "AWS::MSK::BatchScramSecret"

    
    rp_ClusterArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn"""
    p_SecretArnList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecretArnList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist"""

    

@attr.s
class Cluster(Resource):
    """
    AWS Object Type = "AWS::MSK::Cluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html

    Property Document:
    
    - ``rp_BrokerNodeGroupInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
    - ``rp_ClusterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
    - ``rp_KafkaVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
    - ``rp_NumberOfBrokerNodes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
    - ``p_ClientAuthentication``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
    - ``p_ConfigurationInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
    - ``p_CurrentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion
    - ``p_EncryptionInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
    - ``p_EnhancedMonitoring``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
    - ``p_LoggingInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
    - ``p_OpenMonitoring``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster"

    
    rp_BrokerNodeGroupInfo: typing.Union['PropClusterBrokerNodeGroupInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterBrokerNodeGroupInfo.from_dict,
        validator=attr.validators.instance_of(PropClusterBrokerNodeGroupInfo),
        metadata={AttrMeta.PROPERTY_NAME: "BrokerNodeGroupInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo"""
    rp_ClusterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername"""
    rp_KafkaVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion"""
    rp_NumberOfBrokerNodes: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "NumberOfBrokerNodes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes"""
    p_ClientAuthentication: typing.Union['PropClusterClientAuthentication', dict] = attr.ib(
        default=None,
        converter=PropClusterClientAuthentication.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterClientAuthentication)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientAuthentication"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication"""
    p_ConfigurationInfo: typing.Union['PropClusterConfigurationInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterConfigurationInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterConfigurationInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo"""
    p_CurrentVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CurrentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion"""
    p_EncryptionInfo: typing.Union['PropClusterEncryptionInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterEncryptionInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterEncryptionInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo"""
    p_EnhancedMonitoring: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EnhancedMonitoring"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring"""
    p_LoggingInfo: typing.Union['PropClusterLoggingInfo', dict] = attr.ib(
        default=None,
        converter=PropClusterLoggingInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterLoggingInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo"""
    p_OpenMonitoring: typing.Union['PropClusterOpenMonitoring', dict] = attr.ib(
        default=None,
        converter=PropClusterOpenMonitoring.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropClusterOpenMonitoring)),
        metadata={AttrMeta.PROPERTY_NAME: "OpenMonitoring"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring"""
    p_Tags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#aws-resource-msk-cluster-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Configuration(Resource):
    """
    AWS Object Type = "AWS::MSK::Configuration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html

    Property Document:
    
    - ``rp_ServerProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description
    - ``p_KafkaVersionsList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Configuration"

    
    rp_ServerProperties: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServerProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description"""
    p_KafkaVersionsList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaVersionsList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#aws-resource-msk-configuration-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
