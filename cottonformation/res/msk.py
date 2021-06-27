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
class ClusterS3(Property):
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
class ClusterCloudWatchLogs(Property):
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
class ClusterEncryptionAtRest(Property):
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
class ClusterEncryptionInTransit(Property):
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
class ClusterEncryptionInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EncryptionInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html

    Property Document:
    
    - ``p_EncryptionAtRest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest
    - ``p_EncryptionInTransit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EncryptionInfo"
    
    p_EncryptionAtRest: typing.Union['ClusterEncryptionAtRest', dict] = attr.ib(
        default=None,
        converter=ClusterEncryptionAtRest.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterEncryptionAtRest)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionAtRest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest"""
    p_EncryptionInTransit: typing.Union['ClusterEncryptionInTransit', dict] = attr.ib(
        default=None,
        converter=ClusterEncryptionInTransit.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterEncryptionInTransit)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionInTransit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit"""

@attr.s
class ClusterIam(Property):
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
class ClusterConfigurationInfo(Property):
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
class ClusterScram(Property):
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
class ClusterJmxExporter(Property):
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
class ClusterNodeExporter(Property):
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
class ClusterEBSStorageInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.EBSStorageInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html

    Property Document:
    
    - ``p_VolumeSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.EBSStorageInfo"
    
    p_VolumeSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "VolumeSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize"""

