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
class PropNotificationChannelSnsChannelConfig(Property):
    """
    AWS Object Type = "AWS::DevOpsGuru::NotificationChannel.SnsChannelConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html

    Property Document:
    
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html#cfn-devopsguru-notificationchannel-snschannelconfig-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::NotificationChannel.SnsChannelConfig"
    
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html#cfn-devopsguru-notificationchannel-snschannelconfig-topicarn"""

@attr.s
class PropResourceCollectionCloudFormationCollectionFilter(Property):
    """
    AWS Object Type = "AWS::DevOpsGuru::ResourceCollection.CloudFormationCollectionFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html

    Property Document:
    
    - ``p_StackNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::ResourceCollection.CloudFormationCollectionFilter"
    
    p_StackNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StackNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames"""

@attr.s
class PropNotificationChannelNotificationChannelConfig(Property):
    """
    AWS Object Type = "AWS::DevOpsGuru::NotificationChannel.NotificationChannelConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html

    Property Document:
    
    - ``p_Sns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-sns
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::NotificationChannel.NotificationChannelConfig"
    
    p_Sns: typing.Union['PropNotificationChannelSnsChannelConfig', dict] = attr.ib(
        default=None,
        converter=PropNotificationChannelSnsChannelConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropNotificationChannelSnsChannelConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "Sns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-sns"""

@attr.s
class PropResourceCollectionResourceCollectionFilter(Property):
    """
    AWS Object Type = "AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html

    Property Document:
    
    - ``p_CloudFormation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-cloudformation
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::ResourceCollection.ResourceCollectionFilter"
    
    p_CloudFormation: typing.Union['PropResourceCollectionCloudFormationCollectionFilter', dict] = attr.ib(
        default=None,
        converter=PropResourceCollectionCloudFormationCollectionFilter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceCollectionCloudFormationCollectionFilter)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudFormation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-cloudformation"""


#--- Resource declaration ---

@attr.s
class NotificationChannel(Resource):
    """
    AWS Object Type = "AWS::DevOpsGuru::NotificationChannel"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html

    Property Document:
    
    - ``rp_Config``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::NotificationChannel"

    
    rp_Config: typing.Union['PropNotificationChannelNotificationChannelConfig', dict] = attr.ib(
        default=None,
        converter=PropNotificationChannelNotificationChannelConfig.from_dict,
        validator=attr.validators.instance_of(PropNotificationChannelNotificationChannelConfig),
        metadata={AttrMeta.PROPERTY_NAME: "Config"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#aws-resource-devopsguru-notificationchannel-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class ResourceCollection(Resource):
    """
    AWS Object Type = "AWS::DevOpsGuru::ResourceCollection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html

    Property Document:
    
    - ``rp_ResourceCollectionFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter
    """
    AWS_OBJECT_TYPE = "AWS::DevOpsGuru::ResourceCollection"

    
    rp_ResourceCollectionFilter: typing.Union['PropResourceCollectionResourceCollectionFilter', dict] = attr.ib(
        default=None,
        converter=PropResourceCollectionResourceCollectionFilter.from_dict,
        validator=attr.validators.instance_of(PropResourceCollectionResourceCollectionFilter),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceCollectionFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter"""

    
    @property
    def rv_ResourceCollectionType(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#aws-resource-devopsguru-resourcecollection-return-values"""
        return GetAtt(resource=self, attr_name="ResourceCollectionType")
    
