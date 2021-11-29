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


#--- Resource declaration ---

@attr.s
class Database(Resource):
    """
    AWS Object Type = "AWS::Timestream::Database"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html

    Property Document:
    
    - ``p_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-databasename
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-kmskeyid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-tags
    """
    AWS_OBJECT_TYPE = "AWS::Timestream::Database"

    
    p_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-databasename"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-kmskeyid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#cfn-timestream-database-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html#aws-resource-timestream-database-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class Table(Resource):
    """
    AWS Object Type = "AWS::Timestream::Table"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html

    Property Document:
    
    - ``rp_DatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-databasename
    - ``p_RetentionProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-retentionproperties
    - ``p_TableName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tablename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tags
    """
    AWS_OBJECT_TYPE = "AWS::Timestream::Table"

    
    rp_DatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-databasename"""
    p_RetentionProperties: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "RetentionProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-retentionproperties"""
    p_TableName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TableName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tablename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#cfn-timestream-table-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#aws-resource-timestream-table-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html#aws-resource-timestream-table-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    
