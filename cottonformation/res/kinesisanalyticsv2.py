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
class ApplicationReferenceDataSourceRecordColumn(Property):
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
class ApplicationS3ContentLocation(Property):
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
class ApplicationPropertyGroup(Property):
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
class ApplicationInputParallelism(Property):
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
class ApplicationOutputKinesisFirehoseOutput(Property):
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
class ApplicationOutputKinesisStreamsOutput(Property):
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
class ApplicationApplicationSnapshotConfiguration(Property):
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
class ApplicationKinesisFirehoseInput(Property):
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
class ApplicationParallelismConfiguration(Property):
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
class ApplicationMonitoringConfiguration(Property):
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
class ApplicationOutputDestinationSchema(Property):
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
class ApplicationCustomArtifactsConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CustomArtifactsConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactsconfiguration.html

    Property Document:
    
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CustomArtifactsConfiguration"
    

@attr.s
class ApplicationOutputLambdaOutput(Property):
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
class ApplicationReferenceDataSourceJSONMappingParameters(Property):
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
class ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption(Property):
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
class ApplicationMavenReference(Property):
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
class ApplicationKinesisStreamsInput(Property):
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
class ApplicationCheckpointConfiguration(Property):
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
class ApplicationZeppelinMonitoringConfiguration(Property):
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
class ApplicationS3ContentBaseLocation(Property):
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
class ApplicationInputLambdaProcessor(Property):
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
class ApplicationRecordColumn(Property):
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
class ApplicationCSVMappingParameters(Property):
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
class ApplicationGlueDataCatalogConfiguration(Property):
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
class ApplicationJSONMappingParameters(Property):
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
class ApplicationCodeContent(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CodeContent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html

    Property Document:
    
    - ``p_S3ContentLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation
    - ``p_TextContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent
    - ``p_ZipFileContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CodeContent"
    
    p_S3ContentLocation: typing.Union['ApplicationS3ContentLocation', dict] = attr.ib(
        default=None,
        converter=ApplicationS3ContentLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationS3ContentLocation)),
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
class ApplicationReferenceDataSourceS3ReferenceDataSource(Property):
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
class ApplicationEnvironmentProperties(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.EnvironmentProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html

    Property Document:
    
    - ``p_PropertyGroups``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.EnvironmentProperties"
    
    p_PropertyGroups: typing.List[typing.Union['ApplicationPropertyGroup', dict]] = attr.ib(
        default=None,
        converter=ApplicationPropertyGroup.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationPropertyGroup), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "PropertyGroups"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups"""

@attr.s
class ApplicationCatalogConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.CatalogConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html

    Property Document:
    
    - ``p_GlueDataCatalogConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.CatalogConfiguration"
    
    p_GlueDataCatalogConfiguration: typing.Union['ApplicationGlueDataCatalogConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationGlueDataCatalogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationGlueDataCatalogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "GlueDataCatalogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration"""

@attr.s
class ApplicationReferenceDataSourceCSVMappingParameters(Property):
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
class ApplicationCustomArtifactConfiguration(Property):
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
    p_MavenReference: typing.Union['ApplicationMavenReference', dict] = attr.ib(
        default=None,
        converter=ApplicationMavenReference.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationMavenReference)),
        metadata={AttrMeta.PROPERTY_NAME: "MavenReference"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference"""
    p_S3ContentLocation: typing.Union['ApplicationS3ContentLocation', dict] = attr.ib(
        default=None,
        converter=ApplicationS3ContentLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationS3ContentLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ContentLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation"""

@attr.s
class ApplicationDeployAsApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html

    Property Document:
    
    - ``rp_S3ContentLocation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.DeployAsApplicationConfiguration"
    
    rp_S3ContentLocation: typing.Union['ApplicationS3ContentBaseLocation', dict] = attr.ib(
        default=None,
        converter=ApplicationS3ContentBaseLocation.from_dict,
        validator=attr.validators.instance_of(ApplicationS3ContentBaseLocation),
        metadata={AttrMeta.PROPERTY_NAME: "S3ContentLocation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation"""

@attr.s
class ApplicationMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['ApplicationCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['ApplicationJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters"""

@attr.s
class ApplicationFlinkApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html

    Property Document:
    
    - ``p_CheckpointConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration
    - ``p_MonitoringConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration
    - ``p_ParallelismConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.FlinkApplicationConfiguration"
    
    p_CheckpointConfiguration: typing.Union['ApplicationCheckpointConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationCheckpointConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationCheckpointConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CheckpointConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration"""
    p_MonitoringConfiguration: typing.Union['ApplicationMonitoringConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationMonitoringConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationMonitoringConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitoringConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration"""
    p_ParallelismConfiguration: typing.Union['ApplicationParallelismConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationParallelismConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationParallelismConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ParallelismConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration"""

@attr.s
class ApplicationOutputOutput(Property):
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
    
    rp_DestinationSchema: typing.Union['ApplicationOutputDestinationSchema', dict] = attr.ib(
        default=None,
        converter=ApplicationOutputDestinationSchema.from_dict,
        validator=attr.validators.instance_of(ApplicationOutputDestinationSchema),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema"""
    p_KinesisFirehoseOutput: typing.Union['ApplicationOutputKinesisFirehoseOutput', dict] = attr.ib(
        default=None,
        converter=ApplicationOutputKinesisFirehoseOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationOutputKinesisFirehoseOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput"""
    p_KinesisStreamsOutput: typing.Union['ApplicationOutputKinesisStreamsOutput', dict] = attr.ib(
        default=None,
        converter=ApplicationOutputKinesisStreamsOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationOutputKinesisStreamsOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput"""
    p_LambdaOutput: typing.Union['ApplicationOutputLambdaOutput', dict] = attr.ib(
        default=None,
        converter=ApplicationOutputLambdaOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationOutputLambdaOutput)),
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
class ApplicationInputProcessingConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html

    Property Document:
    
    - ``p_InputLambdaProcessor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputProcessingConfiguration"
    
    p_InputLambdaProcessor: typing.Union['ApplicationInputLambdaProcessor', dict] = attr.ib(
        default=None,
        converter=ApplicationInputLambdaProcessor.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationInputLambdaProcessor)),
        metadata={AttrMeta.PROPERTY_NAME: "InputLambdaProcessor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor"""

@attr.s
class ApplicationApplicationCodeConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html

    Property Document:
    
    - ``rp_CodeContent``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent
    - ``rp_CodeContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.ApplicationCodeConfiguration"
    
    rp_CodeContent: typing.Union['ApplicationCodeContent', dict] = attr.ib(
        default=None,
        converter=ApplicationCodeContent.from_dict,
        validator=attr.validators.instance_of(ApplicationCodeContent),
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
class ApplicationZeppelinApplicationConfiguration(Property):
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
    
    p_CatalogConfiguration: typing.Union['ApplicationCatalogConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationCatalogConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationCatalogConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration"""
    p_CustomArtifactsConfiguration: typing.Union['ApplicationCustomArtifactsConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationCustomArtifactsConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationCustomArtifactsConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomArtifactsConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration"""
    p_DeployAsApplicationConfiguration: typing.Union['ApplicationDeployAsApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationDeployAsApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationDeployAsApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DeployAsApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration"""
    p_MonitoringConfiguration: typing.Union['ApplicationZeppelinMonitoringConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationZeppelinMonitoringConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationZeppelinMonitoringConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "MonitoringConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration"""

@attr.s
class ApplicationReferenceDataSourceMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['ApplicationReferenceDataSourceCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationReferenceDataSourceCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['ApplicationReferenceDataSourceJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationReferenceDataSourceJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters"""

@attr.s
class ApplicationRecordFormat(Property):
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
    p_MappingParameters: typing.Union['ApplicationMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters"""

@attr.s
class ApplicationReferenceDataSourceRecordFormat(Property):
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
    p_MappingParameters: typing.Union['ApplicationReferenceDataSourceMappingParameters', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationReferenceDataSourceMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters"""

@attr.s
class ApplicationInputSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.InputSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.InputSchema"
    
    rp_RecordColumns: typing.List[typing.Union['ApplicationRecordColumn', dict]] = attr.ib(
        default=None,
        converter=ApplicationRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns"""
    rp_RecordFormat: typing.Union['ApplicationRecordFormat', dict] = attr.ib(
        default=None,
        converter=ApplicationRecordFormat.from_dict,
        validator=attr.validators.instance_of(ApplicationRecordFormat),
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
class ApplicationReferenceDataSourceReferenceSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceSchema"
    
    rp_RecordColumns: typing.List[typing.Union['ApplicationReferenceDataSourceRecordColumn', dict]] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationReferenceDataSourceRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns"""
    rp_RecordFormat: typing.Union['ApplicationReferenceDataSourceRecordFormat', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceRecordFormat.from_dict,
        validator=attr.validators.instance_of(ApplicationReferenceDataSourceRecordFormat),
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
class ApplicationInput(Property):
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
    
    rp_InputSchema: typing.Union['ApplicationInputSchema', dict] = attr.ib(
        default=None,
        converter=ApplicationInputSchema.from_dict,
        validator=attr.validators.instance_of(ApplicationInputSchema),
        metadata={AttrMeta.PROPERTY_NAME: "InputSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema"""
    rp_NamePrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NamePrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix"""
    p_InputParallelism: typing.Union['ApplicationInputParallelism', dict] = attr.ib(
        default=None,
        converter=ApplicationInputParallelism.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationInputParallelism)),
        metadata={AttrMeta.PROPERTY_NAME: "InputParallelism"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism"""
    p_InputProcessingConfiguration: typing.Union['ApplicationInputProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationInputProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationInputProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "InputProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration"""
    p_KinesisFirehoseInput: typing.Union['ApplicationKinesisFirehoseInput', dict] = attr.ib(
        default=None,
        converter=ApplicationKinesisFirehoseInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationKinesisFirehoseInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput"""
    p_KinesisStreamsInput: typing.Union['ApplicationKinesisStreamsInput', dict] = attr.ib(
        default=None,
        converter=ApplicationKinesisStreamsInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationKinesisStreamsInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput"""

@attr.s
class ApplicationSqlApplicationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html

    Property Document:
    
    - ``p_Inputs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::Application.SqlApplicationConfiguration"
    
    p_Inputs: typing.List[typing.Union['ApplicationInput', dict]] = attr.ib(
        default=None,
        converter=ApplicationInput.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationInput), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Inputs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs"""

@attr.s
class ApplicationReferenceDataSourceReferenceDataSource(Property):
    """
    AWS Object Type = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html

    Property Document:
    
    - ``rp_ReferenceSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema
    - ``p_S3ReferenceDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource"
    
    rp_ReferenceSchema: typing.Union['ApplicationReferenceDataSourceReferenceSchema', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceReferenceSchema.from_dict,
        validator=attr.validators.instance_of(ApplicationReferenceDataSourceReferenceSchema),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema"""
    p_S3ReferenceDataSource: typing.Union['ApplicationReferenceDataSourceS3ReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceS3ReferenceDataSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationReferenceDataSourceS3ReferenceDataSource)),
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
class ApplicationApplicationConfiguration(Property):
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
    
    p_ApplicationCodeConfiguration: typing.Union['ApplicationApplicationCodeConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationApplicationCodeConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationApplicationCodeConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationCodeConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration"""
    p_ApplicationSnapshotConfiguration: typing.Union['ApplicationApplicationSnapshotConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationApplicationSnapshotConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationApplicationSnapshotConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationSnapshotConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration"""
    p_EnvironmentProperties: typing.Union['ApplicationEnvironmentProperties', dict] = attr.ib(
        default=None,
        converter=ApplicationEnvironmentProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationEnvironmentProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "EnvironmentProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties"""
    p_FlinkApplicationConfiguration: typing.Union['ApplicationFlinkApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationFlinkApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationFlinkApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "FlinkApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration"""
    p_SqlApplicationConfiguration: typing.Union['ApplicationSqlApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationSqlApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationSqlApplicationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SqlApplicationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration"""
    p_ZeppelinApplicationConfiguration: typing.Union['ApplicationZeppelinApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationZeppelinApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationZeppelinApplicationConfiguration)),
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
    rp_CloudWatchLoggingOption: typing.Union['ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption', dict] = attr.ib(
        default=None,
        converter=ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption.from_dict,
        validator=attr.validators.instance_of(ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption),
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
    p_ApplicationConfiguration: typing.Union['ApplicationApplicationConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationApplicationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationApplicationConfiguration)),
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
    rp_Output: typing.Union['ApplicationOutputOutput', dict] = attr.ib(
        default=None,
        converter=ApplicationOutputOutput.from_dict,
        validator=attr.validators.instance_of(ApplicationOutputOutput),
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
    rp_ReferenceDataSource: typing.Union['ApplicationReferenceDataSourceReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=ApplicationReferenceDataSourceReferenceDataSource.from_dict,
        validator=attr.validators.instance_of(ApplicationReferenceDataSourceReferenceDataSource),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource"""

    
