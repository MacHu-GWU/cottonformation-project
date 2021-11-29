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
class PropMulticastGroupLoRaWAN(Property):
    """
    AWS Object Type = "AWS::IoTWireless::MulticastGroup.LoRaWAN"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html

    Property Document:
    
    - ``rp_DlClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-dlclass
    - ``rp_RfRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-rfregion
    - ``p_NumberOfDevicesInGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup
    - ``p_NumberOfDevicesRequested``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::MulticastGroup.LoRaWAN"
    
    rp_DlClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DlClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-dlclass"""
    rp_RfRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RfRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-rfregion"""
    p_NumberOfDevicesInGroup: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "NumberOfDevicesInGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup"""
    p_NumberOfDevicesRequested: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "NumberOfDevicesRequested"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested"""

@attr.s
class PropWirelessDeviceSessionKeysAbpV11(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.SessionKeysAbpV11"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html

    Property Document:
    
    - ``rp_AppSKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey
    - ``rp_FNwkSIntKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey
    - ``rp_NwkSEncKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey
    - ``rp_SNwkSIntKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.SessionKeysAbpV11"
    
    rp_AppSKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppSKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey"""
    rp_FNwkSIntKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FNwkSIntKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey"""
    rp_NwkSEncKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NwkSEncKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey"""
    rp_SNwkSIntKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SNwkSIntKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey"""

@attr.s
class PropDeviceProfileLoRaWANDeviceProfile(Property):
    """
    AWS Object Type = "AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html

    Property Document:
    
    - ``p_ClassBTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout
    - ``p_ClassCTimeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout
    - ``p_MacVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion
    - ``p_MaxDutyCycle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle
    - ``p_MaxEirp``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp
    - ``p_PingSlotDr``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr
    - ``p_PingSlotFreq``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq
    - ``p_PingSlotPeriod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod
    - ``p_RegParamsRevision``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision
    - ``p_RfRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion
    - ``p_Supports32BitFCnt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt
    - ``p_SupportsClassB``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb
    - ``p_SupportsClassC``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc
    - ``p_SupportsJoin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::DeviceProfile.LoRaWANDeviceProfile"
    
    p_ClassBTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ClassBTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout"""
    p_ClassCTimeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ClassCTimeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout"""
    p_MacVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MacVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion"""
    p_MaxDutyCycle: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxDutyCycle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle"""
    p_MaxEirp: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxEirp"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp"""
    p_PingSlotDr: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PingSlotDr"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr"""
    p_PingSlotFreq: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PingSlotFreq"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq"""
    p_PingSlotPeriod: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "PingSlotPeriod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod"""
    p_RegParamsRevision: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RegParamsRevision"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision"""
    p_RfRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RfRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion"""
    p_Supports32BitFCnt: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Supports32BitFCnt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt"""
    p_SupportsClassB: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportsClassB"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb"""
    p_SupportsClassC: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportsClassC"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc"""
    p_SupportsJoin: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportsJoin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin"""

@attr.s
class PropFuotaTaskLoRaWAN(Property):
    """
    AWS Object Type = "AWS::IoTWireless::FuotaTask.LoRaWAN"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html

    Property Document:
    
    - ``rp_RfRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-rfregion
    - ``p_StartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-starttime
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::FuotaTask.LoRaWAN"
    
    rp_RfRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RfRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-rfregion"""
    p_StartTime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-starttime"""

@attr.s
class PropTaskDefinitionLoRaWANGatewayVersion(Property):
    """
    AWS Object Type = "AWS::IoTWireless::TaskDefinition.LoRaWANGatewayVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html

    Property Document:
    
    - ``p_Model``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model
    - ``p_PackageVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion
    - ``p_Station``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::TaskDefinition.LoRaWANGatewayVersion"
    
    p_Model: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Model"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model"""
    p_PackageVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PackageVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion"""
    p_Station: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Station"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station"""

@attr.s
class PropPartnerAccountSidewalkAccountInfo(Property):
    """
    AWS Object Type = "AWS::IoTWireless::PartnerAccount.SidewalkAccountInfo"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html

    Property Document:
    
    - ``rp_AppServerPrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::PartnerAccount.SidewalkAccountInfo"
    
    rp_AppServerPrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppServerPrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey"""

