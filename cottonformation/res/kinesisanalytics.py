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
class PropApplicationOutputKinesisFirehoseOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput.KinesisFirehoseOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput.KinesisFirehoseOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn"""

@attr.s
class PropApplicationCSVMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.CSVMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html

    Property Document:
    
    - ``rp_RecordColumnDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter
    - ``rp_RecordRowDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.CSVMappingParameters"
    
    rp_RecordColumnDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumnDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter"""
    rp_RecordRowDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter"""

@attr.s
class PropApplicationReferenceDataSourceCSVMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.CSVMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html

    Property Document:
    
    - ``rp_RecordColumnDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
    - ``rp_RecordRowDelimiter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.CSVMappingParameters"
    
    rp_RecordColumnDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumnDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter"""
    rp_RecordRowDelimiter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowDelimiter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter"""

@attr.s
class PropApplicationJSONMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.JSONMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html

    Property Document:
    
    - ``rp_RecordRowPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.JSONMappingParameters"
    
    rp_RecordRowPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath"""

@attr.s
class PropApplicationReferenceDataSourceS3ReferenceDataSource(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.S3ReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html

    Property Document:
    
    - ``rp_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-bucketarn
    - ``rp_FileKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-filekey
    - ``rp_ReferenceRoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-referencerolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.S3ReferenceDataSource"
    
    rp_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-bucketarn"""
    rp_FileKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FileKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-filekey"""
    rp_ReferenceRoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceRoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-referencerolearn"""

@attr.s
class PropApplicationOutputKinesisStreamsOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput.KinesisStreamsOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput.KinesisStreamsOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn"""

@attr.s
class PropApplicationKinesisStreamsInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.KinesisStreamsInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.KinesisStreamsInput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-rolearn"""

@attr.s
class PropApplicationRecordColumn(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.RecordColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-name
    - ``rp_SqlType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-sqltype
    - ``p_Mapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-mapping
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.RecordColumn"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-name"""
    rp_SqlType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SqlType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-sqltype"""
    p_Mapping: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-mapping"""

@attr.s
class PropApplicationReferenceDataSourceRecordColumn(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name
    - ``rp_SqlType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype
    - ``p_Mapping``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordColumn"
    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name"""
    rp_SqlType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SqlType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype"""
    p_Mapping: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mapping"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping"""

@attr.s
class PropApplicationKinesisFirehoseInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.KinesisFirehoseInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.KinesisFirehoseInput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-rolearn"""

@attr.s
class PropApplicationInputParallelism(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.InputParallelism"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html

    Property Document:
    
    - ``p_Count``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html#cfn-kinesisanalytics-application-inputparallelism-count
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.InputParallelism"
    
    p_Count: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Count"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html#cfn-kinesisanalytics-application-inputparallelism-count"""

@attr.s
class PropApplicationOutputLambdaOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput.LambdaOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput.LambdaOutput"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-rolearn"""

@attr.s
class PropApplicationOutputDestinationSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput.DestinationSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html

    Property Document:
    
    - ``p_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput.DestinationSchema"
    
    p_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype"""

@attr.s
class PropApplicationMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['PropApplicationCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['PropApplicationJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-jsonmappingparameters"""

@attr.s
class PropApplicationReferenceDataSourceJSONMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.JSONMappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html

    Property Document:
    
    - ``rp_RecordRowPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters-recordrowpath
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.JSONMappingParameters"
    
    rp_RecordRowPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordRowPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters-recordrowpath"""

@attr.s
class PropApplicationRecordFormat(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.RecordFormat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html

    Property Document:
    
    - ``rp_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-recordformattype
    - ``p_MappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-mappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.RecordFormat"
    
    rp_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-recordformattype"""
    p_MappingParameters: typing.Union['PropApplicationMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-mappingparameters"""

@attr.s
class PropApplicationInputLambdaProcessor(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.InputLambdaProcessor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html

    Property Document:
    
    - ``rp_ResourceARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.InputLambdaProcessor"
    
    rp_ResourceARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn"""

@attr.s
class PropApplicationOutputOutput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput.Output"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html

    Property Document:
    
    - ``rp_DestinationSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-destinationschema
    - ``p_KinesisFirehoseOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisfirehoseoutput
    - ``p_KinesisStreamsOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisstreamsoutput
    - ``p_LambdaOutput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-lambdaoutput
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-name
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput.Output"
    
    rp_DestinationSchema: typing.Union['PropApplicationOutputDestinationSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputDestinationSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationOutputDestinationSchema),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-destinationschema"""
    p_KinesisFirehoseOutput: typing.Union['PropApplicationOutputKinesisFirehoseOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputKinesisFirehoseOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputKinesisFirehoseOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisfirehoseoutput"""
    p_KinesisStreamsOutput: typing.Union['PropApplicationOutputKinesisStreamsOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputKinesisStreamsOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputKinesisStreamsOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisstreamsoutput"""
    p_LambdaOutput: typing.Union['PropApplicationOutputLambdaOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputLambdaOutput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationOutputLambdaOutput)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaOutput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-lambdaoutput"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-name"""

@attr.s
class PropApplicationInputSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.InputSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.InputSchema"
    
    rp_RecordColumns: typing.List[typing.Union['PropApplicationRecordColumn', dict]] = attr.ib(
        default=None,
        converter=PropApplicationRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordcolumns"""
    rp_RecordFormat: typing.Union['PropApplicationRecordFormat', dict] = attr.ib(
        default=None,
        converter=PropApplicationRecordFormat.from_dict,
        validator=attr.validators.instance_of(PropApplicationRecordFormat),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordformat"""
    p_RecordEncoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordEncoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordencoding"""

@attr.s
class PropApplicationReferenceDataSourceMappingParameters(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.MappingParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html

    Property Document:
    
    - ``p_CSVMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-csvmappingparameters
    - ``p_JSONMappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-jsonmappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.MappingParameters"
    
    p_CSVMappingParameters: typing.Union['PropApplicationReferenceDataSourceCSVMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceCSVMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceCSVMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "CSVMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-csvmappingparameters"""
    p_JSONMappingParameters: typing.Union['PropApplicationReferenceDataSourceJSONMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceJSONMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceJSONMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "JSONMappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-jsonmappingparameters"""

@attr.s
class PropApplicationInputProcessingConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.InputProcessingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html

    Property Document:
    
    - ``p_InputLambdaProcessor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.InputProcessingConfiguration"
    
    p_InputLambdaProcessor: typing.Union['PropApplicationInputLambdaProcessor', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputLambdaProcessor.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputLambdaProcessor)),
        metadata={AttrMeta.PROPERTY_NAME: "InputLambdaProcessor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor"""

@attr.s
class PropApplicationInput(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application.Input"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html

    Property Document:
    
    - ``rp_InputSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputschema
    - ``rp_NamePrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-nameprefix
    - ``p_InputParallelism``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputparallelism
    - ``p_InputProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputprocessingconfiguration
    - ``p_KinesisFirehoseInput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisfirehoseinput
    - ``p_KinesisStreamsInput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisstreamsinput
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application.Input"
    
    rp_InputSchema: typing.Union['PropApplicationInputSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationInputSchema),
        metadata={AttrMeta.PROPERTY_NAME: "InputSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputschema"""
    rp_NamePrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NamePrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-nameprefix"""
    p_InputParallelism: typing.Union['PropApplicationInputParallelism', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputParallelism.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputParallelism)),
        metadata={AttrMeta.PROPERTY_NAME: "InputParallelism"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputparallelism"""
    p_InputProcessingConfiguration: typing.Union['PropApplicationInputProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropApplicationInputProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInputProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "InputProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputprocessingconfiguration"""
    p_KinesisFirehoseInput: typing.Union['PropApplicationKinesisFirehoseInput', dict] = attr.ib(
        default=None,
        converter=PropApplicationKinesisFirehoseInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationKinesisFirehoseInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisfirehoseinput"""
    p_KinesisStreamsInput: typing.Union['PropApplicationKinesisStreamsInput', dict] = attr.ib(
        default=None,
        converter=PropApplicationKinesisStreamsInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationKinesisStreamsInput)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamsInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisstreamsinput"""

@attr.s
class PropApplicationReferenceDataSourceRecordFormat(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordFormat"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html

    Property Document:
    
    - ``rp_RecordFormatType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-recordformattype
    - ``p_MappingParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-mappingparameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.RecordFormat"
    
    rp_RecordFormatType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormatType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-recordformattype"""
    p_MappingParameters: typing.Union['PropApplicationReferenceDataSourceMappingParameters', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceMappingParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceMappingParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "MappingParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-mappingparameters"""

@attr.s
class PropApplicationReferenceDataSourceReferenceSchema(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceSchema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html

    Property Document:
    
    - ``rp_RecordColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns
    - ``rp_RecordFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat
    - ``p_RecordEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceSchema"
    
    rp_RecordColumns: typing.List[typing.Union['PropApplicationReferenceDataSourceRecordColumn', dict]] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceRecordColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationReferenceDataSourceRecordColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns"""
    rp_RecordFormat: typing.Union['PropApplicationReferenceDataSourceRecordFormat', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceRecordFormat.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceRecordFormat),
        metadata={AttrMeta.PROPERTY_NAME: "RecordFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat"""
    p_RecordEncoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RecordEncoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding"""

@attr.s
class PropApplicationReferenceDataSourceReferenceDataSource(Property):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html

    Property Document:
    
    - ``rp_ReferenceSchema``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-referenceschema
    - ``p_S3ReferenceDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-s3referencedatasource
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-tablename
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource"
    
    rp_ReferenceSchema: typing.Union['PropApplicationReferenceDataSourceReferenceSchema', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceReferenceSchema.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceReferenceSchema),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceSchema"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-referenceschema"""
    p_S3ReferenceDataSource: typing.Union['PropApplicationReferenceDataSourceS3ReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceS3ReferenceDataSource.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationReferenceDataSourceS3ReferenceDataSource)),
        metadata={AttrMeta.PROPERTY_NAME: "S3ReferenceDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-s3referencedatasource"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-tablename"""


#--- Resource declaration ---

@attr.s
class ApplicationOutput(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationOutput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname
    - ``rp_Output``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationOutput"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname"""
    rp_Output: typing.Union['PropApplicationOutputOutput', dict] = attr.ib(
        default=None,
        converter=PropApplicationOutputOutput.from_dict,
        validator=attr.validators.instance_of(PropApplicationOutputOutput),
        metadata={AttrMeta.PROPERTY_NAME: "Output"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output"""

    

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalytics::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html

    Property Document:
    
    - ``rp_Inputs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs
    - ``p_ApplicationCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode
    - ``p_ApplicationDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription
    - ``p_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::Application"

    
    rp_Inputs: typing.List[typing.Union['PropApplicationInput', dict]] = attr.ib(
        default=None,
        converter=PropApplicationInput.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropApplicationInput), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Inputs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs"""
    p_ApplicationCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode"""
    p_ApplicationDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription"""
    p_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname"""

    

@attr.s
class ApplicationReferenceDataSource(Resource):
    """
    AWS Object Type = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html

    Property Document:
    
    - ``rp_ApplicationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname
    - ``rp_ReferenceDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource
    """
    AWS_OBJECT_TYPE = "AWS::KinesisAnalytics::ApplicationReferenceDataSource"

    
    rp_ApplicationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname"""
    rp_ReferenceDataSource: typing.Union['PropApplicationReferenceDataSourceReferenceDataSource', dict] = attr.ib(
        default=None,
        converter=PropApplicationReferenceDataSourceReferenceDataSource.from_dict,
        validator=attr.validators.instance_of(PropApplicationReferenceDataSourceReferenceDataSource),
        metadata={AttrMeta.PROPERTY_NAME: "ReferenceDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource"""

    
