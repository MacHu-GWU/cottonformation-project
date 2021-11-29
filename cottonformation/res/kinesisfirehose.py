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
class PropDeliveryStreamAmazonopensearchserviceRetryOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceRetryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html

    Property Document:
    
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceRetryOptions"
    
    p_DurationInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds"""

@attr.s
class PropDeliveryStreamHiveJsonSerDe(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.HiveJsonSerDe"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html

    Property Document:
    
    - ``p_TimestampFormats``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.HiveJsonSerDe"
    
    p_TimestampFormats: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TimestampFormats"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats"""

@attr.s
class PropDeliveryStreamSchemaConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.SchemaConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html

    Property Document:
    
    - ``p_CatalogId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid
    - ``p_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename
    - ``p_Region``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region
    - ``p_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename
    - ``p_VersionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.SchemaConfiguration"
    
    p_CatalogId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CatalogId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid"""
    p_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename"""
    p_Region: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Region"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region"""
    p_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename"""
    p_VersionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VersionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid"""

@attr.s
class PropDeliveryStreamSplunkRetryOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.SplunkRetryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html

    Property Document:
    
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.SplunkRetryOptions"
    
    p_DurationInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds"""

@attr.s
class PropDeliveryStreamHttpEndpointConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html

    Property Document:
    
    - ``rp_Url``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url
    - ``p_AccessKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointConfiguration"
    
    rp_Url: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Url"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url"""
    p_AccessKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name"""

@attr.s
class PropDeliveryStreamCopyCommand(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.CopyCommand"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html

    Property Document:
    
    - ``rp_DataTableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename
    - ``p_CopyOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions
    - ``p_DataTableColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.CopyCommand"
    
    rp_DataTableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataTableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename"""
    p_CopyOptions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CopyOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions"""
    p_DataTableColumns: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataTableColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns"""

