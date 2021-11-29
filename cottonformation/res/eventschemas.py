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
class PropSchemaTagsEntry(Property):
    """
    AWS Object Type = "AWS::EventSchemas::Schema.TagsEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Schema.TagsEntry"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value"""

@attr.s
class PropDiscovererTagsEntry(Property):
    """
    AWS Object Type = "AWS::EventSchemas::Discoverer.TagsEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Discoverer.TagsEntry"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value"""

@attr.s
class PropRegistryTagsEntry(Property):
    """
    AWS Object Type = "AWS::EventSchemas::Registry.TagsEntry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html

    Property Document:
    
    - ``rp_Key``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Registry.TagsEntry"
    
    rp_Key: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Key"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key"""
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value"""


#--- Resource declaration ---

@attr.s
class Schema(Resource):
    """
    AWS Object Type = "AWS::EventSchemas::Schema"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html

    Property Document:
    
    - ``rp_Content``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
    - ``rp_RegistryName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
    - ``p_SchemaName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Schema"

    
    rp_Content: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Content"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content"""
    rp_RegistryName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description"""
    p_SchemaName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SchemaName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname"""
    p_Tags: typing.List[typing.Union['PropSchemaTagsEntry', dict]] = attr.ib(
        default=None,
        converter=PropSchemaTagsEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSchemaTagsEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags"""

    
    @property
    def rv_SchemaVersion(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#aws-resource-eventschemas-schema-return-values"""
        return GetAtt(resource=self, attr_name="SchemaVersion")
    
    @property
    def rv_SchemaArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#aws-resource-eventschemas-schema-return-values"""
        return GetAtt(resource=self, attr_name="SchemaArn")
    
    @property
    def rv_SchemaName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#aws-resource-eventschemas-schema-return-values"""
        return GetAtt(resource=self, attr_name="SchemaName")
    

@attr.s
class Discoverer(Resource):
    """
    AWS Object Type = "AWS::EventSchemas::Discoverer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html

    Property Document:
    
    - ``rp_SourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
    - ``p_CrossAccount``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Discoverer"

    
    rp_SourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn"""
    p_CrossAccount: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CrossAccount"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description"""
    p_Tags: typing.List[typing.Union['PropDiscovererTagsEntry', dict]] = attr.ib(
        default=None,
        converter=PropDiscovererTagsEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDiscovererTagsEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags"""

    
    @property
    def rv_DiscovererArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#aws-resource-eventschemas-discoverer-return-values"""
        return GetAtt(resource=self, attr_name="DiscovererArn")
    
    @property
    def rv_DiscovererId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#aws-resource-eventschemas-discoverer-return-values"""
        return GetAtt(resource=self, attr_name="DiscovererId")
    
    @property
    def rv_CrossAccount(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#aws-resource-eventschemas-discoverer-return-values"""
        return GetAtt(resource=self, attr_name="CrossAccount")
    

@attr.s
class RegistryPolicy(Resource):
    """
    AWS Object Type = "AWS::EventSchemas::RegistryPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html

    Property Document:
    
    - ``rp_Policy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy
    - ``rp_RegistryName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname
    - ``p_RevisionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::RegistryPolicy"

    
    rp_Policy: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "Policy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy"""
    rp_RegistryName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname"""
    p_RevisionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RevisionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#aws-resource-eventschemas-registrypolicy-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class Registry(Resource):
    """
    AWS Object Type = "AWS::EventSchemas::Registry"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html

    Property Document:
    
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
    - ``p_RegistryName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
    """
    AWS_OBJECT_TYPE = "AWS::EventSchemas::Registry"

    
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description"""
    p_RegistryName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RegistryName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname"""
    p_Tags: typing.List[typing.Union['PropRegistryTagsEntry', dict]] = attr.ib(
        default=None,
        converter=PropRegistryTagsEntry.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRegistryTagsEntry), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags"""

    
    @property
    def rv_RegistryName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#aws-resource-eventschemas-registry-return-values"""
        return GetAtt(resource=self, attr_name="RegistryName")
    
    @property
    def rv_RegistryArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#aws-resource-eventschemas-registry-return-values"""
        return GetAtt(resource=self, attr_name="RegistryArn")
    
