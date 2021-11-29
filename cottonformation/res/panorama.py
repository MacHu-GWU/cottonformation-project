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
class PropApplicationInstanceManifestPayload(Property):
    """
    AWS Object Type = "AWS::Panorama::ApplicationInstance.ManifestPayload"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html

    Property Document:
    
    - ``p_PayloadData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html#cfn-panorama-applicationinstance-manifestpayload-payloaddata
    """
    AWS_OBJECT_TYPE = "AWS::Panorama::ApplicationInstance.ManifestPayload"
    
    p_PayloadData: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PayloadData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestpayload.html#cfn-panorama-applicationinstance-manifestpayload-payloaddata"""

@attr.s
class PropApplicationInstanceManifestOverridesPayload(Property):
    """
    AWS Object Type = "AWS::Panorama::ApplicationInstance.ManifestOverridesPayload"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html

    Property Document:
    
    - ``p_PayloadData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata
    """
    AWS_OBJECT_TYPE = "AWS::Panorama::ApplicationInstance.ManifestOverridesPayload"
    
    p_PayloadData: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PayloadData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-panorama-applicationinstance-manifestoverridespayload.html#cfn-panorama-applicationinstance-manifestoverridespayload-payloaddata"""


#--- Resource declaration ---

@attr.s
class Package(Resource):
    """
    AWS Object Type = "AWS::Panorama::Package"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html

    Property Document:
    
    - ``rp_PackageName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-packagename
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-tags
    """
    AWS_OBJECT_TYPE = "AWS::Panorama::Package"

    
    rp_PackageName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackageName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-packagename"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#cfn-panorama-package-tags"""

    
    @property
    def rv_PackageId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#aws-resource-panorama-package-return-values"""
        return GetAtt(resource=self, attr_name="PackageId")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#aws-resource-panorama-package-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-package.html#aws-resource-panorama-package-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    

@attr.s
class PackageVersion(Resource):
    """
    AWS Object Type = "AWS::Panorama::PackageVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html

    Property Document:
    
    - ``rp_PackageId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageid
    - ``rp_PackageVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageversion
    - ``rp_PatchVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-patchversion
    - ``p_MarkLatest``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-marklatest
    - ``p_OwnerAccount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-owneraccount
    - ``p_UpdatedLatestPatchVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-updatedlatestpatchversion
    """
    AWS_OBJECT_TYPE = "AWS::Panorama::PackageVersion"

    
    rp_PackageId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackageId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageid"""
    rp_PackageVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PackageVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-packageversion"""
    rp_PatchVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PatchVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-patchversion"""
    p_MarkLatest: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "MarkLatest"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-marklatest"""
    p_OwnerAccount: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerAccount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-owneraccount"""
    p_UpdatedLatestPatchVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "UpdatedLatestPatchVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#cfn-panorama-packageversion-updatedlatestpatchversion"""

    
    @property
    def rv_PackageArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="PackageArn")
    
    @property
    def rv_IsLatestPatch(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="IsLatestPatch")
    
    @property
    def rv_PackageName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="PackageName")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_StatusDescription(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="StatusDescription")
    
    @property
    def rv_RegisteredTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-packageversion.html#aws-resource-panorama-packageversion-return-values"""
        return GetAtt(resource=self, attr_name="RegisteredTime")
    

@attr.s
class ApplicationInstance(Resource):
    """
    AWS Object Type = "AWS::Panorama::ApplicationInstance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html

    Property Document:
    
    - ``rp_DefaultRuntimeContextDevice``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-defaultruntimecontextdevice
    - ``rp_ManifestPayload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestpayload
    - ``p_ApplicationInstanceIdToReplace``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-applicationinstanceidtoreplace
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-description
    - ``p_DeviceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-deviceid
    - ``p_ManifestOverridesPayload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestoverridespayload
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-name
    - ``p_RuntimeRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-runtimerolearn
    - ``p_StatusFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-statusfilter
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-tags
    """
    AWS_OBJECT_TYPE = "AWS::Panorama::ApplicationInstance"

    
    rp_DefaultRuntimeContextDevice: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultRuntimeContextDevice"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-defaultruntimecontextdevice"""
    rp_ManifestPayload: typing.Union['PropApplicationInstanceManifestPayload', dict] = attr.ib(
        default=None,
        converter=PropApplicationInstanceManifestPayload.from_dict,
        validator=attr.validators.instance_of(PropApplicationInstanceManifestPayload),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestPayload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestpayload"""
    p_ApplicationInstanceIdToReplace: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationInstanceIdToReplace"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-applicationinstanceidtoreplace"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-description"""
    p_DeviceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-deviceid"""
    p_ManifestOverridesPayload: typing.Union['PropApplicationInstanceManifestOverridesPayload', dict] = attr.ib(
        default=None,
        converter=PropApplicationInstanceManifestOverridesPayload.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropApplicationInstanceManifestOverridesPayload)),
        metadata={AttrMeta.PROPERTY_NAME: "ManifestOverridesPayload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-manifestoverridespayload"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-name"""
    p_RuntimeRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuntimeRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-runtimerolearn"""
    p_StatusFilter: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StatusFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-statusfilter"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#cfn-panorama-applicationinstance-tags"""

    
    @property
    def rv_DefaultRuntimeContextDeviceName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="DefaultRuntimeContextDeviceName")
    
    @property
    def rv_ApplicationInstanceId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="ApplicationInstanceId")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_HealthStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="HealthStatus")
    
    @property
    def rv_StatusDescription(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="StatusDescription")
    
    @property
    def rv_CreatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="CreatedTime")
    
    @property
    def rv_LastUpdatedTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedTime")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-panorama-applicationinstance.html#aws-resource-panorama-applicationinstance-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