@attr.s
class PropDeliveryStreamOpenXJsonSerDe(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.OpenXJsonSerDe"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html

    Property Document:
    
    - ``p_CaseInsensitive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive
    - ``p_ColumnToJsonKeyMappings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings
    - ``p_ConvertDotsInJsonKeysToUnderscores``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.OpenXJsonSerDe"
    
    p_CaseInsensitive: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CaseInsensitive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive"""
    p_ColumnToJsonKeyMappings: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnToJsonKeyMappings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings"""
    p_ConvertDotsInJsonKeysToUnderscores: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ConvertDotsInJsonKeysToUnderscores"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores"""

@attr.s
class PropDeliveryStreamOrcSerDe(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.OrcSerDe"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html

    Property Document:
    
    - ``p_BlockSizeBytes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes
    - ``p_BloomFilterColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns
    - ``p_BloomFilterFalsePositiveProbability``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability
    - ``p_Compression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression
    - ``p_DictionaryKeyThreshold``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold
    - ``p_EnablePadding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding
    - ``p_FormatVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion
    - ``p_PaddingTolerance``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance
    - ``p_RowIndexStride``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride
    - ``p_StripeSizeBytes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.OrcSerDe"
    
    p_BlockSizeBytes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockSizeBytes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes"""
    p_BloomFilterColumns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "BloomFilterColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns"""
    p_BloomFilterFalsePositiveProbability: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "BloomFilterFalsePositiveProbability"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability"""
    p_Compression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Compression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression"""
    p_DictionaryKeyThreshold: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "DictionaryKeyThreshold"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold"""
    p_EnablePadding: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnablePadding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding"""
    p_FormatVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FormatVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion"""
    p_PaddingTolerance: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "PaddingTolerance"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance"""
    p_RowIndexStride: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "RowIndexStride"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride"""
    p_StripeSizeBytes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StripeSizeBytes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes"""

@attr.s
class PropDeliveryStreamElasticsearchBufferingHints(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchBufferingHints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html

    Property Document:
    
    - ``p_IntervalInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds
    - ``p_SizeInMBs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchBufferingHints"
    
    p_IntervalInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds"""
    p_SizeInMBs: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInMBs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs"""

@attr.s
class PropDeliveryStreamCloudWatchLoggingOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.CloudWatchLoggingOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled
    - ``p_LogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname
    - ``p_LogStreamName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.CloudWatchLoggingOptions"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled"""
    p_LogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname"""
    p_LogStreamName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogStreamName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname"""

@attr.s
class PropDeliveryStreamBufferingHints(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.BufferingHints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html

    Property Document:
    
    - ``p_IntervalInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds
    - ``p_SizeInMBs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.BufferingHints"
    
    p_IntervalInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds"""
    p_SizeInMBs: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInMBs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs"""

@attr.s
class PropDeliveryStreamProcessorParameter(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ProcessorParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html

    Property Document:
    
    - ``rp_ParameterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername
    - ``rp_ParameterValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ProcessorParameter"
    
    rp_ParameterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername"""
    rp_ParameterValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue"""

@attr.s
class PropDeliveryStreamAmazonopensearchserviceBufferingHints(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceBufferingHints"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html

    Property Document:
    
    - ``p_IntervalInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds
    - ``p_SizeInMBs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceBufferingHints"
    
    p_IntervalInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "IntervalInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds"""
    p_SizeInMBs: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInMBs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs"""

@attr.s
class PropDeliveryStreamDeliveryStreamEncryptionConfigurationInput(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html

    Property Document:
    
    - ``rp_KeyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype
    - ``p_KeyARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput"
    
    rp_KeyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KeyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype"""
    p_KeyARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn"""

@attr.s
class PropDeliveryStreamElasticsearchRetryOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchRetryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html

    Property Document:
    
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchRetryOptions"
    
    p_DurationInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds"""

@attr.s
class PropDeliveryStreamKMSEncryptionConfig(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.KMSEncryptionConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html

    Property Document:
    
    - ``rp_AWSKMSKeyARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.KMSEncryptionConfig"
    
    rp_AWSKMSKeyARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AWSKMSKeyARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn"""

@attr.s
class PropDeliveryStreamDeserializer(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.Deserializer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html

    Property Document:
    
    - ``p_HiveJsonSerDe``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde
    - ``p_OpenXJsonSerDe``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.Deserializer"
    
    p_HiveJsonSerDe: typing.Union['PropDeliveryStreamHiveJsonSerDe', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamHiveJsonSerDe.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamHiveJsonSerDe)),
        metadata={AttrMeta.PROPERTY_NAME: "HiveJsonSerDe"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde"""
    p_OpenXJsonSerDe: typing.Union['PropDeliveryStreamOpenXJsonSerDe', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamOpenXJsonSerDe.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamOpenXJsonSerDe)),
        metadata={AttrMeta.PROPERTY_NAME: "OpenXJsonSerDe"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde"""

@attr.s
class PropDeliveryStreamKinesisStreamSourceConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html

    Property Document:
    
    - ``rp_KinesisStreamARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration"
    
    rp_KinesisStreamARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn"""

@attr.s
class PropDeliveryStreamRedshiftRetryOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.RedshiftRetryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html

    Property Document:
    
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.RedshiftRetryOptions"
    
    p_DurationInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds"""

@attr.s
class PropDeliveryStreamRetryOptions(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.RetryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html

    Property Document:
    
    - ``p_DurationInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.RetryOptions"
    
    p_DurationInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DurationInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds"""

@attr.s
class PropDeliveryStreamParquetSerDe(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ParquetSerDe"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html

    Property Document:
    
    - ``p_BlockSizeBytes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes
    - ``p_Compression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression
    - ``p_EnableDictionaryCompression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression
    - ``p_MaxPaddingBytes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes
    - ``p_PageSizeBytes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes
    - ``p_WriterVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ParquetSerDe"
    
    p_BlockSizeBytes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BlockSizeBytes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes"""
    p_Compression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Compression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression"""
    p_EnableDictionaryCompression: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableDictionaryCompression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression"""
    p_MaxPaddingBytes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxPaddingBytes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes"""
    p_PageSizeBytes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PageSizeBytes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes"""
    p_WriterVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "WriterVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion"""

@attr.s
class PropDeliveryStreamVpcConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.VpcConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html

    Property Document:
    
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn
    - ``rp_SecurityGroupIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids
    - ``rp_SubnetIds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.VpcConfiguration"
    
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn"""
    rp_SecurityGroupIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids"""
    rp_SubnetIds: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetIds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids"""

@attr.s
class PropDeliveryStreamHttpEndpointCommonAttribute(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointCommonAttribute"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html

    Property Document:
    
    - ``rp_AttributeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename
    - ``rp_AttributeValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointCommonAttribute"
    
    rp_AttributeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename"""
    rp_AttributeValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue"""

@attr.s
class PropDeliveryStreamEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.EncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html

    Property Document:
    
    - ``p_KMSEncryptionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig
    - ``p_NoEncryptionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.EncryptionConfiguration"
    
    p_KMSEncryptionConfig: typing.Union['PropDeliveryStreamKMSEncryptionConfig', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamKMSEncryptionConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamKMSEncryptionConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "KMSEncryptionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig"""
    p_NoEncryptionConfig: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "NoEncryptionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig"""

@attr.s
class PropDeliveryStreamInputFormatConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.InputFormatConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html

    Property Document:
    
    - ``p_Deserializer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.InputFormatConfiguration"
    
    p_Deserializer: typing.Union['PropDeliveryStreamDeserializer', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamDeserializer.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamDeserializer)),
        metadata={AttrMeta.PROPERTY_NAME: "Deserializer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer"""

@attr.s
class PropDeliveryStreamProcessor(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.Processor"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html

    Property Document:
    
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.Processor"
    
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type"""
    p_Parameters: typing.List[typing.Union['PropDeliveryStreamProcessorParameter', dict]] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessorParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeliveryStreamProcessorParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters"""

@attr.s
class PropDeliveryStreamHttpEndpointRequestConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointRequestConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html

    Property Document:
    
    - ``p_CommonAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes
    - ``p_ContentEncoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointRequestConfiguration"
    
    p_CommonAttributes: typing.List[typing.Union['PropDeliveryStreamHttpEndpointCommonAttribute', dict]] = attr.ib(
        default=None,
        converter=PropDeliveryStreamHttpEndpointCommonAttribute.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeliveryStreamHttpEndpointCommonAttribute), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CommonAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes"""
    p_ContentEncoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentEncoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding"""

@attr.s
class PropDeliveryStreamSerializer(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.Serializer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html

    Property Document:
    
    - ``p_OrcSerDe``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde
    - ``p_ParquetSerDe``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.Serializer"
    
    p_OrcSerDe: typing.Union['PropDeliveryStreamOrcSerDe', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamOrcSerDe.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamOrcSerDe)),
        metadata={AttrMeta.PROPERTY_NAME: "OrcSerDe"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde"""
    p_ParquetSerDe: typing.Union['PropDeliveryStreamParquetSerDe', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamParquetSerDe.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamParquetSerDe)),
        metadata={AttrMeta.PROPERTY_NAME: "ParquetSerDe"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde"""

@attr.s
class PropDeliveryStreamDynamicPartitioningConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.DynamicPartitioningConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.DynamicPartitioningConfiguration"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled"""
    p_RetryOptions: typing.Union['PropDeliveryStreamRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions"""

@attr.s
class PropDeliveryStreamProcessingConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ProcessingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled
    - ``p_Processors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ProcessingConfiguration"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled"""
    p_Processors: typing.List[typing.Union['PropDeliveryStreamProcessor', dict]] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessor.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeliveryStreamProcessor), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Processors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors"""

@attr.s
class PropDeliveryStreamOutputFormatConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.OutputFormatConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html

    Property Document:
    
    - ``p_Serializer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.OutputFormatConfiguration"
    
    p_Serializer: typing.Union['PropDeliveryStreamSerializer', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamSerializer.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamSerializer)),
        metadata={AttrMeta.PROPERTY_NAME: "Serializer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer"""

@attr.s
class PropDeliveryStreamS3DestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html

    Property Document:
    
    - ``rp_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn
    - ``p_BufferingHints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions
    - ``p_CompressionFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat
    - ``p_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration
    - ``p_ErrorOutputPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration"
    
    rp_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn"""
    p_BufferingHints: typing.Union['PropDeliveryStreamBufferingHints', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamBufferingHints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamBufferingHints)),
        metadata={AttrMeta.PROPERTY_NAME: "BufferingHints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions"""
    p_CompressionFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CompressionFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat"""
    p_EncryptionConfiguration: typing.Union['PropDeliveryStreamEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration"""
    p_ErrorOutputPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ErrorOutputPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix"""

@attr.s
class PropDeliveryStreamRedshiftDestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html

    Property Document:
    
    - ``rp_ClusterJDBCURL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl
    - ``rp_CopyCommand``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand
    - ``rp_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn
    - ``rp_S3Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration
    - ``rp_Username``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions
    - ``p_S3BackupConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration"
    
    rp_ClusterJDBCURL: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterJDBCURL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl"""
    rp_CopyCommand: typing.Union['PropDeliveryStreamCopyCommand', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCopyCommand.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamCopyCommand),
        metadata={AttrMeta.PROPERTY_NAME: "CopyCommand"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand"""
    rp_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn"""
    rp_S3Configuration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "S3Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration"""
    rp_Username: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Username"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration"""
    p_RetryOptions: typing.Union['PropDeliveryStreamRedshiftRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamRedshiftRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamRedshiftRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions"""
    p_S3BackupConfiguration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode"""

@attr.s
class PropDeliveryStreamHttpEndpointDestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html

    Property Document:
    
    - ``rp_EndpointConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration
    - ``rp_S3Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration
    - ``p_BufferingHints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration
    - ``p_RequestConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions
    - ``p_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration"
    
    rp_EndpointConfiguration: typing.Union['PropDeliveryStreamHttpEndpointConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamHttpEndpointConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamHttpEndpointConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "EndpointConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration"""
    rp_S3Configuration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "S3Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration"""
    p_BufferingHints: typing.Union['PropDeliveryStreamBufferingHints', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamBufferingHints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamBufferingHints)),
        metadata={AttrMeta.PROPERTY_NAME: "BufferingHints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration"""
    p_RequestConfiguration: typing.Union['PropDeliveryStreamHttpEndpointRequestConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamHttpEndpointRequestConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamHttpEndpointRequestConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "RequestConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration"""
    p_RetryOptions: typing.Union['PropDeliveryStreamRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions"""
    p_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode"""

@attr.s
class PropDeliveryStreamDataFormatConversionConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.DataFormatConversionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html

    Property Document:
    
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled
    - ``p_InputFormatConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration
    - ``p_OutputFormatConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration
    - ``p_SchemaConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.DataFormatConversionConfiguration"
    
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled"""
    p_InputFormatConfiguration: typing.Union['PropDeliveryStreamInputFormatConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamInputFormatConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamInputFormatConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "InputFormatConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration"""
    p_OutputFormatConfiguration: typing.Union['PropDeliveryStreamOutputFormatConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamOutputFormatConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamOutputFormatConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "OutputFormatConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration"""
    p_SchemaConfiguration: typing.Union['PropDeliveryStreamSchemaConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamSchemaConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamSchemaConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SchemaConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration"""

@attr.s
class PropDeliveryStreamAmazonopensearchserviceDestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn
    - ``rp_S3Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration
    - ``p_BufferingHints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions
    - ``p_ClusterEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint
    - ``p_DomainARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn
    - ``p_IndexRotationPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode
    - ``p_TypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename
    - ``p_VpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn"""
    rp_S3Configuration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "S3Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration"""
    p_BufferingHints: typing.Union['PropDeliveryStreamAmazonopensearchserviceBufferingHints', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamAmazonopensearchserviceBufferingHints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamAmazonopensearchserviceBufferingHints)),
        metadata={AttrMeta.PROPERTY_NAME: "BufferingHints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions"""
    p_ClusterEndpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint"""
    p_DomainARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn"""
    p_IndexRotationPeriod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IndexRotationPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration"""
    p_RetryOptions: typing.Union['PropDeliveryStreamAmazonopensearchserviceRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamAmazonopensearchserviceRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamAmazonopensearchserviceRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode"""
    p_TypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename"""
    p_VpcConfiguration: typing.Union['PropDeliveryStreamVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamVpcConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamVpcConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration"""

@attr.s
class PropDeliveryStreamSplunkDestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html

    Property Document:
    
    - ``rp_HECEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint
    - ``rp_HECEndpointType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype
    - ``rp_HECToken``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken
    - ``rp_S3Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions
    - ``p_HECAcknowledgmentTimeoutInSeconds``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration"
    
    rp_HECEndpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HECEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint"""
    rp_HECEndpointType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HECEndpointType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype"""
    rp_HECToken: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HECToken"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken"""
    rp_S3Configuration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "S3Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions"""
    p_HECAcknowledgmentTimeoutInSeconds: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "HECAcknowledgmentTimeoutInSeconds"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration"""
    p_RetryOptions: typing.Union['PropDeliveryStreamSplunkRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamSplunkRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamSplunkRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode"""

@attr.s
class PropDeliveryStreamElasticsearchDestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html

    Property Document:
    
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn
    - ``rp_S3Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration
    - ``p_BufferingHints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions
    - ``p_ClusterEndpoint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint
    - ``p_DomainARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn
    - ``p_IndexRotationPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration
    - ``p_RetryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode
    - ``p_TypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename
    - ``p_VpcConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration"
    
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn"""
    rp_S3Configuration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "S3Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration"""
    p_BufferingHints: typing.Union['PropDeliveryStreamElasticsearchBufferingHints', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamElasticsearchBufferingHints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamElasticsearchBufferingHints)),
        metadata={AttrMeta.PROPERTY_NAME: "BufferingHints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions"""
    p_ClusterEndpoint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ClusterEndpoint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint"""
    p_DomainARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn"""
    p_IndexRotationPeriod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IndexRotationPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration"""
    p_RetryOptions: typing.Union['PropDeliveryStreamElasticsearchRetryOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamElasticsearchRetryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamElasticsearchRetryOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "RetryOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode"""
    p_TypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename"""
    p_VpcConfiguration: typing.Union['PropDeliveryStreamVpcConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamVpcConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamVpcConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration"""

@attr.s
class PropDeliveryStreamExtendedS3DestinationConfiguration(Property):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html

    Property Document:
    
    - ``rp_BucketARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn
    - ``rp_RoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn
    - ``p_BufferingHints``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints
    - ``p_CloudWatchLoggingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions
    - ``p_CompressionFormat``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat
    - ``p_DataFormatConversionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration
    - ``p_DynamicPartitioningConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration
    - ``p_EncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration
    - ``p_ErrorOutputPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix
    - ``p_Prefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix
    - ``p_ProcessingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration
    - ``p_S3BackupConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration
    - ``p_S3BackupMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration"
    
    rp_BucketARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn"""
    rp_RoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn"""
    p_BufferingHints: typing.Union['PropDeliveryStreamBufferingHints', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamBufferingHints.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamBufferingHints)),
        metadata={AttrMeta.PROPERTY_NAME: "BufferingHints"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints"""
    p_CloudWatchLoggingOptions: typing.Union['PropDeliveryStreamCloudWatchLoggingOptions', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamCloudWatchLoggingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamCloudWatchLoggingOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLoggingOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions"""
    p_CompressionFormat: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CompressionFormat"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat"""
    p_DataFormatConversionConfiguration: typing.Union['PropDeliveryStreamDataFormatConversionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamDataFormatConversionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamDataFormatConversionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DataFormatConversionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration"""
    p_DynamicPartitioningConfiguration: typing.Union['PropDeliveryStreamDynamicPartitioningConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamDynamicPartitioningConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamDynamicPartitioningConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DynamicPartitioningConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration"""
    p_EncryptionConfiguration: typing.Union['PropDeliveryStreamEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration"""
    p_ErrorOutputPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ErrorOutputPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix"""
    p_Prefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Prefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix"""
    p_ProcessingConfiguration: typing.Union['PropDeliveryStreamProcessingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamProcessingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamProcessingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ProcessingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration"""
    p_S3BackupConfiguration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration"""
    p_S3BackupMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3BackupMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode"""


#--- Resource declaration ---

@attr.s
class DeliveryStream(Resource):
    """
    AWS Object Type = "AWS::KinesisFirehose::DeliveryStream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html

    Property Document:
    
    - ``p_AmazonopensearchserviceDestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration
    - ``p_DeliveryStreamEncryptionConfigurationInput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput
    - ``p_DeliveryStreamName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname
    - ``p_DeliveryStreamType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype
    - ``p_ElasticsearchDestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration
    - ``p_ExtendedS3DestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration
    - ``p_HttpEndpointDestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration
    - ``p_KinesisStreamSourceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration
    - ``p_RedshiftDestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration
    - ``p_S3DestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration
    - ``p_SplunkDestinationConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags
    """
    AWS_OBJECT_TYPE = "AWS::KinesisFirehose::DeliveryStream"

    
    p_AmazonopensearchserviceDestinationConfiguration: typing.Union['PropDeliveryStreamAmazonopensearchserviceDestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamAmazonopensearchserviceDestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamAmazonopensearchserviceDestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AmazonopensearchserviceDestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration"""
    p_DeliveryStreamEncryptionConfigurationInput: typing.Union['PropDeliveryStreamDeliveryStreamEncryptionConfigurationInput', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamDeliveryStreamEncryptionConfigurationInput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamDeliveryStreamEncryptionConfigurationInput)),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStreamEncryptionConfigurationInput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput"""
    p_DeliveryStreamName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStreamName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname"""
    p_DeliveryStreamType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStreamType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype"""
    p_ElasticsearchDestinationConfiguration: typing.Union['PropDeliveryStreamElasticsearchDestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamElasticsearchDestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamElasticsearchDestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ElasticsearchDestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration"""
    p_ExtendedS3DestinationConfiguration: typing.Union['PropDeliveryStreamExtendedS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamExtendedS3DestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamExtendedS3DestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ExtendedS3DestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration"""
    p_HttpEndpointDestinationConfiguration: typing.Union['PropDeliveryStreamHttpEndpointDestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamHttpEndpointDestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamHttpEndpointDestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "HttpEndpointDestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration"""
    p_KinesisStreamSourceConfiguration: typing.Union['PropDeliveryStreamKinesisStreamSourceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamKinesisStreamSourceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamKinesisStreamSourceConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisStreamSourceConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration"""
    p_RedshiftDestinationConfiguration: typing.Union['PropDeliveryStreamRedshiftDestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamRedshiftDestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamRedshiftDestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "RedshiftDestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration"""
    p_S3DestinationConfiguration: typing.Union['PropDeliveryStreamS3DestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamS3DestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamS3DestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "S3DestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration"""
    p_SplunkDestinationConfiguration: typing.Union['PropDeliveryStreamSplunkDestinationConfiguration', dict] = attr.ib(
        default=None,
        converter=PropDeliveryStreamSplunkDestinationConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeliveryStreamSplunkDestinationConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SplunkDestinationConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#aws-resource-kinesisfirehose-deliverystream-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
