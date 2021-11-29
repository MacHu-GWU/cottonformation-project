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
class PropAssistantAssociationAssociationData(Property):
    """
    AWS Object Type = "AWS::Wisdom::AssistantAssociation.AssociationData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html

    Property Document:
    
    - ``rp_KnowledgeBaseId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::AssistantAssociation.AssociationData"
    
    rp_KnowledgeBaseId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KnowledgeBaseId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid"""

@attr.s
class PropKnowledgeBaseAppIntegrationsConfiguration(Property):
    """
    AWS Object Type = "AWS::Wisdom::KnowledgeBase.AppIntegrationsConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html

    Property Document:
    
    - ``rp_AppIntegrationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn
    - ``rp_ObjectFields``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::KnowledgeBase.AppIntegrationsConfiguration"
    
    rp_AppIntegrationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AppIntegrationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn"""
    rp_ObjectFields: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectFields"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields"""

@attr.s
class PropKnowledgeBaseServerSideEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::Wisdom::KnowledgeBase.ServerSideEncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html

    Property Document:
    
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::KnowledgeBase.ServerSideEncryptionConfiguration"
    
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid"""

@attr.s
class PropKnowledgeBaseRenderingConfiguration(Property):
    """
    AWS Object Type = "AWS::Wisdom::KnowledgeBase.RenderingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html

    Property Document:
    
    - ``p_TemplateUri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::KnowledgeBase.RenderingConfiguration"
    
    p_TemplateUri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateUri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri"""

@attr.s
class PropAssistantServerSideEncryptionConfiguration(Property):
    """
    AWS Object Type = "AWS::Wisdom::Assistant.ServerSideEncryptionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html

    Property Document:
    
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::Assistant.ServerSideEncryptionConfiguration"
    
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid"""

@attr.s
class PropKnowledgeBaseSourceConfiguration(Property):
    """
    AWS Object Type = "AWS::Wisdom::KnowledgeBase.SourceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html

    Property Document:
    
    - ``p_AppIntegrations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::KnowledgeBase.SourceConfiguration"
    
    p_AppIntegrations: typing.Union['PropKnowledgeBaseAppIntegrationsConfiguration', dict] = attr.ib(
        default=None,
        converter=PropKnowledgeBaseAppIntegrationsConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropKnowledgeBaseAppIntegrationsConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "AppIntegrations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations"""


#--- Resource declaration ---

@attr.s
class KnowledgeBase(Resource):
    """
    AWS Object Type = "AWS::Wisdom::KnowledgeBase"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html

    Property Document:
    
    - ``rp_KnowledgeBaseType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description
    - ``p_RenderingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration
    - ``p_ServerSideEncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration
    - ``p_SourceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::KnowledgeBase"

    
    rp_KnowledgeBaseType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KnowledgeBaseType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description"""
    p_RenderingConfiguration: typing.Union['PropKnowledgeBaseRenderingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropKnowledgeBaseRenderingConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropKnowledgeBaseRenderingConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "RenderingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration"""
    p_ServerSideEncryptionConfiguration: typing.Union['PropKnowledgeBaseServerSideEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropKnowledgeBaseServerSideEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropKnowledgeBaseServerSideEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerSideEncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration"""
    p_SourceConfiguration: typing.Union['PropKnowledgeBaseSourceConfiguration', dict] = attr.ib(
        default=None,
        converter=PropKnowledgeBaseSourceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropKnowledgeBaseSourceConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags"""

    
    @property
    def rv_KnowledgeBaseArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#aws-resource-wisdom-knowledgebase-return-values"""
        return GetAtt(resource=self, attr_name="KnowledgeBaseArn")
    
    @property
    def rv_KnowledgeBaseId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#aws-resource-wisdom-knowledgebase-return-values"""
        return GetAtt(resource=self, attr_name="KnowledgeBaseId")
    

@attr.s
class AssistantAssociation(Resource):
    """
    AWS Object Type = "AWS::Wisdom::AssistantAssociation"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html

    Property Document:
    
    - ``rp_AssistantId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid
    - ``rp_Association``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association
    - ``rp_AssociationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::AssistantAssociation"

    
    rp_AssistantId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AssistantId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid"""
    rp_Association: typing.Union['PropAssistantAssociationAssociationData', dict] = attr.ib(
        default=None,
        converter=PropAssistantAssociationAssociationData.from_dict,
        validator=attr.validators.instance_of(PropAssistantAssociationAssociationData),
        metadata={AttrMeta.PROPERTY_NAME: "Association"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association"""
    rp_AssociationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AssociationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags"""

    
    @property
    def rv_AssistantAssociationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#aws-resource-wisdom-assistantassociation-return-values"""
        return GetAtt(resource=self, attr_name="AssistantAssociationArn")
    
    @property
    def rv_AssistantArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#aws-resource-wisdom-assistantassociation-return-values"""
        return GetAtt(resource=self, attr_name="AssistantArn")
    
    @property
    def rv_AssistantAssociationId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#aws-resource-wisdom-assistantassociation-return-values"""
        return GetAtt(resource=self, attr_name="AssistantAssociationId")
    

@attr.s
class Assistant(Resource):
    """
    AWS Object Type = "AWS::Wisdom::Assistant"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description
    - ``p_ServerSideEncryptionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags
    """
    AWS_OBJECT_TYPE = "AWS::Wisdom::Assistant"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description"""
    p_ServerSideEncryptionConfiguration: typing.Union['PropAssistantServerSideEncryptionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropAssistantServerSideEncryptionConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropAssistantServerSideEncryptionConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerSideEncryptionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags"""

    
    @property
    def rv_AssistantArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#aws-resource-wisdom-assistant-return-values"""
        return GetAtt(resource=self, attr_name="AssistantArn")
    
    @property
    def rv_AssistantId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#aws-resource-wisdom-assistant-return-values"""
        return GetAtt(resource=self, attr_name="AssistantId")
    
