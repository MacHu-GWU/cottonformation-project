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
class PropEnvironmentFederationParameters(Property):
    """
    AWS Object Type = "AWS::FinSpace::Environment.FederationParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html

    Property Document:
    
    - ``p_ApplicationCallBackURL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-applicationcallbackurl
    - ``p_AttributeMap``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-attributemap
    - ``p_FederationProviderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationprovidername
    - ``p_FederationURN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationurn
    - ``p_SamlMetadataDocument``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadatadocument
    - ``p_SamlMetadataURL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadataurl
    """
    AWS_OBJECT_TYPE = "AWS::FinSpace::Environment.FederationParameters"
    
    p_ApplicationCallBackURL: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ApplicationCallBackURL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-applicationcallbackurl"""
    p_AttributeMap: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AttributeMap"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-attributemap"""
    p_FederationProviderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FederationProviderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationprovidername"""
    p_FederationURN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FederationURN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationurn"""
    p_SamlMetadataDocument: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SamlMetadataDocument"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadatadocument"""
    p_SamlMetadataURL: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SamlMetadataURL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadataurl"""

@attr.s
class PropEnvironmentSuperuserParameters(Property):
    """
    AWS Object Type = "AWS::FinSpace::Environment.SuperuserParameters"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html

    Property Document:
    
    - ``p_EmailAddress``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-emailaddress
    - ``p_FirstName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-firstname
    - ``p_LastName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-lastname
    """
    AWS_OBJECT_TYPE = "AWS::FinSpace::Environment.SuperuserParameters"
    
    p_EmailAddress: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EmailAddress"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-emailaddress"""
    p_FirstName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FirstName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-firstname"""
    p_LastName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LastName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-lastname"""


#--- Resource declaration ---

@attr.s
class Environment(Resource):
    """
    AWS Object Type = "AWS::FinSpace::Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name
    - ``p_DataBundles``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-databundles
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description
    - ``p_FederationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode
    - ``p_FederationParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid
    - ``p_SuperuserParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-superuserparameters
    """
    AWS_OBJECT_TYPE = "AWS::FinSpace::Environment"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name"""
    p_DataBundles: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DataBundles"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-databundles"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description"""
    p_FederationMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FederationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode"""
    p_FederationParameters: typing.Union['PropEnvironmentFederationParameters', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentFederationParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentFederationParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "FederationParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid"""
    p_SuperuserParameters: typing.Union['PropEnvironmentSuperuserParameters', dict] = attr.ib(
        default=None,
        converter=PropEnvironmentSuperuserParameters.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEnvironmentSuperuserParameters)),
        metadata={AttrMeta.PROPERTY_NAME: "SuperuserParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-superuserparameters"""

    
    @property
    def rv_EnvironmentId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="EnvironmentId")
    
    @property
    def rv_AwsAccountId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="AwsAccountId")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_EnvironmentUrl(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="EnvironmentUrl")
    
    @property
    def rv_EnvironmentArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="EnvironmentArn")
    
    @property
    def rv_SageMakerStudioDomainUrl(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="SageMakerStudioDomainUrl")
    
    @property
    def rv_DedicatedServiceAccountId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#aws-resource-finspace-environment-return-values"""
        return GetAtt(resource=self, attr_name="DedicatedServiceAccountId")
    
