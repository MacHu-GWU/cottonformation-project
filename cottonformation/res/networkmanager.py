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
class PropDeviceLocation(Property):
    """
    AWS Object Type = "AWS::NetworkManager::Device.Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html

    Property Document:
    
    - ``p_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address
    - ``p_Latitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude
    - ``p_Longitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Device.Location"
    
    p_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address"""
    p_Latitude: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Latitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude"""
    p_Longitude: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Longitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude"""

@attr.s
class PropLinkBandwidth(Property):
    """
    AWS Object Type = "AWS::NetworkManager::Link.Bandwidth"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html

    Property Document:
    
    - ``p_DownloadSpeed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed
    - ``p_UploadSpeed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Link.Bandwidth"
    
    p_DownloadSpeed: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DownloadSpeed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed"""
    p_UploadSpeed: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UploadSpeed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed"""

@attr.s
class PropSiteLocation(Property):
    """
    AWS Object Type = "AWS::NetworkManager::Site.Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html

    Property Document:
    
    - ``p_Address``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address
    - ``p_Latitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude
    - ``p_Longitude``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Site.Location"
    
    p_Address: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Address"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address"""
    p_Latitude: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Latitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude"""
    p_Longitude: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Longitude"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude"""


#--- Resource declaration ---

@attr.s
class Link(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::Link"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html

    Property Document:
    
    - ``rp_Bandwidth``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
    - ``rp_SiteId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
    - ``p_Provider``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Link"

    
    rp_Bandwidth: typing.Union['PropLinkBandwidth', dict] = attr.ib(
        default=None,
        converter=PropLinkBandwidth.from_dict,
        validator=attr.validators.instance_of(PropLinkBandwidth),
        metadata={AttrMeta.PROPERTY_NAME: "Bandwidth"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth"""
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid"""
    rp_SiteId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SiteId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description"""
    p_Provider: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Provider"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags"""

    
    @property
    def rv_LinkArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#aws-resource-networkmanager-link-return-values"""
        return GetAtt(resource=self, attr_name="LinkArn")
    
    @property
    def rv_LinkId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#aws-resource-networkmanager-link-return-values"""
        return GetAtt(resource=self, attr_name="LinkId")
    

@attr.s
class CustomerGatewayAssociation(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::CustomerGatewayAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html

    Property Document:
    
    - ``rp_CustomerGatewayArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
    - ``rp_DeviceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
    - ``p_LinkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::CustomerGatewayAssociation"

    
    rp_CustomerGatewayArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CustomerGatewayArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn"""
    rp_DeviceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid"""
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid"""
    p_LinkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LinkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid"""

    

@attr.s
class LinkAssociation(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::LinkAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html

    Property Document:
    
    - ``rp_DeviceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
    - ``rp_LinkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::LinkAssociation"

    
    rp_DeviceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid"""
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid"""
    rp_LinkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LinkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid"""

    

@attr.s
class Device(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::Device"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html

    Property Document:
    
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
    - ``p_Model``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
    - ``p_SerialNumber``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
    - ``p_SiteId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
    - ``p_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
    - ``p_Vendor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Device"

    
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description"""
    p_Location: typing.Union['PropDeviceLocation', dict] = attr.ib(
        default=None,
        converter=PropDeviceLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeviceLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location"""
    p_Model: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Model"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model"""
    p_SerialNumber: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SerialNumber"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber"""
    p_SiteId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SiteId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid"""
    p_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type"""
    p_Vendor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Vendor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags"""

    
    @property
    def rv_DeviceArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#aws-resource-networkmanager-device-return-values"""
        return GetAtt(resource=self, attr_name="DeviceArn")
    
    @property
    def rv_DeviceId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#aws-resource-networkmanager-device-return-values"""
        return GetAtt(resource=self, attr_name="DeviceId")
    

@attr.s
class GlobalNetwork(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::GlobalNetwork"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html

    Property Document:
    
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::GlobalNetwork"

    
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#aws-resource-networkmanager-globalnetwork-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#aws-resource-networkmanager-globalnetwork-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class TransitGatewayRegistration(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::TransitGatewayRegistration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html

    Property Document:
    
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
    - ``rp_TransitGatewayArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::TransitGatewayRegistration"

    
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid"""
    rp_TransitGatewayArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TransitGatewayArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn"""

    

@attr.s
class Site(Resource):
    """
    AWS Object Type = "AWS::NetworkManager::Site"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html

    Property Document:
    
    - ``rp_GlobalNetworkId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
    - ``p_Location``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkManager::Site"

    
    rp_GlobalNetworkId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GlobalNetworkId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description"""
    p_Location: typing.Union['PropSiteLocation', dict] = attr.ib(
        default=None,
        converter=PropSiteLocation.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSiteLocation)),
        metadata={AttrMeta.PROPERTY_NAME: "Location"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags"""

    
    @property
    def rv_SiteArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#aws-resource-networkmanager-site-return-values"""
        return GetAtt(resource=self, attr_name="SiteArn")
    
    @property
    def rv_SiteId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#aws-resource-networkmanager-site-return-values"""
        return GetAtt(resource=self, attr_name="SiteId")
    
