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
class PropStreamKinesisConfiguration(Property):
    """
    AWS Object Type = "AWS::QLDB::Stream.KinesisConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html

    Property Document:
    
    - ``p_AggregationEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled
    - ``p_StreamArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn
    """
    AWS_OBJECT_TYPE = "AWS::QLDB::Stream.KinesisConfiguration"
    
    p_AggregationEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AggregationEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled"""
    p_StreamArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StreamArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn"""


#--- Resource declaration ---

@attr.s
class Stream(Resource):
    """
    AWS Object Type = "AWS::QLDB::Stream"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html

    Property Document:
    
    - ``rp_InclusiveStartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
    - ``rp_KinesisConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
    - ``rp_LedgerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
    - ``rp_StreamName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
    - ``p_ExclusiveEndTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
    """
    AWS_OBJECT_TYPE = "AWS::QLDB::Stream"

    
    rp_InclusiveStartTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InclusiveStartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime"""
    rp_KinesisConfiguration: typing.Union['PropStreamKinesisConfiguration', dict] = attr.ib(
        default=None,
        converter=PropStreamKinesisConfiguration.from_dict,
        validator=attr.validators.instance_of(PropStreamKinesisConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration"""
    rp_LedgerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LedgerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn"""
    rp_StreamName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StreamName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname"""
    p_ExclusiveEndTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExclusiveEndTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#aws-resource-qldb-stream-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#aws-resource-qldb-stream-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class Ledger(Resource):
    """
    AWS Object Type = "AWS::QLDB::Ledger"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html

    Property Document:
    
    - ``rp_PermissionsMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
    - ``p_DeletionProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
    - ``p_KmsKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
    """
    AWS_OBJECT_TYPE = "AWS::QLDB::Ledger"

    
    rp_PermissionsMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PermissionsMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode"""
    p_DeletionProtection: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeletionProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection"""
    p_KmsKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags"""

    
