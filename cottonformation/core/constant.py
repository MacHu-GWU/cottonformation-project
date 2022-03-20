# -*- coding: utf-8 -*-

import enum


class AttrMeta:
    """
    Attribute metadata field keys. For better attrs integration.
    """
    PROPERTY_NAME = "p_name"


class IntrinsicFunction:
    """
    Intrinsic Function constant value.
    """
    REF = "Ref"
    BASE64 = "Fn::Base64"
    CIDR = "Fn::Cidr"
    FIND_IN_MAP = "Fn::FindInMap"
    GET_ATT = "Fn::GetAtt"
    GET_AZS = "Fn::GetAZs"
    IMPORT_VALUE = "Fn::ImportValue"
    JOIN = "Fn::Join"
    SELECT = "Fn::Select"
    SPLIT = "Fn::Split"
    SUB = "Fn::Sub"
    TRANSFORM = "Fn::Transform"


class ResourceAttribute:
    """
    Resource Attribute constant value
    """
    CREATION_POLICY = "CreationPolicy"
    DELETION_POLICY = "DeletionPolicy"
    DEPENDS_ON = "DependsOn"
    METADATA = "Metadata"
    UPDATE_POLICY = "UpdatePolicy"
    UPDATE_REPLACE_POLICY = "UpdateReplacePolicy"
    CONDITION = "Condition"


class DeletionPolicy:
    """
    Ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html
    """
    Delete = "Delete"
    Retain = "Retain"
    Snapshot = "Snapshot"


class UpdateReplacePolicy:
    """
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html
    """
    Delete = "Delete"
    Retain = "Retain"
    Snapshot = "Snapshot"


class CloudFomation:
    """
    Used in cloudformation template as Keys
    """
    Version = "AWSTemplateFormatVersion"
    Description = "AWSTemplateFormatVersion"
    Metadata = "Metadata"

    Parameters = "Parameters"
    Resources = "Resources"
    Outputs = "Outputs"

    Rules = "Rules"
    Mappings = "Mappings"
    Conditions = "Conditions"
    Transform = "Transform"

    Type = "Type"
    Properties = "Properties"


class PseudoParameter:
    """
    Reference:

    - Pseudo Parameter: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html
    """
    AWS_ACCOUNT_ID = "AWS::AccountId"
    AWS_NOTIFICATION_ARNS = "AWS::NotificationARNs"
    AWS_NO_VALUE = "AWS::NoValue"
    AWS_PARTITION = "AWS::Partition"
    AWS_REGION = "AWS::Region"
    AWS_STACK_ID = "AWS::StackId"
    AWS_STACK_NAME = "AWS::StackName"
    AWS_URL_SURFIX = "AWS::URLSuffix"


def _collect_enum(klass):
    return [v for k, v in klass.__dict__.items() if not k.startswith("_")]


class Collections:
    INTRINSIC_FUNCTION_LIST = _collect_enum(IntrinsicFunction)
    INTRINSIC_FUNCTION_SET = set(INTRINSIC_FUNCTION_LIST)

    RESOURCE_ATTRIBUTE_LIST = _collect_enum(ResourceAttribute)
    RESOURCE_ATTRIBUTE_SET = set(RESOURCE_ATTRIBUTE_LIST)

    PARAMETER_TYPE_ENUM_SET = set()


class MetaData:
    CTF = "cottonformation"
    Version = "version"
    DependsOn = "depends_on"
    Parameters = "parameters"
    Resources = "resources"
    Mappings = "mappings"
    Conditions = "conditions"
