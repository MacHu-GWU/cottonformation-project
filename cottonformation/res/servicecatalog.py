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
class PropCloudFormationProvisionedProductProvisioningParameter(Property):
    """
    AWS Object Type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-value
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningParameter"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningparameter.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameter-value"""

@attr.s
class PropCloudFormationProvisionedProductProvisioningPreferences(Property):
    """
    AWS Object Type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html

    Property Document:
    
    - ``p_StackSetAccounts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts
    - ``p_StackSetFailureToleranceCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount
    - ``p_StackSetFailureTolerancePercentage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage
    - ``p_StackSetMaxConcurrencyCount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount
    - ``p_StackSetMaxConcurrencyPercentage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage
    - ``p_StackSetOperationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype
    - ``p_StackSetRegions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::CloudFormationProvisionedProduct.ProvisioningPreferences"
    
    p_StackSetAccounts: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetAccounts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetaccounts"""
    p_StackSetFailureToleranceCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetFailureToleranceCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancecount"""
    p_StackSetFailureTolerancePercentage: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetFailureTolerancePercentage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetfailuretolerancepercentage"""
    p_StackSetMaxConcurrencyCount: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetMaxConcurrencyCount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencycount"""
    p_StackSetMaxConcurrencyPercentage: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetMaxConcurrencyPercentage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetmaxconcurrencypercentage"""
    p_StackSetOperationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetOperationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetoperationtype"""
    p_StackSetRegions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StackSetRegions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences-stacksetregions"""

@attr.s
class PropServiceActionDefinitionParameter(Property):
    """
    AWS Object Type = "AWS::ServiceCatalog::ServiceAction.DefinitionParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-value
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::ServiceAction.DefinitionParameter"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-serviceaction-definitionparameter.html#cfn-servicecatalog-serviceaction-definitionparameter-value"""

@attr.s
class PropCloudFormationProductProvisioningArtifactProperties(Property):
    """
    AWS Object Type = "AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html

    Property Document:
    
    - ``rp_Info``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description
    - ``p_DisableTemplateValidation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::CloudFormationProduct.ProvisioningArtifactProperties"
    
    rp_Info: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "Info"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-info"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-description"""
    p_DisableTemplateValidation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DisableTemplateValidation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-disabletemplatevalidation"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicecatalog-cloudformationproduct-provisioningartifactproperties.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactproperties-name"""


#--- Resource declaration ---