@attr.s
class PropWirelessGatewayLoRaWANGateway(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessGateway.LoRaWANGateway"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html

    Property Document:
    
    - ``rp_GatewayEui``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui
    - ``rp_RfRegion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessGateway.LoRaWANGateway"
    
    rp_GatewayEui: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GatewayEui"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui"""
    rp_RfRegion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RfRegion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion"""

@attr.s
class PropTaskDefinitionLoRaWANUpdateGatewayTaskCreate(Property):
    """
    AWS Object Type = "AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskCreate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html

    Property Document:
    
    - ``p_CurrentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion
    - ``p_SigKeyCrc``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc
    - ``p_UpdateSignature``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature
    - ``p_UpdateVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskCreate"
    
    p_CurrentVersion: typing.Union['PropTaskDefinitionLoRaWANGatewayVersion', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANGatewayVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANGatewayVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "CurrentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion"""
    p_SigKeyCrc: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "SigKeyCrc"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc"""
    p_UpdateSignature: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateSignature"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature"""
    p_UpdateVersion: typing.Union['PropTaskDefinitionLoRaWANGatewayVersion', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANGatewayVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANGatewayVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion"""

@attr.s
class PropWirelessDeviceOtaaV11(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.OtaaV11"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html

    Property Document:
    
    - ``rp_AppKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey
    - ``rp_JoinEui``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui
    - ``rp_NwkKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.OtaaV11"
    
    rp_AppKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey"""
    rp_JoinEui: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "JoinEui"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui"""
    rp_NwkKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NwkKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey"""

@attr.s
class PropWirelessDeviceSessionKeysAbpV10x(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.SessionKeysAbpV10x"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html

    Property Document:
    
    - ``rp_AppSKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey
    - ``rp_NwkSKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.SessionKeysAbpV10x"
    
    rp_AppSKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppSKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey"""
    rp_NwkSKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "NwkSKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey"""

@attr.s
class PropServiceProfileLoRaWANServiceProfile(Property):
    """
    AWS Object Type = "AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html

    Property Document:
    
    - ``p_AddGwMetadata``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata
    - ``p_ChannelMask``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask
    - ``p_DevStatusReqFreq``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq
    - ``p_DlBucketSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize
    - ``p_DlRate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate
    - ``p_DlRatePolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy
    - ``p_DrMax``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax
    - ``p_DrMin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin
    - ``p_HrAllowed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed
    - ``p_MinGwDiversity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity
    - ``p_NwkGeoLoc``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc
    - ``p_PrAllowed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed
    - ``p_RaAllowed``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed
    - ``p_ReportDevStatusBattery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery
    - ``p_ReportDevStatusMargin``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin
    - ``p_TargetPer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper
    - ``p_UlBucketSize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize
    - ``p_UlRate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate
    - ``p_UlRatePolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::ServiceProfile.LoRaWANServiceProfile"
    
    p_AddGwMetadata: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AddGwMetadata"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata"""
    p_ChannelMask: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ChannelMask"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask"""
    p_DevStatusReqFreq: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DevStatusReqFreq"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq"""
    p_DlBucketSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DlBucketSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize"""
    p_DlRate: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DlRate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate"""
    p_DlRatePolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DlRatePolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy"""
    p_DrMax: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DrMax"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax"""
    p_DrMin: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DrMin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin"""
    p_HrAllowed: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "HrAllowed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed"""
    p_MinGwDiversity: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MinGwDiversity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity"""
    p_NwkGeoLoc: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "NwkGeoLoc"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc"""
    p_PrAllowed: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PrAllowed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed"""
    p_RaAllowed: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RaAllowed"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed"""
    p_ReportDevStatusBattery: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportDevStatusBattery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery"""
    p_ReportDevStatusMargin: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportDevStatusMargin"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin"""
    p_TargetPer: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetPer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper"""
    p_UlBucketSize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UlBucketSize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize"""
    p_UlRate: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "UlRate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate"""
    p_UlRatePolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UlRatePolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy"""

@attr.s
class PropWirelessDeviceOtaaV10x(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.OtaaV10x"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html

    Property Document:
    
    - ``rp_AppEui``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui
    - ``rp_AppKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.OtaaV10x"
    
    rp_AppEui: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppEui"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui"""
    rp_AppKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey"""

@attr.s
class PropPartnerAccountSidewalkUpdateAccount(Property):
    """
    AWS Object Type = "AWS::IoTWireless::PartnerAccount.SidewalkUpdateAccount"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html

    Property Document:
    
    - ``p_AppServerPrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::PartnerAccount.SidewalkUpdateAccount"
    
    p_AppServerPrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AppServerPrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey"""

@attr.s
class PropWirelessDeviceAbpV11(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.AbpV11"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html

    Property Document:
    
    - ``rp_DevAddr``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr
    - ``rp_SessionKeys``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.AbpV11"
    
    rp_DevAddr: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DevAddr"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr"""
    rp_SessionKeys: typing.Union['PropWirelessDeviceSessionKeysAbpV11', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceSessionKeysAbpV11.from_dict,
        validator=attr.validators.instance_of(PropWirelessDeviceSessionKeysAbpV11),
        metadata={AttrMeta.PROPERTY_NAME: "SessionKeys"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys"""

@attr.s
class PropTaskDefinitionUpdateWirelessGatewayTaskCreate(Property):
    """
    AWS Object Type = "AWS::IoTWireless::TaskDefinition.UpdateWirelessGatewayTaskCreate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html

    Property Document:
    
    - ``p_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan
    - ``p_UpdateDataRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole
    - ``p_UpdateDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::TaskDefinition.UpdateWirelessGatewayTaskCreate"
    
    p_LoRaWAN: typing.Union['PropTaskDefinitionLoRaWANUpdateGatewayTaskCreate', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANUpdateGatewayTaskCreate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANUpdateGatewayTaskCreate)),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan"""
    p_UpdateDataRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateDataRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole"""
    p_UpdateDataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource"""

@attr.s
class PropTaskDefinitionLoRaWANUpdateGatewayTaskEntry(Property):
    """
    AWS Object Type = "AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html

    Property Document:
    
    - ``p_CurrentVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion
    - ``p_UpdateVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry"
    
    p_CurrentVersion: typing.Union['PropTaskDefinitionLoRaWANGatewayVersion', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANGatewayVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANGatewayVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "CurrentVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion"""
    p_UpdateVersion: typing.Union['PropTaskDefinitionLoRaWANGatewayVersion', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANGatewayVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANGatewayVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdateVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion"""

@attr.s
class PropWirelessDeviceAbpV10x(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.AbpV10x"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html

    Property Document:
    
    - ``rp_DevAddr``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr
    - ``rp_SessionKeys``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.AbpV10x"
    
    rp_DevAddr: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DevAddr"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr"""
    rp_SessionKeys: typing.Union['PropWirelessDeviceSessionKeysAbpV10x', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceSessionKeysAbpV10x.from_dict,
        validator=attr.validators.instance_of(PropWirelessDeviceSessionKeysAbpV10x),
        metadata={AttrMeta.PROPERTY_NAME: "SessionKeys"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys"""

@attr.s
class PropWirelessDeviceLoRaWANDevice(Property):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice.LoRaWANDevice"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html

    Property Document:
    
    - ``p_AbpV10x``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x
    - ``p_AbpV11``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11
    - ``p_DevEui``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui
    - ``p_DeviceProfileId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid
    - ``p_OtaaV10x``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x
    - ``p_OtaaV11``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11
    - ``p_ServiceProfileId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice.LoRaWANDevice"
    
    p_AbpV10x: typing.Union['PropWirelessDeviceAbpV10x', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceAbpV10x.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWirelessDeviceAbpV10x)),
        metadata={AttrMeta.PROPERTY_NAME: "AbpV10x"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x"""
    p_AbpV11: typing.Union['PropWirelessDeviceAbpV11', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceAbpV11.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWirelessDeviceAbpV11)),
        metadata={AttrMeta.PROPERTY_NAME: "AbpV11"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11"""
    p_DevEui: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DevEui"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui"""
    p_DeviceProfileId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceProfileId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid"""
    p_OtaaV10x: typing.Union['PropWirelessDeviceOtaaV10x', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceOtaaV10x.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWirelessDeviceOtaaV10x)),
        metadata={AttrMeta.PROPERTY_NAME: "OtaaV10x"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x"""
    p_OtaaV11: typing.Union['PropWirelessDeviceOtaaV11', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceOtaaV11.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWirelessDeviceOtaaV11)),
        metadata={AttrMeta.PROPERTY_NAME: "OtaaV11"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11"""
    p_ServiceProfileId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceProfileId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid"""


#--- Resource declaration ---

@attr.s
class ServiceProfile(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::ServiceProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html

    Property Document:
    
    - ``p_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::ServiceProfile"

    
    p_LoRaWAN: typing.Union['PropServiceProfileLoRaWANServiceProfile', dict] = attr.ib(
        default=None,
        converter=PropServiceProfileLoRaWANServiceProfile.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropServiceProfileLoRaWANServiceProfile)),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags"""

    
    @property
    def rv_LoRaWANUlRate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.UlRate")
    
    @property
    def rv_LoRaWANUlBucketSize(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.UlBucketSize")
    
    @property
    def rv_LoRaWANUlRatePolicy(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.UlRatePolicy")
    
    @property
    def rv_LoRaWANDlRate(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DlRate")
    
    @property
    def rv_LoRaWANDlBucketSize(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DlBucketSize")
    
    @property
    def rv_LoRaWANDlRatePolicy(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DlRatePolicy")
    
    @property
    def rv_LoRaWANDevStatusReqFreq(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DevStatusReqFreq")
    
    @property
    def rv_LoRaWANReportDevStatusBattery(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.ReportDevStatusBattery")
    
    @property
    def rv_LoRaWANReportDevStatusMargin(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.ReportDevStatusMargin")
    
    @property
    def rv_LoRaWANDrMin(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DrMin")
    
    @property
    def rv_LoRaWANDrMax(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.DrMax")
    
    @property
    def rv_LoRaWANChannelMask(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.ChannelMask")
    
    @property
    def rv_LoRaWANPrAllowed(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.PrAllowed")
    
    @property
    def rv_LoRaWANHrAllowed(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.HrAllowed")
    
    @property
    def rv_LoRaWANRaAllowed(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.RaAllowed")
    
    @property
    def rv_LoRaWANNwkGeoLoc(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.NwkGeoLoc")
    
    @property
    def rv_LoRaWANTargetPer(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.TargetPer")
    
    @property
    def rv_LoRaWANMinGwDiversity(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.MinGwDiversity")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#aws-resource-iotwireless-serviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class WirelessDevice(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessDevice"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html

    Property Document:
    
    - ``rp_DestinationName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
    - ``p_LastUplinkReceivedAt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
    - ``p_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
    - ``p_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessDevice"

    
    rp_DestinationName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description"""
    p_LastUplinkReceivedAt: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUplinkReceivedAt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat"""
    p_LoRaWAN: typing.Union['PropWirelessDeviceLoRaWANDevice', dict] = attr.ib(
        default=None,
        converter=PropWirelessDeviceLoRaWANDevice.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropWirelessDeviceLoRaWANDevice)),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name"""
    p_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#aws-resource-iotwireless-wirelessdevice-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#aws-resource-iotwireless-wirelessdevice-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_ThingName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#aws-resource-iotwireless-wirelessdevice-return-values"""
        return GetAtt(resource=self, attr_name="ThingName")
    

@attr.s
class DeviceProfile(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::DeviceProfile"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html

    Property Document:
    
    - ``p_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::DeviceProfile"

    
    p_LoRaWAN: typing.Union['PropDeviceProfileLoRaWANDeviceProfile', dict] = attr.ib(
        default=None,
        converter=PropDeviceProfileLoRaWANDeviceProfile.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeviceProfileLoRaWANDeviceProfile)),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#aws-resource-iotwireless-deviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#aws-resource-iotwireless-deviceprofile-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class MulticastGroup(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::MulticastGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html

    Property Document:
    
    - ``rp_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan
    - ``p_AssociateWirelessDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description
    - ``p_DisassociateWirelessDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::MulticastGroup"

    
    rp_LoRaWAN: typing.Union['PropMulticastGroupLoRaWAN', dict] = attr.ib(
        default=None,
        converter=PropMulticastGroupLoRaWAN.from_dict,
        validator=attr.validators.instance_of(PropMulticastGroupLoRaWAN),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan"""
    p_AssociateWirelessDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssociateWirelessDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description"""
    p_DisassociateWirelessDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DisassociateWirelessDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags"""

    
    @property
    def rv_LoRaWANNumberOfDevicesRequested(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#aws-resource-iotwireless-multicastgroup-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.NumberOfDevicesRequested")
    
    @property
    def rv_LoRaWANNumberOfDevicesInGroup(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#aws-resource-iotwireless-multicastgroup-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.NumberOfDevicesInGroup")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#aws-resource-iotwireless-multicastgroup-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#aws-resource-iotwireless-multicastgroup-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#aws-resource-iotwireless-multicastgroup-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    

@attr.s
class WirelessGateway(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::WirelessGateway"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html

    Property Document:
    
    - ``rp_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
    - ``p_LastUplinkReceivedAt``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
    - ``p_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::WirelessGateway"

    
    rp_LoRaWAN: typing.Union['PropWirelessGatewayLoRaWANGateway', dict] = attr.ib(
        default=None,
        converter=PropWirelessGatewayLoRaWANGateway.from_dict,
        validator=attr.validators.instance_of(PropWirelessGatewayLoRaWANGateway),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description"""
    p_LastUplinkReceivedAt: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastUplinkReceivedAt"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name"""
    p_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#aws-resource-iotwireless-wirelessgateway-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#aws-resource-iotwireless-wirelessgateway-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_ThingName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#aws-resource-iotwireless-wirelessgateway-return-values"""
        return GetAtt(resource=self, attr_name="ThingName")
    

@attr.s
class FuotaTask(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::FuotaTask"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html

    Property Document:
    
    - ``rp_FirmwareUpdateImage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage
    - ``rp_FirmwareUpdateRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole
    - ``rp_LoRaWAN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan
    - ``p_AssociateMulticastGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup
    - ``p_AssociateWirelessDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description
    - ``p_DisassociateMulticastGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup
    - ``p_DisassociateWirelessDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::FuotaTask"

    
    rp_FirmwareUpdateImage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirmwareUpdateImage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage"""
    rp_FirmwareUpdateRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirmwareUpdateRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole"""
    rp_LoRaWAN: typing.Union['PropFuotaTaskLoRaWAN', dict] = attr.ib(
        default=None,
        converter=PropFuotaTaskLoRaWAN.from_dict,
        validator=attr.validators.instance_of(PropFuotaTaskLoRaWAN),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWAN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan"""
    p_AssociateMulticastGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssociateMulticastGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup"""
    p_AssociateWirelessDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AssociateWirelessDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description"""
    p_DisassociateMulticastGroup: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DisassociateMulticastGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup"""
    p_DisassociateWirelessDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DisassociateWirelessDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags"""

    
    @property
    def rv_LoRaWANStartTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#aws-resource-iotwireless-fuotatask-return-values"""
        return GetAtt(resource=self, attr_name="LoRaWAN.StartTime")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#aws-resource-iotwireless-fuotatask-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#aws-resource-iotwireless-fuotatask-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_FuotaTaskStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#aws-resource-iotwireless-fuotatask-return-values"""
        return GetAtt(resource=self, attr_name="FuotaTaskStatus")
    

@attr.s
class Destination(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::Destination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html

    Property Document:
    
    - ``rp_Expression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
    - ``rp_ExpressionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::Destination"

    
    rp_Expression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Expression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression"""
    rp_ExpressionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ExpressionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#aws-resource-iotwireless-destination-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class PartnerAccount(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::PartnerAccount"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html

    Property Document:
    
    - ``p_AccountLinked``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
    - ``p_Fingerprint``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint
    - ``p_PartnerAccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
    - ``p_PartnerType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
    - ``p_Sidewalk``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
    - ``p_SidewalkUpdate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::PartnerAccount"

    
    p_AccountLinked: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AccountLinked"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked"""
    p_Fingerprint: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Fingerprint"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint"""
    p_PartnerAccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PartnerAccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid"""
    p_PartnerType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PartnerType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype"""
    p_Sidewalk: typing.Union['PropPartnerAccountSidewalkAccountInfo', dict] = attr.ib(
        default=None,
        converter=PropPartnerAccountSidewalkAccountInfo.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPartnerAccountSidewalkAccountInfo)),
        metadata={AttrMeta.PROPERTY_NAME: "Sidewalk"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk"""
    p_SidewalkUpdate: typing.Union['PropPartnerAccountSidewalkUpdateAccount', dict] = attr.ib(
        default=None,
        converter=PropPartnerAccountSidewalkUpdateAccount.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropPartnerAccountSidewalkUpdateAccount)),
        metadata={AttrMeta.PROPERTY_NAME: "SidewalkUpdate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags"""

    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#aws-resource-iotwireless-partneraccount-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    

@attr.s
class TaskDefinition(Resource):
    """
    AWS Object Type = "AWS::IoTWireless::TaskDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html

    Property Document:
    
    - ``rp_AutoCreateTasks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
    - ``p_LoRaWANUpdateGatewayTaskEntry``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
    - ``p_TaskDefinitionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
    - ``p_Update``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::IoTWireless::TaskDefinition"

    
    rp_AutoCreateTasks: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AutoCreateTasks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks"""
    p_LoRaWANUpdateGatewayTaskEntry: typing.Union['PropTaskDefinitionLoRaWANUpdateGatewayTaskEntry', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionLoRaWANUpdateGatewayTaskEntry.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionLoRaWANUpdateGatewayTaskEntry)),
        metadata={AttrMeta.PROPERTY_NAME: "LoRaWANUpdateGatewayTaskEntry"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name"""
    p_TaskDefinitionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TaskDefinitionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype"""
    p_Update: typing.Union['PropTaskDefinitionUpdateWirelessGatewayTaskCreate', dict] = attr.ib(
        default=None,
        converter=PropTaskDefinitionUpdateWirelessGatewayTaskCreate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTaskDefinitionUpdateWirelessGatewayTaskCreate)),
        metadata={AttrMeta.PROPERTY_NAME: "Update"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#aws-resource-iotwireless-taskdefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#aws-resource-iotwireless-taskdefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
