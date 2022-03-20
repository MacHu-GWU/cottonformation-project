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
class PropApplicationReferenceDataSourceRecordColumn(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name
    - ``rp_SqlType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype
    - ``p_Mapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordColumn"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name"""
    rp_SqlType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SqlType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype"""
    p_Mapping: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping"""

@attr.s
class PropApplicationS3ContentLocation(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.S3ContentLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html

    Property Document:
    
    - ``p_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn
    - ``p_FileKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey
    - ``p_ObjectVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.S3ContentLocation"
    
    p_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn"""
    p_FileKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FileKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey"""
    p_ObjectVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion"""

@attr.s
class PropApplicationPropertyGroup(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.PropertyGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html

    Property Document:
    
    - ``p_PropertyGroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid
    - ``p_PropertyMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.PropertyGroup"
    
    p_PropertyGroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PropertyGroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid"""
    p_PropertyMap: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "PropertyMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap"""

@attr.s
class PropApplicationInputParallelism(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputParallelism"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html

    Property Document:
    
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputParallelism"
    
    p_Count: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count"""

@attr.s
class PropApplicationOutputKinesisFirehoseOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisFirehoseOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisFirehoseOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn"""

@attr.s
class PropApplicationOutputKinesisStreamsOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisStreamsOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput.KinesisStreamsOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn"""

@attr.s
class PropApplicationApplicationSnapshotConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html

    Property Document:
    
    - ``rp_SnapshotsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ApplicationSnapshotConfiguration"
    
    rp_SnapshotsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled"""

@attr.s
class PropApplicationKinesisFirehoseInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.KinesisFirehoseInput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn"""

@attr.s
class PropApplicationParallelismConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html

    Property Document:
    
    - ``rp_ConfigurationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype
    - ``p_AutoScalingEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled
    - ``p_Parallelism``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism
    - ``p_ParallelismPerKPU``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ParallelismConfiguration"
    
    rp_ConfigurationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype"""
    p_AutoScalingEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoScalingEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled"""
    p_Parallelism: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Parallelism"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism"""
    p_ParallelismPerKPU: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ParallelismPerKPU"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu"""

@attr.s
class PropApplicationMonitoringConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html

    Property Document:
    
    - ``rp_ConfigurationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype
    - ``p_LogLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel
    - ``p_MetricsLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.MonitoringConfiguration"
    
    rp_ConfigurationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype"""
    p_LogLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel"""
    p_MetricsLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MetricsLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel"""

@attr.s
class PropApplicationOutputDestinationSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput.DestinationSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html

    Property Document:
    
    - ``p_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput.DestinationSchema"
    
    p_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype"""

@attr.s
class PropApplicationOutputLambdaOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput.LambdaOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput.LambdaOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn"""

@attr.s
class PropApplicationReferenceDataSourceJSONMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.JSONMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html

    Property Document:
    
    - ``rp_RecordRowPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.JSONMappingParameters"
    
    rp_RecordRowPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath"""

@attr.s
class PropApplicationCloudWatchLoggingOptionCloudWatchLoggingOption(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html

    Property Document:
    
    - ``rp_LogStreamARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption"
    
    rp_LogStreamARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogStreamARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn"""

@attr.s
class PropApplicationMavenReference(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.MavenReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html

    Property Document:
    
    - ``rp_ArtifactId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-artifactid
    - ``rp_GroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-groupid
    - ``rp_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-version
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.MavenReference"
    
    rp_ArtifactId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ArtifactId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-artifactid"""
    rp_GroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-groupid"""
    rp_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-version"""

@attr.s
class PropApplicationKinesisStreamsInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.KinesisStreamsInput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn"""

@attr.s
class PropApplicationCheckpointConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html

    Property Document:
    
    - ``rp_ConfigurationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype
    - ``p_CheckpointInterval``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval
    - ``p_CheckpointingEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled
    - ``p_MinPauseBetweenCheckpoints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CheckpointConfiguration"
    
    rp_ConfigurationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype"""
    p_CheckpointInterval: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "CheckpointInterval"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval"""
    p_CheckpointingEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CheckpointingEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled"""
    p_MinPauseBetweenCheckpoints: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinPauseBetweenCheckpoints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints"""

@attr.s
class PropApplicationZeppelinMonitoringConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ZeppelinMonitoringConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html

    Property Document:
    
    - ``p_LogLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration-loglevel
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ZeppelinMonitoringConfiguration"
    
    p_LogLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration-loglevel"""

@attr.s
class PropApplicationS3ContentBaseLocation(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.S3ContentBaseLocation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html

    Property Document:
    
    - ``rp_BasePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath
    - ``rp_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.S3ContentBaseLocation"
    
    rp_BasePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BasePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath"""
    rp_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn"""

@attr.s
class PropApplicationInputLambdaProcessor(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputLambdaProcessor"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn"""

@attr.s
class PropApplicationRecordColumn(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.RecordColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name
    - ``rp_SqlType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype
    - ``p_Mapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.RecordColumn"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name"""
    rp_SqlType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SqlType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype"""
    p_Mapping: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping"""

@attr.s
class PropApplicationCSVMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CSVMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html

    Property Document:
    
    - ``rp_RecordColumnDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter
    - ``rp_RecordRowDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CSVMappingParameters"
    
    rp_RecordColumnDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumnDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter"""
    rp_RecordRowDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter"""

@attr.s
class PropApplicationGlueDataCatalogConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.GlueDataCatalogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html

    Property Document:
    
    - ``p_DatabaseARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.GlueDataCatalogConfiguration"
    
    p_DatabaseARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn"""

@attr.s
class PropApplicationJSONMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.JSONMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html

    Property Document:
    
    - ``rp_RecordRowPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.JSONMappingParameters"
    
    rp_RecordRowPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath"""

@attr.s
class PropApplicationCodeContent(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CodeContent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html

    Property Document:
    
    - ``p_S3ContentLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation
    - ``p_TextContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent
    - ``p_ZipFileContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CodeContent"
    
    p_S3ContentLocation: typing.Union['PropApplicationS3ContentLocation', dict] = attr.ib(
        default=None,
        converter=PropApplicationS3ContentLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationS3ContentLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ContentLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation"""
    p_TextContent: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextContent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent"""
    p_ZipFileContent: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ZipFileContent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent"""

@attr.s
class PropApplicationReferenceDataSourceS3ReferenceDataSource(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.S3ReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html

    Property Document:
    
    - ``rp_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn
    - ``rp_FileKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.S3ReferenceDataSource"
    
    rp_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn"""
    rp_FileKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FileKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey"""

@attr.s
class PropApplicationEnvironmentProperties(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.EnvironmentProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html

    Property Document:
    
    - ``p_PropertyGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.EnvironmentProperties"
    
    p_PropertyGroups: typing.List[typing.Union['PropApplicationPropertyGroup', dict]] = attr.ib(
        default=None,
        converter=PropApplicationPropertyGroup.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationPropertyGroup), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PropertyGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups"""

@attr.s
class PropApplicationCatalogConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CatalogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html

    Property Document:
    
    - ``p_GlueDataCatalogConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CatalogConfiguration"
    
    p_GlueDataCatalogConfiguration: typing.Union['PropApplicationGlueDataCatalogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationGlueDataCatalogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationGlueDataCatalogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "GlueDataCatalogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration"""

@attr.s
class PropApplicationReferenceDataSourceCSVMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.CSVMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html

    Property Document:
    
    - ``rp_RecordColumnDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
    - ``rp_RecordRowDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.CSVMappingParameters"
    
    rp_RecordColumnDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumnDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter"""
    rp_RecordRowDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter"""

@attr.s
class PropApplicationCustomArtifactConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CustomArtifactConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html

    Property Document:
    
    - ``rp_ArtifactType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype
    - ``p_MavenReference``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference
    - ``p_S3ContentLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CustomArtifactConfiguration"
    
    rp_ArtifactType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ArtifactType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype"""
    p_MavenReference: typing.Union['PropApplicationMavenReference', dict] = attr.ib(
        default=None,
        converter=PropApplicationMavenReference.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMavenReference)),
        metadata={AttrMeta.PROPERTY_NAME: "MavenReference"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference"""
    p_S3ContentLocation: typing.Union['PropApplicationS3ContentLocation', dict] = attr.ib(
        default=None,
        converter=PropApplicationS3ContentLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationS3ContentLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ContentLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation"""

@attr.s
class PropApplicationDeployAsApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html

    Property Document:
    
    - ``rp_S3ContentLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration"
    
    rp_S3ContentLocation: typing.Union['PropApplicationS3ContentBaseLocation', dict] = attr.ib(
        default=None,
        converter=PropApplicationS3ContentBaseLocation.from_dict,
        validator=attr.validators.instance_of(PropApplicationS3ContentBaseLocation),
        metadata={AttrMeta.PROPERTY_NAME: "S3ContentLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation"""

@attr.s
class PropApplicationMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['PropApplicationCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['PropApplicationJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters"""

@attr.s
class PropApplicationFlinkApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html

    Property Document:
    
    - ``p_CheckpointConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration
    - ``p_MonitoringConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration
    - ``p_ParallelismConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration"
    
    p_CheckpointConfiguration: typing.Union['PropApplicationCheckpointConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationCheckpointConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationCheckpointConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CheckpointConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration"""
    p_MonitoringConfiguration: typing.Union['PropApplicationMonitoringConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationMonitoringConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMonitoringConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitoringConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration"""
    p_ParallelismConfiguration: typing.Union['PropApplicationParallelismConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationParallelismConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationParallelismConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ParallelismConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration"""

@attr.s
class PropApplicationOutputOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput.Output"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html

    Property Document:
    
    - ``rp_DestinationSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema
    - ``p_KinesisFirehoseOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput
    - ``p_KinesisStreamsOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput
    - ``p_LambdaOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput.Output"
    
    rp_DestinationSchema: typing.Union['PropApplicationOutputDestinationSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputDestinationSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationOutputDestinationSchema),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema"""
    p_KinesisFirehoseOutput: typing.Union['PropApplicationOutputKinesisFirehoseOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputKinesisFirehoseOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputKinesisFirehoseOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput"""
    p_KinesisStreamsOutput: typing.Union['PropApplicationOutputKinesisStreamsOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputKinesisStreamsOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputKinesisStreamsOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput"""
    p_LambdaOutput: typing.Union['PropApplicationOutputLambdaOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputLambdaOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputLambdaOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name"""

@attr.s
class PropApplicationInputProcessingConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html

    Property Document:
    
    - ``p_InputLambdaProcessor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration"
    
    p_InputLambdaProcessor: typing.Union['PropApplicationInputLambdaProcessor', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputLambdaProcessor.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputLambdaProcessor)),
        metadata={AttrMeta.PROPERTY_NAME: "InputLambdaProcessor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor"""

@attr.s
class PropApplicationApplicationCodeConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html

    Property Document:
    
    - ``rp_CodeContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent
    - ``rp_CodeContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration"
    
    rp_CodeContent: typing.Union['PropApplicationCodeContent', dict] = attr.ib(
        default=None,
        converter=PropApplicationCodeContent.from_dict,
        validator=attr.validators.instance_of(PropApplicationCodeContent),
        metadata={AttrMeta.PROPERTY_NAME: "CodeContent"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent"""
    rp_CodeContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CodeContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype"""

@attr.s
class PropApplicationZeppelinApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ZeppelinApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html

    Property Document:
    
    - ``p_CatalogConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration
    - ``p_CustomArtifactsConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration
    - ``p_DeployAsApplicationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration
    - ``p_MonitoringConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ZeppelinApplicationConfiguration"
    
    p_CatalogConfiguration: typing.Union['PropApplicationCatalogConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationCatalogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationCatalogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration"""
    p_CustomArtifactsConfiguration: typing.List[typing.Union['PropApplicationCustomArtifactConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropApplicationCustomArtifactConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationCustomArtifactConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomArtifactsConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration"""
    p_DeployAsApplicationConfiguration: typing.Union['PropApplicationDeployAsApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationDeployAsApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationDeployAsApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DeployAsApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration"""
    p_MonitoringConfiguration: typing.Union['PropApplicationZeppelinMonitoringConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationZeppelinMonitoringConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationZeppelinMonitoringConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitoringConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration"""

@attr.s
class PropApplicationReferenceDataSourceMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['PropApplicationReferenceDataSourceCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['PropApplicationReferenceDataSourceJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters"""

@attr.s
class PropApplicationRecordFormat(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.RecordFormat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html

    Property Document:
    
    - ``rp_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype
    - ``p_MappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.RecordFormat"
    
    rp_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype"""
    p_MappingParameters: typing.Union['PropApplicationMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters"""

@attr.s
class PropApplicationReferenceDataSourceRecordFormat(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordFormat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html

    Property Document:
    
    - ``rp_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype
    - ``p_MappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.RecordFormat"
    
    rp_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype"""
    p_MappingParameters: typing.Union['PropApplicationReferenceDataSourceMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters"""

@attr.s
class PropApplicationInputSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputSchema"
    
    rp_RecordColumns: typing.List[typing.Union['PropApplicationRecordColumn', dict]] = attr.ib(
        default=None,
        converter=PropApplicationRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns"""
    rp_RecordFormat: typing.Union['PropApplicationRecordFormat', dict] = attr.ib(
        default=None,
        converter=PropApplicationRecordFormat.from_dict,
        validator=attr.validators.instance_of(PropApplicationRecordFormat),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat"""
    p_RecordEncoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordEncoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding"""

@attr.s
class PropApplicationReferenceDataSourceReferenceSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema"
    
    rp_RecordColumns: typing.List[typing.Union['PropApplicationReferenceDataSourceRecordColumn', dict]] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationReferenceDataSourceRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns"""
    rp_RecordFormat: typing.Union['PropApplicationReferenceDataSourceRecordFormat', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceRecordFormat.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceRecordFormat),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat"""
    p_RecordEncoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordEncoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding"""

@attr.s
class PropApplicationInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.Input"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html

    Property Document:
    
    - ``rp_InputSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema
    - ``rp_NamePrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix
    - ``p_InputParallelism``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism
    - ``p_InputProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration
    - ``p_KinesisFirehoseInput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput
    - ``p_KinesisStreamsInput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.Input"
    
    rp_InputSchema: typing.Union['PropApplicationInputSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationInputSchema),
        metadata={AttrMeta.PROPERTY_NAME: "InputSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema"""
    rp_NamePrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NamePrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix"""
    p_InputParallelism: typing.Union['PropApplicationInputParallelism', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputParallelism.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputParallelism)),
        metadata={AttrMeta.PROPERTY_NAME: "InputParallelism"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism"""
    p_InputProcessingConfiguration: typing.Union['PropApplicationInputProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "InputProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration"""
    p_KinesisFirehoseInput: typing.Union['PropApplicationKinesisFirehoseInput', dict] = attr.ib(
        default=None,
        converter=PropApplicationKinesisFirehoseInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationKinesisFirehoseInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput"""
    p_KinesisStreamsInput: typing.Union['PropApplicationKinesisStreamsInput', dict] = attr.ib(
        default=None,
        converter=PropApplicationKinesisStreamsInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationKinesisStreamsInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput"""

@attr.s
class PropApplicationSqlApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html

    Property Document:
    
    - ``p_Inputs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration"
    
    p_Inputs: typing.List[typing.Union['PropApplicationInput', dict]] = attr.ib(
        default=None,
        converter=PropApplicationInput.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationInput), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Inputs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs"""

@attr.s
class PropApplicationReferenceDataSourceReferenceDataSource(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html

    Property Document:
    
    - ``rp_ReferenceSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema
    - ``p_S3ReferenceDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource"
    
    rp_ReferenceSchema: typing.Union['PropApplicationReferenceDataSourceReferenceSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceReferenceSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceReferenceSchema),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema"""
    p_S3ReferenceDataSource: typing.Union['PropApplicationReferenceDataSourceS3ReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceS3ReferenceDataSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceS3ReferenceDataSource)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ReferenceDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename"""

@attr.s
class PropApplicationApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html

    Property Document:
    
    - ``p_ApplicationCodeConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration
    - ``p_ApplicationSnapshotConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration
    - ``p_EnvironmentProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties
    - ``p_FlinkApplicationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration
    - ``p_SqlApplicationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration
    - ``p_ZeppelinApplicationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration"
    
    p_ApplicationCodeConfiguration: typing.Union['PropApplicationApplicationCodeConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationApplicationCodeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationApplicationCodeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationCodeConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration"""
    p_ApplicationSnapshotConfiguration: typing.Union['PropApplicationApplicationSnapshotConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationApplicationSnapshotConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationApplicationSnapshotConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationSnapshotConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration"""
    p_EnvironmentProperties: typing.Union['PropApplicationEnvironmentProperties', dict] = attr.ib(
        default=None,
        converter=PropApplicationEnvironmentProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationEnvironmentProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties"""
    p_FlinkApplicationConfiguration: typing.Union['PropApplicationFlinkApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationFlinkApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationFlinkApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "FlinkApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration"""
    p_SqlApplicationConfiguration: typing.Union['PropApplicationSqlApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationSqlApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationSqlApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SqlApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration"""
    p_ZeppelinApplicationConfiguration: typing.Union['PropApplicationZeppelinApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationZeppelinApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationZeppelinApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ZeppelinApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration"""


#--- Resource declaration ---

@attr.s
class ApplicationCloudWatchLoggingOption(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
    - ``rp_CloudWatchLoggingOption``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname"""
    rp_CloudWatchLoggingOption: typing.Union['PropApplicationCloudWatchLoggingOptionCloudWatchLoggingOption', dict] = attr.ib(
        default=None,
        converter=PropApplicationCloudWatchLoggingOptionCloudWatchLoggingOption.from_dict,
        validator=attr.validators.instance_of(PropApplicationCloudWatchLoggingOptionCloudWatchLoggingOption),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOption"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption"""

    

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html

    Property Document:
    
    - ``rp_RuntimeEnvironment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
    - ``rp_ServiceExecutionRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
    - ``p_ApplicationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
    - ``p_ApplicationDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
    - ``p_ApplicationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode
    - ``p_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application"

    
    rp_RuntimeEnvironment: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimeEnvironment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment"""
    rp_ServiceExecutionRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceExecutionRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole"""
    p_ApplicationConfiguration: typing.Union['PropApplicationApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration"""
    p_ApplicationDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription"""
    p_ApplicationMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode"""
    p_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags"""

    

@attr.s
class ApplicationOutput(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
    - ``rp_Output``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationOutput"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname"""
    rp_Output: typing.Union['PropApplicationOutputOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputOutput.from_dict,
        validator=attr.validators.instance_of(PropApplicationOutputOutput),
        metadata={AttrMeta.PROPERTY_NAME: "Output"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output"""

    

@attr.s
class ApplicationReferenceDataSource(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
    - ``rp_ReferenceDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname"""
    rp_ReferenceDataSource: typing.Union['PropApplicationReferenceDataSourceReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceReferenceDataSource.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceReferenceDataSource),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource"""

    
