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
class PropConnectorFirehoseLogDelivery(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.FirehoseLogDelivery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-enabled
    - ``p_DeliveryStream``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.FirehoseLogDelivery"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-enabled"""
    p_DeliveryStream: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStream"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-firehoselogdelivery.html#cfn-kafkaconnect-connector-firehoselogdelivery-deliverystream"""

@attr.s
class PropConnectorVpc(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.Vpc"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html

    Property Document:
    
    - ``rp_SecurityGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-securitygroups
    - ``rp_Subnets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-subnets
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.Vpc"
    
    rp_SecurityGroups: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-securitygroups"""
    rp_Subnets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subnets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-vpc.html#cfn-kafkaconnect-connector-vpc-subnets"""

@attr.s
class PropConnectorS3LogDelivery(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.S3LogDelivery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-enabled
    - ``p_Bucket``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-bucket
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-prefix
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.S3LogDelivery"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-enabled"""
    p_Bucket: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Bucket"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-bucket"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-s3logdelivery.html#cfn-kafkaconnect-connector-s3logdelivery-prefix"""

@attr.s
class PropConnectorWorkerConfiguration(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.WorkerConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html

    Property Document:
    
    - ``rp_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-revision
    - ``rp_WorkerConfigurationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-workerconfigurationarn
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.WorkerConfiguration"
    
    rp_Revision: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-revision"""
    rp_WorkerConfigurationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "WorkerConfigurationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerconfiguration.html#cfn-kafkaconnect-connector-workerconfiguration-workerconfigurationarn"""

@attr.s
class PropConnectorScaleInPolicy(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.ScaleInPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html

    Property Document:
    
    - ``rp_CpuUtilizationPercentage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.ScaleInPolicy"
    
    rp_CpuUtilizationPercentage: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "CpuUtilizationPercentage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleinpolicy.html#cfn-kafkaconnect-connector-scaleinpolicy-cpuutilizationpercentage"""

@attr.s
class PropConnectorKafkaClusterEncryptionInTransit(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.KafkaClusterEncryptionInTransit"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html

    Property Document:
    
    - ``rp_EncryptionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.KafkaClusterEncryptionInTransit"
    
    rp_EncryptionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterencryptionintransit.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit-encryptiontype"""

@attr.s
class PropConnectorScaleOutPolicy(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.ScaleOutPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html

    Property Document:
    
    - ``rp_CpuUtilizationPercentage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html#cfn-kafkaconnect-connector-scaleoutpolicy-cpuutilizationpercentage
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.ScaleOutPolicy"
    
    rp_CpuUtilizationPercentage: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "CpuUtilizationPercentage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-scaleoutpolicy.html#cfn-kafkaconnect-connector-scaleoutpolicy-cpuutilizationpercentage"""

@attr.s
class PropConnectorProvisionedCapacity(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.ProvisionedCapacity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html

    Property Document:
    
    - ``rp_WorkerCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-workercount
    - ``p_McuCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-mcucount
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.ProvisionedCapacity"
    
    rp_WorkerCount: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "WorkerCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-workercount"""
    p_McuCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "McuCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-provisionedcapacity.html#cfn-kafkaconnect-connector-provisionedcapacity-mcucount"""

@attr.s
class PropConnectorCloudWatchLogsLogDelivery(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.CloudWatchLogsLogDelivery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html

    Property Document:
    
    - ``rp_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-enabled
    - ``p_LogGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-loggroup
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.CloudWatchLogsLogDelivery"
    
    rp_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-enabled"""
    p_LogGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.html#cfn-kafkaconnect-connector-cloudwatchlogslogdelivery-loggroup"""

@attr.s
class PropConnectorCustomPlugin(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.CustomPlugin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html

    Property Document:
    
    - ``rp_CustomPluginArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-custompluginarn
    - ``rp_Revision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-revision
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.CustomPlugin"
    
    rp_CustomPluginArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CustomPluginArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-custompluginarn"""
    rp_Revision: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Revision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-customplugin.html#cfn-kafkaconnect-connector-customplugin-revision"""

@attr.s
class PropConnectorPlugin(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.Plugin"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html

    Property Document:
    
    - ``rp_CustomPlugin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html#cfn-kafkaconnect-connector-plugin-customplugin
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.Plugin"
    
    rp_CustomPlugin: typing.Union['PropConnectorCustomPlugin', dict] = attr.ib(
        default=None,
        converter=PropConnectorCustomPlugin.from_dict,
        validator=attr.validators.instance_of(PropConnectorCustomPlugin),
        metadata={AttrMeta.PROPERTY_NAME: "CustomPlugin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-plugin.html#cfn-kafkaconnect-connector-plugin-customplugin"""

@attr.s
class PropConnectorKafkaClusterClientAuthentication(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.KafkaClusterClientAuthentication"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html

    Property Document:
    
    - ``rp_AuthenticationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.KafkaClusterClientAuthentication"
    
    rp_AuthenticationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AuthenticationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkaclusterclientauthentication.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication-authenticationtype"""

@attr.s
class PropConnectorApacheKafkaCluster(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.ApacheKafkaCluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html

    Property Document:
    
    - ``rp_BootstrapServers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers
    - ``rp_Vpc``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-vpc
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.ApacheKafkaCluster"
    
    rp_BootstrapServers: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BootstrapServers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-bootstrapservers"""
    rp_Vpc: typing.Union['PropConnectorVpc', dict] = attr.ib(
        default=None,
        converter=PropConnectorVpc.from_dict,
        validator=attr.validators.instance_of(PropConnectorVpc),
        metadata={AttrMeta.PROPERTY_NAME: "Vpc"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-apachekafkacluster.html#cfn-kafkaconnect-connector-apachekafkacluster-vpc"""

@attr.s
class PropConnectorAutoScaling(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.AutoScaling"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html

    Property Document:
    
    - ``rp_MaxWorkerCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-maxworkercount
    - ``rp_McuCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-mcucount
    - ``rp_MinWorkerCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-minworkercount
    - ``rp_ScaleInPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy
    - ``rp_ScaleOutPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.AutoScaling"
    
    rp_MaxWorkerCount: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MaxWorkerCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-maxworkercount"""
    rp_McuCount: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "McuCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-mcucount"""
    rp_MinWorkerCount: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "MinWorkerCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-minworkercount"""
    rp_ScaleInPolicy: typing.Union['PropConnectorScaleInPolicy', dict] = attr.ib(
        default=None,
        converter=PropConnectorScaleInPolicy.from_dict,
        validator=attr.validators.instance_of(PropConnectorScaleInPolicy),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleInPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleinpolicy"""
    rp_ScaleOutPolicy: typing.Union['PropConnectorScaleOutPolicy', dict] = attr.ib(
        default=None,
        converter=PropConnectorScaleOutPolicy.from_dict,
        validator=attr.validators.instance_of(PropConnectorScaleOutPolicy),
        metadata={AttrMeta.PROPERTY_NAME: "ScaleOutPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-autoscaling.html#cfn-kafkaconnect-connector-autoscaling-scaleoutpolicy"""

@attr.s
class PropConnectorCapacity(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.Capacity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html

    Property Document:
    
    - ``p_AutoScaling``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-autoscaling
    - ``p_ProvisionedCapacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-provisionedcapacity
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.Capacity"
    
    p_AutoScaling: typing.Union['PropConnectorAutoScaling', dict] = attr.ib(
        default=None,
        converter=PropConnectorAutoScaling.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorAutoScaling)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScaling"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-autoscaling"""
    p_ProvisionedCapacity: typing.Union['PropConnectorProvisionedCapacity', dict] = attr.ib(
        default=None,
        converter=PropConnectorProvisionedCapacity.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorProvisionedCapacity)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedCapacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-capacity.html#cfn-kafkaconnect-connector-capacity-provisionedcapacity"""

@attr.s
class PropConnectorWorkerLogDelivery(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.WorkerLogDelivery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html

    Property Document:
    
    - ``p_CloudWatchLogs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs
    - ``p_Firehose``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-firehose
    - ``p_S3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-s3
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.WorkerLogDelivery"
    
    p_CloudWatchLogs: typing.Union['PropConnectorCloudWatchLogsLogDelivery', dict] = attr.ib(
        default=None,
        converter=PropConnectorCloudWatchLogsLogDelivery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorCloudWatchLogsLogDelivery)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs"""
    p_Firehose: typing.Union['PropConnectorFirehoseLogDelivery', dict] = attr.ib(
        default=None,
        converter=PropConnectorFirehoseLogDelivery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorFirehoseLogDelivery)),
        metadata={AttrMeta.PROPERTY_NAME: "Firehose"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-firehose"""
    p_S3: typing.Union['PropConnectorS3LogDelivery', dict] = attr.ib(
        default=None,
        converter=PropConnectorS3LogDelivery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorS3LogDelivery)),
        metadata={AttrMeta.PROPERTY_NAME: "S3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-workerlogdelivery.html#cfn-kafkaconnect-connector-workerlogdelivery-s3"""

@attr.s
class PropConnectorKafkaCluster(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.KafkaCluster"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html

    Property Document:
    
    - ``rp_ApacheKafkaCluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html#cfn-kafkaconnect-connector-kafkacluster-apachekafkacluster
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.KafkaCluster"
    
    rp_ApacheKafkaCluster: typing.Union['PropConnectorApacheKafkaCluster', dict] = attr.ib(
        default=None,
        converter=PropConnectorApacheKafkaCluster.from_dict,
        validator=attr.validators.instance_of(PropConnectorApacheKafkaCluster),
        metadata={AttrMeta.PROPERTY_NAME: "ApacheKafkaCluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-kafkacluster.html#cfn-kafkaconnect-connector-kafkacluster-apachekafkacluster"""

@attr.s
class PropConnectorLogDelivery(Property):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector.LogDelivery"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html

    Property Document:
    
    - ``rp_WorkerLogDelivery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector.LogDelivery"
    
    rp_WorkerLogDelivery: typing.Union['PropConnectorWorkerLogDelivery', dict] = attr.ib(
        default=None,
        converter=PropConnectorWorkerLogDelivery.from_dict,
        validator=attr.validators.instance_of(PropConnectorWorkerLogDelivery),
        metadata={AttrMeta.PROPERTY_NAME: "WorkerLogDelivery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kafkaconnect-connector-logdelivery.html#cfn-kafkaconnect-connector-logdelivery-workerlogdelivery"""


#--- Resource declaration ---

@attr.s
class Connector(Resource):
    """
    AWS Object Type = "AWS::KafkaConnect::Connector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html

    Property Document:
    
    - ``rp_Capacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity
    - ``rp_ConnectorConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration
    - ``rp_ConnectorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname
    - ``rp_KafkaCluster``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster
    - ``rp_KafkaClusterClientAuthentication``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication
    - ``rp_KafkaClusterEncryptionInTransit``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit
    - ``rp_KafkaConnectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion
    - ``rp_Plugins``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins
    - ``rp_ServiceExecutionRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn
    - ``p_ConnectorDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription
    - ``p_LogDelivery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery
    - ``p_WorkerConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KafkaConnect::Connector"

    
    rp_Capacity: typing.Union['PropConnectorCapacity', dict] = attr.ib(
        default=None,
        converter=PropConnectorCapacity.from_dict,
        validator=attr.validators.instance_of(PropConnectorCapacity),
        metadata={AttrMeta.PROPERTY_NAME: "Capacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-capacity"""
    rp_ConnectorConfiguration: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorconfiguration"""
    rp_ConnectorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectorname"""
    rp_KafkaCluster: typing.Union['PropConnectorKafkaCluster', dict] = attr.ib(
        default=None,
        converter=PropConnectorKafkaCluster.from_dict,
        validator=attr.validators.instance_of(PropConnectorKafkaCluster),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaCluster"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkacluster"""
    rp_KafkaClusterClientAuthentication: typing.Union['PropConnectorKafkaClusterClientAuthentication', dict] = attr.ib(
        default=None,
        converter=PropConnectorKafkaClusterClientAuthentication.from_dict,
        validator=attr.validators.instance_of(PropConnectorKafkaClusterClientAuthentication),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaClusterClientAuthentication"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterclientauthentication"""
    rp_KafkaClusterEncryptionInTransit: typing.Union['PropConnectorKafkaClusterEncryptionInTransit', dict] = attr.ib(
        default=None,
        converter=PropConnectorKafkaClusterEncryptionInTransit.from_dict,
        validator=attr.validators.instance_of(PropConnectorKafkaClusterEncryptionInTransit),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaClusterEncryptionInTransit"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaclusterencryptionintransit"""
    rp_KafkaConnectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KafkaConnectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-kafkaconnectversion"""
    rp_Plugins: typing.List[typing.Union['PropConnectorPlugin', dict]] = attr.ib(
        default=None,
        converter=PropConnectorPlugin.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConnectorPlugin), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Plugins"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-plugins"""
    rp_ServiceExecutionRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceExecutionRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-serviceexecutionrolearn"""
    p_ConnectorDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-connectordescription"""
    p_LogDelivery: typing.Union['PropConnectorLogDelivery', dict] = attr.ib(
        default=None,
        converter=PropConnectorLogDelivery.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorLogDelivery)),
        metadata={AttrMeta.PROPERTY_NAME: "LogDelivery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-logdelivery"""
    p_WorkerConfiguration: typing.Union['PropConnectorWorkerConfiguration', dict] = attr.ib(
        default=None,
        converter=PropConnectorWorkerConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorWorkerConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkerConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#cfn-kafkaconnect-connector-workerconfiguration"""

    
    @property
    def rv_ConnectorArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kafkaconnect-connector.html#aws-resource-kafkaconnect-connector-return-values"""
        return GetAtt(resource=self, attr_name="ConnectorArn")
    
