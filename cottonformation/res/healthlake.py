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
class PropFHIRDatastorePreloadDataConfig(Property):
    """
    AWS Object Type = "AWS::HealthLake::FHIRDatastore.PreloadDataConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html

    Property Document:
    
    - ``rp_PreloadDataType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype
    """
    AWS_OBJECT_TYPE = "AWS::HealthLake::FHIRDatastore.PreloadDataConfig"
    
    rp_PreloadDataType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PreloadDataType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype"""

@attr.s
class PropFHIRDatastoreKmsEncryptionConfig(Property):
    """
    AWS Object Type = "AWS::HealthLake::FHIRDatastore.KmsEncryptionConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html

    Property Document:
    
    - ``rp_CmkType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::HealthLake::FHIRDatastore.KmsEncryptionConfig"
    
    rp_CmkType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CmkType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid"""

@attr.s
class PropFHIRDatastoreSseConfiguration(Property):
    """
    AWS Object Type = "AWS::HealthLake::FHIRDatastore.SseConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html

    Property Document:
    
    - ``rp_KmsEncryptionConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig
    """
    AWS_OBJECT_TYPE = "AWS::HealthLake::FHIRDatastore.SseConfiguration"
    
    rp_KmsEncryptionConfig: typing.Union['PropFHIRDatastoreKmsEncryptionConfig', dict] = attr.ib(
        default=None,
        converter=PropFHIRDatastoreKmsEncryptionConfig.from_dict,
        validator=attr.validators.instance_of(PropFHIRDatastoreKmsEncryptionConfig),
        metadata={AttrMeta.PROPERTY_NAME: "KmsEncryptionConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig"""


#--- Resource declaration ---

@attr.s
class FHIRDatastore(Resource):
    """
    AWS Object Type = "AWS::HealthLake::FHIRDatastore"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html

    Property Document:
    
    - ``rp_DatastoreTypeVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion
    - ``p_DatastoreName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename
    - ``p_PreloadDataConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig
    - ``p_SseConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags
    """
    AWS_OBJECT_TYPE = "AWS::HealthLake::FHIRDatastore"

    
    rp_DatastoreTypeVersion: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DatastoreTypeVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion"""
    p_DatastoreName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatastoreName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename"""
    p_PreloadDataConfig: typing.Union['PropFHIRDatastorePreloadDataConfig', dict] = attr.ib(
        default=None,
        converter=PropFHIRDatastorePreloadDataConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFHIRDatastorePreloadDataConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "PreloadDataConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig"""
    p_SseConfiguration: typing.Union['PropFHIRDatastoreSseConfiguration', dict] = attr.ib(
        default=None,
        converter=PropFHIRDatastoreSseConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFHIRDatastoreSseConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SseConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags"""

    
    @property
    def rv_DatastoreArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#aws-resource-healthlake-fhirdatastore-return-values"""
        return GetAtt(resource=self, attr_name="DatastoreArn")
    
    @property
    def rv_DatastoreEndpoint(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#aws-resource-healthlake-fhirdatastore-return-values"""
        return GetAtt(resource=self, attr_name="DatastoreEndpoint")
    
    @property
    def rv_DatastoreId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#aws-resource-healthlake-fhirdatastore-return-values"""
        return GetAtt(resource=self, attr_name="DatastoreId")
    
    @property
    def rv_DatastoreStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#aws-resource-healthlake-fhirdatastore-return-values"""
        return GetAtt(resource=self, attr_name="DatastoreStatus")
    
