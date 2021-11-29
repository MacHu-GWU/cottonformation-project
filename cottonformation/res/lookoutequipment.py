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
class InferenceScheduler(Resource):
    """
    AWS Object Type = "AWS::LookoutEquipment::InferenceScheduler"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html

    Property Document:
    
    - ``rp_DataInputConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration
    - ``rp_DataOutputConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration
    - ``rp_DataUploadFrequency``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency
    - ``rp_ModelName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn
    - ``p_DataDelayOffsetInMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes
    - ``p_InferenceSchedulerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername
    - ``p_ServerSideKmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags
    """
    AWS_OBJECT_TYPE = "AWS::LookoutEquipment::InferenceScheduler"

    
    rp_DataInputConfiguration: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "DataInputConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datainputconfiguration"""
    rp_DataOutputConfiguration: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "DataOutputConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-dataoutputconfiguration"""
    rp_DataUploadFrequency: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataUploadFrequency"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datauploadfrequency"""
    rp_ModelName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ModelName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-modelname"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-rolearn"""
    p_DataDelayOffsetInMinutes: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DataDelayOffsetInMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-datadelayoffsetinminutes"""
    p_InferenceSchedulerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InferenceSchedulerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-inferenceschedulername"""
    p_ServerSideKmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerSideKmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-serversidekmskeyid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#cfn-lookoutequipment-inferencescheduler-tags"""

    
    @property
    def rv_InferenceSchedulerArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutequipment-inferencescheduler.html#aws-resource-lookoutequipment-inferencescheduler-return-values"""
        return GetAtt(resource=self, attr_name="InferenceSchedulerArn")
    
