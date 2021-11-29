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
class PropTableEncryptionSpecification(Property):
    """
    AWS Object Type = "AWS::Cassandra::Table.EncryptionSpecification"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html

    Property Document:
    
    - ``rp_EncryptionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-encryptiontype
    - ``p_KmsKeyIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-kmskeyidentifier
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table.EncryptionSpecification"
    
    rp_EncryptionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-encryptiontype"""
    p_KmsKeyIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-kmskeyidentifier"""

@attr.s
class PropTableColumn(Property):
    """
    AWS Object Type = "AWS::Cassandra::Table.Column"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html

    Property Document:
    
    - ``rp_ColumnName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columnname
    - ``rp_ColumnType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columntype
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table.Column"
    
    rp_ColumnName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columnname"""
    rp_ColumnType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ColumnType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columntype"""

@attr.s
class PropTableClusteringKeyColumn(Property):
    """
    AWS Object Type = "AWS::Cassandra::Table.ClusteringKeyColumn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html

    Property Document:
    
    - ``rp_Column``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-column
    - ``p_OrderBy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-orderby
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table.ClusteringKeyColumn"
    
    rp_Column: typing.Union['PropTableColumn', dict] = attr.ib(
        default=None,
        converter=PropTableColumn.from_dict,
        validator=attr.validators.instance_of(PropTableColumn),
        metadata={AttrMeta.PROPERTY_NAME: "Column"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-column"""
    p_OrderBy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OrderBy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-orderby"""

@attr.s
class PropTableProvisionedThroughput(Property):
    """
    AWS Object Type = "AWS::Cassandra::Table.ProvisionedThroughput"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html

    Property Document:
    
    - ``rp_ReadCapacityUnits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-readcapacityunits
    - ``rp_WriteCapacityUnits``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-writecapacityunits
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table.ProvisionedThroughput"
    
    rp_ReadCapacityUnits: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ReadCapacityUnits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-readcapacityunits"""
    rp_WriteCapacityUnits: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "WriteCapacityUnits"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-writecapacityunits"""

@attr.s
class PropTableBillingMode(Property):
    """
    AWS Object Type = "AWS::Cassandra::Table.BillingMode"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html

    Property Document:
    
    - ``rp_Mode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-mode
    - ``p_ProvisionedThroughput``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-provisionedthroughput
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table.BillingMode"
    
    rp_Mode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Mode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-mode"""
    p_ProvisionedThroughput: typing.Union['PropTableProvisionedThroughput', dict] = attr.ib(
        default=None,
        converter=PropTableProvisionedThroughput.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableProvisionedThroughput)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedThroughput"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-provisionedthroughput"""


#--- Resource declaration ---

@attr.s
class Keyspace(Resource):
    """
    AWS Object Type = "AWS::Cassandra::Keyspace"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html

    Property Document:
    
    - ``p_KeyspaceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Keyspace"

    
    p_KeyspaceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyspaceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags"""

    

@attr.s
class Table(Resource):
    """
    AWS Object Type = "AWS::Cassandra::Table"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html

    Property Document:
    
    - ``rp_KeyspaceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename
    - ``rp_PartitionKeyColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns
    - ``p_BillingMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode
    - ``p_ClusteringKeyColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns
    - ``p_DefaultTimeToLive``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-defaulttimetolive
    - ``p_EncryptionSpecification``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification
    - ``p_PointInTimeRecoveryEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled
    - ``p_RegularColumns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags
    """
    AWS_OBJECT_TYPE = "AWS::Cassandra::Table"

    
    rp_KeyspaceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KeyspaceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename"""
    rp_PartitionKeyColumns: typing.List[typing.Union['PropTableColumn', dict]] = attr.ib(
        default=None,
        converter=PropTableColumn.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableColumn), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "PartitionKeyColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns"""
    p_BillingMode: typing.Union['PropTableBillingMode', dict] = attr.ib(
        default=None,
        converter=PropTableBillingMode.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableBillingMode)),
        metadata={AttrMeta.PROPERTY_NAME: "BillingMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode"""
    p_ClusteringKeyColumns: typing.List[typing.Union['PropTableClusteringKeyColumn', dict]] = attr.ib(
        default=None,
        converter=PropTableClusteringKeyColumn.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableClusteringKeyColumn), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ClusteringKeyColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns"""
    p_DefaultTimeToLive: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultTimeToLive"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-defaulttimetolive"""
    p_EncryptionSpecification: typing.Union['PropTableEncryptionSpecification', dict] = attr.ib(
        default=None,
        converter=PropTableEncryptionSpecification.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTableEncryptionSpecification)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionSpecification"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification"""
    p_PointInTimeRecoveryEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PointInTimeRecoveryEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled"""
    p_RegularColumns: typing.List[typing.Union['PropTableColumn', dict]] = attr.ib(
        default=None,
        converter=PropTableColumn.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropTableColumn), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RegularColumns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags"""

    