@attr.s
class PortfolioShare(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::PortfolioShare"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html

    Property Document:
    
    - ``rp_AccountId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage
    - ``p_ShareTagOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-sharetagoptions
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::PortfolioShare"

    
    rp_AccountId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AccountId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-accountid"""
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-portfolioid"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-acceptlanguage"""
    p_ShareTagOptions: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ShareTagOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html#cfn-servicecatalog-portfolioshare-sharetagoptions"""

    

@attr.s
class ResourceUpdateConstraint(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::ResourceUpdateConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid
    - ``rp_TagUpdateOnProvisionedProduct``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::ResourceUpdateConstraint"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-productid"""
    rp_TagUpdateOnProvisionedProduct: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TagUpdateOnProvisionedProduct"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-tagupdateonprovisionedproduct"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html#cfn-servicecatalog-resourceupdateconstraint-description"""

    

@attr.s
class TagOption(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::TagOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value
    - ``p_Active``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::TagOption"

    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-value"""
    p_Active: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Active"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html#cfn-servicecatalog-tagoption-active"""

    

@attr.s
class CloudFormationProduct(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::CloudFormationProduct"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name
    - ``rp_Owner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner
    - ``rp_ProvisioningArtifactParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description
    - ``p_Distributor``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor
    - ``p_ReplaceProvisioningArtifacts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts
    - ``p_SupportDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription
    - ``p_SupportEmail``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail
    - ``p_SupportUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::CloudFormationProduct"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-name"""
    rp_Owner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Owner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-owner"""
    rp_ProvisioningArtifactParameters: typing.List[typing.Union['PropCloudFormationProductProvisioningArtifactProperties', dict]] = attr.ib(
        default=None,
        converter=PropCloudFormationProductProvisioningArtifactProperties.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCloudFormationProductProvisioningArtifactProperties), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningArtifactParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-provisioningartifactparameters"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-description"""
    p_Distributor: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Distributor"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-distributor"""
    p_ReplaceProvisioningArtifacts: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReplaceProvisioningArtifacts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-replaceprovisioningartifacts"""
    p_SupportDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportdescription"""
    p_SupportEmail: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportEmail"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supportemail"""
    p_SupportUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SupportUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-supporturl"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#cfn-servicecatalog-cloudformationproduct-tags"""

    
    @property
    def rv_ProductName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#aws-resource-servicecatalog-cloudformationproduct-return-values"""
        return GetAtt(resource=self, attr_name="ProductName")
    
    @property
    def rv_ProvisioningArtifactIds(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#aws-resource-servicecatalog-cloudformationproduct-return-values"""
        return GetAtt(resource=self, attr_name="ProvisioningArtifactIds")
    
    @property
    def rv_ProvisioningArtifactNames(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html#aws-resource-servicecatalog-cloudformationproduct-return-values"""
        return GetAtt(resource=self, attr_name="ProvisioningArtifactNames")
    

@attr.s
class PortfolioProductAssociation(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::PortfolioProductAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage
    - ``p_SourcePortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::PortfolioProductAssociation"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-productid"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-acceptlanguage"""
    p_SourcePortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html#cfn-servicecatalog-portfolioproductassociation-sourceportfolioid"""

    

@attr.s
class AcceptedPortfolioShare(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::AcceptedPortfolioShare"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::AcceptedPortfolioShare"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-portfolioid"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html#cfn-servicecatalog-acceptedportfolioshare-acceptlanguage"""

    

@attr.s
class ServiceAction(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::ServiceAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html

    Property Document:
    
    - ``rp_Definition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definition
    - ``rp_DefinitionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definitiontype
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-name
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-description
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::ServiceAction"

    
    rp_Definition: typing.List[typing.Union['PropServiceActionDefinitionParameter', dict]] = attr.ib(
        default=None,
        converter=PropServiceActionDefinitionParameter.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropServiceActionDefinitionParameter), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Definition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definition"""
    rp_DefinitionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefinitionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-definitiontype"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-name"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#cfn-servicecatalog-serviceaction-description"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceaction.html#aws-resource-servicecatalog-serviceaction-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class LaunchTemplateConstraint(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::LaunchTemplateConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid
    - ``rp_Rules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::LaunchTemplateConstraint"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-productid"""
    rp_Rules: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Rules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-rules"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html#cfn-servicecatalog-launchtemplateconstraint-description"""

    

@attr.s
class CloudFormationProvisionedProduct(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html

    Property Document:
    
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage
    - ``p_NotificationArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns
    - ``p_PathId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid
    - ``p_PathName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname
    - ``p_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid
    - ``p_ProductName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname
    - ``p_ProvisionedProductName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname
    - ``p_ProvisioningArtifactId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid
    - ``p_ProvisioningArtifactName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname
    - ``p_ProvisioningParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters
    - ``p_ProvisioningPreferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::CloudFormationProvisionedProduct"

    
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-acceptlanguage"""
    p_NotificationArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "NotificationArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-notificationarns"""
    p_PathId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PathId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathid"""
    p_PathName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PathName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-pathname"""
    p_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productid"""
    p_ProductName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProductName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-productname"""
    p_ProvisionedProductName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisionedProductName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisionedproductname"""
    p_ProvisioningArtifactId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningArtifactId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactid"""
    p_ProvisioningArtifactName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningArtifactName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningartifactname"""
    p_ProvisioningParameters: typing.List[typing.Union['PropCloudFormationProvisionedProductProvisioningParameter', dict]] = attr.ib(
        default=None,
        converter=PropCloudFormationProvisionedProductProvisioningParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCloudFormationProvisionedProductProvisioningParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningparameters"""
    p_ProvisioningPreferences: typing.Union['PropCloudFormationProvisionedProductProvisioningPreferences', dict] = attr.ib(
        default=None,
        converter=PropCloudFormationProvisionedProductProvisioningPreferences.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCloudFormationProvisionedProductProvisioningPreferences)),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningPreferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-provisioningpreferences"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#cfn-servicecatalog-cloudformationprovisionedproduct-tags"""

    
    @property
    def rv_ProvisionedProductId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#aws-resource-servicecatalog-cloudformationprovisionedproduct-return-values"""
        return GetAtt(resource=self, attr_name="ProvisionedProductId")
    
    @property
    def rv_RecordId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#aws-resource-servicecatalog-cloudformationprovisionedproduct-return-values"""
        return GetAtt(resource=self, attr_name="RecordId")
    
    @property
    def rv_CloudformationStackArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html#aws-resource-servicecatalog-cloudformationprovisionedproduct-return-values"""
        return GetAtt(resource=self, attr_name="CloudformationStackArn")
    

@attr.s
class Portfolio(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::Portfolio"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html

    Property Document:
    
    - ``rp_DisplayName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname
    - ``rp_ProviderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::Portfolio"

    
    rp_DisplayName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DisplayName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-displayname"""
    rp_ProviderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProviderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-providername"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#cfn-servicecatalog-portfolio-tags"""

    
    @property
    def rv_PortfolioName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html#aws-resource-servicecatalog-portfolio-return-values"""
        return GetAtt(resource=self, attr_name="PortfolioName")
    

@attr.s
class LaunchNotificationConstraint(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::LaunchNotificationConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html

    Property Document:
    
    - ``rp_NotificationArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::LaunchNotificationConstraint"

    
    rp_NotificationArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "NotificationArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-notificationarns"""
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-productid"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html#cfn-servicecatalog-launchnotificationconstraint-description"""

    

@attr.s
class ServiceActionAssociation(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::ServiceActionAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html

    Property Document:
    
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
    - ``rp_ProvisioningArtifactId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
    - ``rp_ServiceActionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::ServiceActionAssociation"

    
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid"""
    rp_ProvisioningArtifactId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProvisioningArtifactId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid"""
    rp_ServiceActionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceActionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid"""

    

@attr.s
class StackSetConstraint(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::StackSetConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html

    Property Document:
    
    - ``rp_AccountList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist
    - ``rp_AdminRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole
    - ``rp_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description
    - ``rp_ExecutionRole``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid
    - ``rp_RegionList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist
    - ``rp_StackInstanceControl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::StackSetConstraint"

    
    rp_AccountList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AccountList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-accountlist"""
    rp_AdminRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AdminRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-adminrole"""
    rp_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-description"""
    rp_ExecutionRole: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ExecutionRole"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-executionrole"""
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-productid"""
    rp_RegionList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RegionList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-regionlist"""
    rp_StackInstanceControl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "StackInstanceControl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-stackinstancecontrol"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html#cfn-servicecatalog-stacksetconstraint-acceptlanguage"""

    

@attr.s
class TagOptionAssociation(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::TagOptionAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html

    Property Document:
    
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid
    - ``rp_TagOptionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::TagOptionAssociation"

    
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-resourceid"""
    rp_TagOptionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TagOptionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html#cfn-servicecatalog-tagoptionassociation-tagoptionid"""

    

@attr.s
class PortfolioPrincipalAssociation(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid
    - ``rp_PrincipalARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn
    - ``rp_PrincipalType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::PortfolioPrincipalAssociation"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-portfolioid"""
    rp_PrincipalARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrincipalARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principalarn"""
    rp_PrincipalType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PrincipalType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-principaltype"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html#cfn-servicecatalog-portfolioprincipalassociation-acceptlanguage"""

    

@attr.s
class LaunchRoleConstraint(Resource):
    """
    AWS Object Type = "AWS::ServiceCatalog::LaunchRoleConstraint"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html

    Property Document:
    
    - ``rp_PortfolioId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid
    - ``rp_ProductId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid
    - ``p_AcceptLanguage``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description
    - ``p_LocalRoleName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn
    """
    AWS_OBJECT_TYPE = "AWS::ServiceCatalog::LaunchRoleConstraint"

    
    rp_PortfolioId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PortfolioId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-portfolioid"""
    rp_ProductId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ProductId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-productid"""
    p_AcceptLanguage: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AcceptLanguage"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-acceptlanguage"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-description"""
    p_LocalRoleName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LocalRoleName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-localrolename"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html#cfn-servicecatalog-launchroleconstraint-rolearn"""

    