@attr.s
class ClusterFirehose(Property):
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
class ClusterTls(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Tls"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html

    Property Document:
    
    - ``p_CertificateAuthorityArnList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Tls"
    
    p_CertificateAuthorityArnList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateAuthorityArnList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist"""

@attr.s
class ClusterBrokerLogs(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.BrokerLogs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html

    Property Document:
    
    - ``p_CloudWatchLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs
    - ``p_Firehose``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose
    - ``p_S3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.BrokerLogs"
    
    p_CloudWatchLogs: typing.Union['ClusterCloudWatchLogs', dict] = attr.ib(
        default=None,
        converter=ClusterCloudWatchLogs.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterCloudWatchLogs)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs"""
    p_Firehose: typing.Union['ClusterFirehose', dict] = attr.ib(
        default=None,
        converter=ClusterFirehose.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterFirehose)),
        metadata={AttrMeta.PROPERTY_NAME: "Firehose"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose"""
    p_S3: typing.Union['ClusterS3', dict] = attr.ib(
        default=None,
        converter=ClusterS3.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterS3)),
        metadata={AttrMeta.PROPERTY_NAME: "S3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3"""

@attr.s
class ClusterPrometheus(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Prometheus"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html

    Property Document:
    
    - ``p_JmxExporter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter
    - ``p_NodeExporter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Prometheus"
    
    p_JmxExporter: typing.Union['ClusterJmxExporter', dict] = attr.ib(
        default=None,
        converter=ClusterJmxExporter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterJmxExporter)),
        metadata={AttrMeta.PROPERTY_NAME: "JmxExporter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter"""
    p_NodeExporter: typing.Union['ClusterNodeExporter', dict] = attr.ib(
        default=None,
        converter=ClusterNodeExporter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterNodeExporter)),
        metadata={AttrMeta.PROPERTY_NAME: "NodeExporter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter"""

@attr.s
class ClusterLoggingInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.LoggingInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html

    Property Document:
    
    - ``rp_BrokerLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.LoggingInfo"
    
    rp_BrokerLogs: typing.Union['ClusterBrokerLogs', dict] = attr.ib(
        default=None,
        converter=ClusterBrokerLogs.from_dict,
        validator=attr.validators.instance_of(ClusterBrokerLogs),
        metadata={AttrMeta.PROPERTY_NAME: "BrokerLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs"""

@attr.s
class ClusterSasl(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.Sasl"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html

    Property Document:
    
    - ``p_Iam``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam
    - ``p_Scram``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.Sasl"
    
    p_Iam: typing.Union['ClusterIam', dict] = attr.ib(
        default=None,
        converter=ClusterIam.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterIam)),
        metadata={AttrMeta.PROPERTY_NAME: "Iam"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam"""
    p_Scram: typing.Union['ClusterScram', dict] = attr.ib(
        default=None,
        converter=ClusterScram.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterScram)),
        metadata={AttrMeta.PROPERTY_NAME: "Scram"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram"""

@attr.s
class ClusterStorageInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.StorageInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html

    Property Document:
    
    - ``p_EBSStorageInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.StorageInfo"
    
    p_EBSStorageInfo: typing.Union['ClusterEBSStorageInfo', dict] = attr.ib(
        default=None,
        converter=ClusterEBSStorageInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterEBSStorageInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "EBSStorageInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo"""

@attr.s
class ClusterClientAuthentication(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.ClientAuthentication"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html

    Property Document:
    
    - ``p_Sasl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl
    - ``p_Tls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.ClientAuthentication"
    
    p_Sasl: typing.Union['ClusterSasl', dict] = attr.ib(
        default=None,
        converter=ClusterSasl.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterSasl)),
        metadata={AttrMeta.PROPERTY_NAME: "Sasl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl"""
    p_Tls: typing.Union['ClusterTls', dict] = attr.ib(
        default=None,
        converter=ClusterTls.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterTls)),
        metadata={AttrMeta.PROPERTY_NAME: "Tls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls"""

@attr.s
class ClusterOpenMonitoring(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.OpenMonitoring"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html

    Property Document:
    
    - ``rp_Prometheus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster.OpenMonitoring"
    
    rp_Prometheus: typing.Union['ClusterPrometheus', dict] = attr.ib(
        default=None,
        converter=ClusterPrometheus.from_dict,
        validator=attr.validators.instance_of(ClusterPrometheus),
        metadata={AttrMeta.PROPERTY_NAME: "Prometheus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus"""

@attr.s
class ClusterBrokerNodeGroupInfo(Property):
    """
    AWS Object Type = "AWS::MSK::Cluster.BrokerNodeGroupInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html

    Property Document:
    
    - ``rp_ClientSubnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets
    - ``rp_InstanceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype
    - ``p_BrokerAZDistribution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution
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
    p_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups"""
    p_StorageInfo: typing.Union['ClusterStorageInfo', dict] = attr.ib(
        default=None,
        converter=ClusterStorageInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterStorageInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "StorageInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo"""


#--- Resource declaration ---

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
    - ``p_EncryptionInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
    - ``p_EnhancedMonitoring``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
    - ``p_LoggingInfo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
    - ``p_OpenMonitoring``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
    """
    AWS_OBJECT_TYPE = "AWS::MSK::Cluster"

    
    rp_BrokerNodeGroupInfo: typing.Union['ClusterBrokerNodeGroupInfo', dict] = attr.ib(
        default=None,
        converter=ClusterBrokerNodeGroupInfo.from_dict,
        validator=attr.validators.instance_of(ClusterBrokerNodeGroupInfo),
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
    p_ClientAuthentication: typing.Union['ClusterClientAuthentication', dict] = attr.ib(
        default=None,
        converter=ClusterClientAuthentication.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterClientAuthentication)),
        metadata={AttrMeta.PROPERTY_NAME: "ClientAuthentication"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication"""
    p_ConfigurationInfo: typing.Union['ClusterConfigurationInfo', dict] = attr.ib(
        default=None,
        converter=ClusterConfigurationInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterConfigurationInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo"""
    p_EncryptionInfo: typing.Union['ClusterEncryptionInfo', dict] = attr.ib(
        default=None,
        converter=ClusterEncryptionInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterEncryptionInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo"""
    p_EnhancedMonitoring: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EnhancedMonitoring"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring"""
    p_LoggingInfo: typing.Union['ClusterLoggingInfo', dict] = attr.ib(
        default=None,
        converter=ClusterLoggingInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterLoggingInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingInfo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo"""
    p_OpenMonitoring: typing.Union['ClusterOpenMonitoring', dict] = attr.ib(
        default=None,
        converter=ClusterOpenMonitoring.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ClusterOpenMonitoring)),
        metadata={AttrMeta.PROPERTY_NAME: "OpenMonitoring"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags"""

    
