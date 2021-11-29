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
class PropDatabaseRelationalDatabaseParameter(Property):
    """
    AWS Object Type = "AWS::Lightsail::Database.RelationalDatabaseParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html

    Property Document:
    
    - ``p_AllowedValues``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues
    - ``p_ApplyMethod``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod
    - ``p_ApplyType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype
    - ``p_DataType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description
    - ``p_IsModifiable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable
    - ``p_ParameterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername
    - ``p_ParameterValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Database.RelationalDatabaseParameter"
    
    p_AllowedValues: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowedValues"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-allowedvalues"""
    p_ApplyMethod: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplyMethod"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applymethod"""
    p_ApplyType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplyType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-applytype"""
    p_DataType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-datatype"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-description"""
    p_IsModifiable: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsModifiable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-ismodifiable"""
    p_ParameterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametername"""
    p_ParameterValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html#cfn-lightsail-database-relationaldatabaseparameter-parametervalue"""

@attr.s
class PropInstanceMonthlyTransfer(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.MonthlyTransfer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html

    Property Document:
    
    - ``p_GbPerMonthAllocated``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.MonthlyTransfer"
    
    p_GbPerMonthAllocated: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GbPerMonthAllocated"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html#cfn-lightsail-instance-monthlytransfer-gbpermonthallocated"""

@attr.s
class PropInstancePort(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.Port"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html

    Property Document:
    
    - ``p_AccessDirection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection
    - ``p_AccessFrom``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom
    - ``p_AccessType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype
    - ``p_CidrListAliases``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases
    - ``p_Cidrs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs
    - ``p_CommonName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname
    - ``p_FromPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport
    - ``p_Ipv6Cidrs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs
    - ``p_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol
    - ``p_ToPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.Port"
    
    p_AccessDirection: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessDirection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessdirection"""
    p_AccessFrom: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessFrom"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accessfrom"""
    p_AccessType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-accesstype"""
    p_CidrListAliases: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CidrListAliases"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrlistaliases"""
    p_Cidrs: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Cidrs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-cidrs"""
    p_CommonName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CommonName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-commonname"""
    p_FromPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "FromPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-fromport"""
    p_Ipv6Cidrs: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Ipv6Cidrs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-ipv6cidrs"""
    p_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-protocol"""
    p_ToPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ToPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html#cfn-lightsail-instance-port-toport"""

@attr.s
class PropInstanceAutoSnapshotAddOn(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.AutoSnapshotAddOn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html

    Property Document:
    
    - ``p_SnapshotTimeOfDay``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.AutoSnapshotAddOn"
    
    p_SnapshotTimeOfDay: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotTimeOfDay"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html#cfn-lightsail-instance-autosnapshotaddon-snapshottimeofday"""

@attr.s
class PropDiskAutoSnapshotAddOn(Property):
    """
    AWS Object Type = "AWS::Lightsail::Disk.AutoSnapshotAddOn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html

    Property Document:
    
    - ``p_SnapshotTimeOfDay``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Disk.AutoSnapshotAddOn"
    
    p_SnapshotTimeOfDay: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SnapshotTimeOfDay"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-autosnapshotaddon.html#cfn-lightsail-disk-autosnapshotaddon-snapshottimeofday"""

@attr.s
class PropInstanceDisk(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.Disk"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html

    Property Document:
    
    - ``rp_DiskName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname
    - ``rp_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path
    - ``p_AttachedTo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto
    - ``p_AttachmentState``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate
    - ``p_IOPS``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops
    - ``p_IsSystemDisk``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk
    - ``p_SizeInGb``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.Disk"
    
    rp_DiskName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DiskName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-diskname"""
    rp_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-path"""
    p_AttachedTo: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttachedTo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachedto"""
    p_AttachmentState: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttachmentState"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-attachmentstate"""
    p_IOPS: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "IOPS"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-iops"""
    p_IsSystemDisk: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IsSystemDisk"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-issystemdisk"""
    p_SizeInGb: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInGb"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html#cfn-lightsail-instance-disk-sizeingb"""

@attr.s
class PropInstanceHardware(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.Hardware"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html

    Property Document:
    
    - ``p_CpuCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount
    - ``p_Disks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks
    - ``p_RamSizeInGb``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.Hardware"
    
    p_CpuCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "CpuCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-cpucount"""
    p_Disks: typing.List[typing.Union['PropInstanceDisk', dict]] = attr.ib(
        default=None,
        converter=PropInstanceDisk.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInstanceDisk), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Disks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-disks"""
    p_RamSizeInGb: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "RamSizeInGb"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html#cfn-lightsail-instance-hardware-ramsizeingb"""

@attr.s
class PropInstanceLocation(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.Location"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html

    Property Document:
    
    - ``p_AvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone
    - ``p_RegionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.Location"
    
    p_AvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-availabilityzone"""
    p_RegionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RegionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-location.html#cfn-lightsail-instance-location-regionname"""

@attr.s
class PropInstanceNetworking(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.Networking"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html

    Property Document:
    
    - ``rp_Ports``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports
    - ``p_MonthlyTransfer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-monthlytransfer
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.Networking"
    
    rp_Ports: typing.List[typing.Union['PropInstancePort', dict]] = attr.ib(
        default=None,
        converter=PropInstancePort.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInstancePort), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Ports"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-ports"""
    p_MonthlyTransfer: typing.Union['PropInstanceMonthlyTransfer', dict] = attr.ib(
        default=None,
        converter=PropInstanceMonthlyTransfer.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceMonthlyTransfer)),
        metadata={AttrMeta.PROPERTY_NAME: "MonthlyTransfer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html#cfn-lightsail-instance-networking-monthlytransfer"""

@attr.s
class PropInstanceState(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.State"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html

    Property Document:
    
    - ``p_Code``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.State"
    
    p_Code: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Code"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-code"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-state.html#cfn-lightsail-instance-state-name"""

@attr.s
class PropDiskAddOn(Property):
    """
    AWS Object Type = "AWS::Lightsail::Disk.AddOn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html

    Property Document:
    
    - ``rp_AddOnType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype
    - ``p_AutoSnapshotAddOnRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Disk.AddOn"
    
    rp_AddOnType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AddOnType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-addontype"""
    p_AutoSnapshotAddOnRequest: typing.Union['PropDiskAutoSnapshotAddOn', dict] = attr.ib(
        default=None,
        converter=PropDiskAutoSnapshotAddOn.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDiskAutoSnapshotAddOn)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoSnapshotAddOnRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-autosnapshotaddonrequest"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-disk-addon.html#cfn-lightsail-disk-addon-status"""

@attr.s
class PropInstanceAddOn(Property):
    """
    AWS Object Type = "AWS::Lightsail::Instance.AddOn"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html

    Property Document:
    
    - ``rp_AddOnType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype
    - ``p_AutoSnapshotAddOnRequest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest
    - ``p_Status``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance.AddOn"
    
    rp_AddOnType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AddOnType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-addontype"""
    p_AutoSnapshotAddOnRequest: typing.Union['PropInstanceAutoSnapshotAddOn', dict] = attr.ib(
        default=None,
        converter=PropInstanceAutoSnapshotAddOn.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceAutoSnapshotAddOn)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoSnapshotAddOnRequest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-autosnapshotaddonrequest"""
    p_Status: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Status"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html#cfn-lightsail-instance-addon-status"""


#--- Resource declaration ---

@attr.s
class Database(Resource):
    """
    AWS Object Type = "AWS::Lightsail::Database"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html

    Property Document:
    
    - ``rp_MasterDatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename
    - ``rp_MasterUsername``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername
    - ``rp_RelationalDatabaseBlueprintId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid
    - ``rp_RelationalDatabaseBundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid
    - ``rp_RelationalDatabaseName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename
    - ``p_AvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone
    - ``p_BackupRetention``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention
    - ``p_CaCertificateIdentifier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier
    - ``p_MasterUserPassword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword
    - ``p_PreferredBackupWindow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow
    - ``p_PreferredMaintenanceWindow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow
    - ``p_PubliclyAccessible``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible
    - ``p_RelationalDatabaseParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters
    - ``p_RotateMasterUserPassword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Database"

    
    rp_MasterDatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MasterDatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterdatabasename"""
    rp_MasterUsername: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUsername"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masterusername"""
    rp_RelationalDatabaseBlueprintId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RelationalDatabaseBlueprintId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseblueprintid"""
    rp_RelationalDatabaseBundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RelationalDatabaseBundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasebundleid"""
    rp_RelationalDatabaseName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RelationalDatabaseName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabasename"""
    p_AvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-availabilityzone"""
    p_BackupRetention: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "BackupRetention"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-backupretention"""
    p_CaCertificateIdentifier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CaCertificateIdentifier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-cacertificateidentifier"""
    p_MasterUserPassword: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MasterUserPassword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-masteruserpassword"""
    p_PreferredBackupWindow: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PreferredBackupWindow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredbackupwindow"""
    p_PreferredMaintenanceWindow: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PreferredMaintenanceWindow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-preferredmaintenancewindow"""
    p_PubliclyAccessible: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "PubliclyAccessible"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-publiclyaccessible"""
    p_RelationalDatabaseParameters: typing.List[typing.Union['PropDatabaseRelationalDatabaseParameter', dict]] = attr.ib(
        default=None,
        converter=PropDatabaseRelationalDatabaseParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDatabaseRelationalDatabaseParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "RelationalDatabaseParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-relationaldatabaseparameters"""
    p_RotateMasterUserPassword: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "RotateMasterUserPassword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-rotatemasteruserpassword"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#cfn-lightsail-database-tags"""

    
    @property
    def rv_DatabaseArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html#aws-resource-lightsail-database-return-values"""
        return GetAtt(resource=self, attr_name="DatabaseArn")
    

@attr.s
class Instance(Resource):
    """
    AWS Object Type = "AWS::Lightsail::Instance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html

    Property Document:
    
    - ``rp_BlueprintId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid
    - ``rp_BundleId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid
    - ``rp_InstanceName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename
    - ``p_AddOns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons
    - ``p_AvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone
    - ``p_Hardware``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware
    - ``p_KeyPairName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname
    - ``p_Networking``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking
    - ``p_UserData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Instance"

    
    rp_BlueprintId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BlueprintId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-blueprintid"""
    rp_BundleId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BundleId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-bundleid"""
    rp_InstanceName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "InstanceName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-instancename"""
    p_AddOns: typing.List[typing.Union['PropInstanceAddOn', dict]] = attr.ib(
        default=None,
        converter=PropInstanceAddOn.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropInstanceAddOn), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AddOns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-addons"""
    p_AvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-availabilityzone"""
    p_Hardware: typing.Union['PropInstanceHardware', dict] = attr.ib(
        default=None,
        converter=PropInstanceHardware.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceHardware)),
        metadata={AttrMeta.PROPERTY_NAME: "Hardware"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-hardware"""
    p_KeyPairName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KeyPairName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-keypairname"""
    p_Networking: typing.Union['PropInstanceNetworking', dict] = attr.ib(
        default=None,
        converter=PropInstanceNetworking.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropInstanceNetworking)),
        metadata={AttrMeta.PROPERTY_NAME: "Networking"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-networking"""
    p_UserData: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UserData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-userdata"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#cfn-lightsail-instance-tags"""

    
    @property
    def rv_SupportCode(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="SupportCode")
    
    @property
    def rv_ResourceType(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="ResourceType")
    
    @property
    def rv_IsStaticIp(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="IsStaticIp")
    
    @property
    def rv_PrivateIpAddress(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="PrivateIpAddress")
    
    @property
    def rv_PublicIpAddress(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="PublicIpAddress")
    
    @property
    def rv_LocationAvailabilityZone(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="Location.AvailabilityZone")
    
    @property
    def rv_LocationRegionName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="Location.RegionName")
    
    @property
    def rv_HardwareCpuCount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="Hardware.CpuCount")
    
    @property
    def rv_HardwareRamSizeInGb(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="Hardware.RamSizeInGb")
    
    @property
    def rv_StateCode(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="State.Code")
    
    @property
    def rv_StateName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="State.Name")
    
    @property
    def rv_NetworkingMonthlyTransferGbPerMonthAllocated(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="Networking.MonthlyTransfer.GbPerMonthAllocated")
    
    @property
    def rv_UserName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="UserName")
    
    @property
    def rv_SshKeyName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="SshKeyName")
    
    @property
    def rv_InstanceArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html#aws-resource-lightsail-instance-return-values"""
        return GetAtt(resource=self, attr_name="InstanceArn")
    

@attr.s
class Disk(Resource):
    """
    AWS Object Type = "AWS::Lightsail::Disk"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html

    Property Document:
    
    - ``rp_DiskName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname
    - ``rp_SizeInGb``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb
    - ``p_AddOns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons
    - ``p_AvailabilityZone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::Disk"

    
    rp_DiskName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DiskName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-diskname"""
    rp_SizeInGb: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "SizeInGb"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-sizeingb"""
    p_AddOns: typing.List[typing.Union['PropDiskAddOn', dict]] = attr.ib(
        default=None,
        converter=PropDiskAddOn.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDiskAddOn), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AddOns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-addons"""
    p_AvailabilityZone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AvailabilityZone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-availabilityzone"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#cfn-lightsail-disk-tags"""

    
    @property
    def rv_DiskArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="DiskArn")
    
    @property
    def rv_SupportCode(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="SupportCode")
    
    @property
    def rv_ResourceType(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="ResourceType")
    
    @property
    def rv_State(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="State")
    
    @property
    def rv_AttachmentState(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="AttachmentState")
    
    @property
    def rv_Iops(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="Iops")
    
    @property
    def rv_IsAttached(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="IsAttached")
    
    @property
    def rv_Path(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="Path")
    
    @property
    def rv_AttachedTo(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html#aws-resource-lightsail-disk-return-values"""
        return GetAtt(resource=self, attr_name="AttachedTo")
    

@attr.s
class StaticIp(Resource):
    """
    AWS Object Type = "AWS::Lightsail::StaticIp"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html

    Property Document:
    
    - ``rp_StaticIpName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname
    - ``p_AttachedTo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto
    """
    AWS_OBJECT_TYPE = "AWS::Lightsail::StaticIp"

    
    rp_StaticIpName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StaticIpName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-staticipname"""
    p_AttachedTo: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AttachedTo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#cfn-lightsail-staticip-attachedto"""

    
    @property
    def rv_IsAttached(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#aws-resource-lightsail-staticip-return-values"""
        return GetAtt(resource=self, attr_name="IsAttached")
    
    @property
    def rv_IpAddress(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#aws-resource-lightsail-staticip-return-values"""
        return GetAtt(resource=self, attr_name="IpAddress")
    
    @property
    def rv_StaticIpArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html#aws-resource-lightsail-staticip-return-values"""
        return GetAtt(resource=self, attr_name="StaticIpArn")
    
