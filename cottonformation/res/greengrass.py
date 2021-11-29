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
class PropCoreDefinitionCore(Property):
    """
    AWS Object Type = "AWS::Greengrass::CoreDefinition.Core"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-certificatearn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-id
    - ``rp_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-thingarn
    - ``p_SyncShadow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-syncshadow
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::CoreDefinition.Core"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-certificatearn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-id"""
    rp_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-thingarn"""
    p_SyncShadow: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SyncShadow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-core.html#cfn-greengrass-coredefinition-core-syncshadow"""

@attr.s
class PropLoggerDefinitionVersionLogger(Property):
    """
    AWS Object Type = "AWS::Greengrass::LoggerDefinitionVersion.Logger"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html

    Property Document:
    
    - ``rp_Component``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-component
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-id
    - ``rp_Level``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-level
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-type
    - ``p_Space``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-space
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::LoggerDefinitionVersion.Logger"
    
    rp_Component: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Component"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-component"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-id"""
    rp_Level: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Level"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-level"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-type"""
    p_Space: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Space"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinitionversion-logger.html#cfn-greengrass-loggerdefinitionversion-logger-space"""

@attr.s
class PropResourceDefinitionSecretsManagerSecretResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.SecretsManagerSecretResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html

    Property Document:
    
    - ``rp_ARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-arn
    - ``p_AdditionalStagingLabelsToDownload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-additionalstaginglabelstodownload
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.SecretsManagerSecretResourceData"
    
    rp_ARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-arn"""
    p_AdditionalStagingLabelsToDownload: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdditionalStagingLabelsToDownload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinition-secretsmanagersecretresourcedata-additionalstaginglabelstodownload"""

@attr.s
class PropResourceDefinitionResourceDownloadOwnerSetting(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.ResourceDownloadOwnerSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html

    Property Document:
    
    - ``rp_GroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner
    - ``rp_GroupPermission``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.ResourceDownloadOwnerSetting"
    
    rp_GroupOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-groupowner"""
    rp_GroupPermission: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupPermission"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinition-resourcedownloadownersetting-grouppermission"""

@attr.s
class PropLoggerDefinitionLogger(Property):
    """
    AWS Object Type = "AWS::Greengrass::LoggerDefinition.Logger"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html

    Property Document:
    
    - ``rp_Component``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-component
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-id
    - ``rp_Level``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-level
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-type
    - ``p_Space``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-space
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::LoggerDefinition.Logger"
    
    rp_Component: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Component"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-component"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-id"""
    rp_Level: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Level"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-level"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-type"""
    p_Space: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Space"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-logger.html#cfn-greengrass-loggerdefinition-logger-space"""

@attr.s
class PropConnectorDefinitionConnector(Property):
    """
    AWS Object Type = "AWS::Greengrass::ConnectorDefinition.Connector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html

    Property Document:
    
    - ``rp_ConnectorArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-connectorarn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-id
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-parameters
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ConnectorDefinition.Connector"
    
    rp_ConnectorArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-connectorarn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-id"""
    p_Parameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connector.html#cfn-greengrass-connectordefinition-connector-parameters"""

@attr.s
class PropResourceDefinitionVersionSecretsManagerSecretResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.SecretsManagerSecretResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html

    Property Document:
    
    - ``rp_ARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn
    - ``p_AdditionalStagingLabelsToDownload``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.SecretsManagerSecretResourceData"
    
    rp_ARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn"""
    p_AdditionalStagingLabelsToDownload: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdditionalStagingLabelsToDownload"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload"""

@attr.s
class PropSubscriptionDefinitionVersionSubscription(Property):
    """
    AWS Object Type = "AWS::Greengrass::SubscriptionDefinitionVersion.Subscription"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-id
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-source
    - ``rp_Subject``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-subject
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-target
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::SubscriptionDefinitionVersion.Subscription"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-id"""
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-source"""
    rp_Subject: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subject"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-subject"""
    rp_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinitionversion-subscription.html#cfn-greengrass-subscriptiondefinitionversion-subscription-target"""

@attr.s
class PropResourceDefinitionSageMakerMachineLearningModelResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.SageMakerMachineLearningModelResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-destinationpath
    - ``rp_SageMakerJobArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-sagemakerjobarn
    - ``p_OwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-ownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.SageMakerMachineLearningModelResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-destinationpath"""
    rp_SageMakerJobArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SageMakerJobArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-sagemakerjobarn"""
    p_OwnerSetting: typing.Union['PropResourceDefinitionResourceDownloadOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionResourceDownloadOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionResourceDownloadOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-sagemakermachinelearningmodelresourcedata-ownersetting"""

@attr.s
class PropCoreDefinitionVersionCore(Property):
    """
    AWS Object Type = "AWS::Greengrass::CoreDefinitionVersion.Core"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-certificatearn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-id
    - ``rp_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-thingarn
    - ``p_SyncShadow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-syncshadow
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::CoreDefinitionVersion.Core"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-certificatearn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-id"""
    rp_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-thingarn"""
    p_SyncShadow: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SyncShadow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinitionversion-core.html#cfn-greengrass-coredefinitionversion-core-syncshadow"""

@attr.s
class PropFunctionDefinitionVersionRunAs(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.RunAs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html

    Property Document:
    
    - ``p_Gid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-gid
    - ``p_Uid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-uid
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.RunAs"
    
    p_Gid: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Gid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-gid"""
    p_Uid: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Uid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-runas.html#cfn-greengrass-functiondefinitionversion-runas-uid"""

@attr.s
class PropResourceDefinitionVersionResourceDownloadOwnerSetting(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.ResourceDownloadOwnerSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html

    Property Document:
    
    - ``rp_GroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-groupowner
    - ``rp_GroupPermission``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-grouppermission
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.ResourceDownloadOwnerSetting"
    
    rp_GroupOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-groupowner"""
    rp_GroupPermission: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupPermission"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedownloadownersetting.html#cfn-greengrass-resourcedefinitionversion-resourcedownloadownersetting-grouppermission"""

@attr.s
class PropFunctionDefinitionRunAs(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.RunAs"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html

    Property Document:
    
    - ``p_Gid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-gid
    - ``p_Uid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-uid
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.RunAs"
    
    p_Gid: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Gid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-gid"""
    p_Uid: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Uid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-runas.html#cfn-greengrass-functiondefinition-runas-uid"""

@attr.s
class PropDeviceDefinitionVersionDevice(Property):
    """
    AWS Object Type = "AWS::Greengrass::DeviceDefinitionVersion.Device"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-certificatearn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-id
    - ``rp_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-thingarn
    - ``p_SyncShadow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-syncshadow
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::DeviceDefinitionVersion.Device"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-certificatearn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-id"""
    rp_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-thingarn"""
    p_SyncShadow: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SyncShadow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinitionversion-device.html#cfn-greengrass-devicedefinitionversion-device-syncshadow"""

@attr.s
class PropResourceDefinitionGroupOwnerSetting(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.GroupOwnerSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html

    Property Document:
    
    - ``rp_AutoAddGroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner
    - ``p_GroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-groupowner
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.GroupOwnerSetting"
    
    rp_AutoAddGroupOwner: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AutoAddGroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-autoaddgroupowner"""
    p_GroupOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-groupownersetting.html#cfn-greengrass-resourcedefinition-groupownersetting-groupowner"""

@attr.s
class PropGroupGroupVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::Group.GroupVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html

    Property Document:
    
    - ``p_ConnectorDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-connectordefinitionversionarn
    - ``p_CoreDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-coredefinitionversionarn
    - ``p_DeviceDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-devicedefinitionversionarn
    - ``p_FunctionDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-functiondefinitionversionarn
    - ``p_LoggerDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-loggerdefinitionversionarn
    - ``p_ResourceDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-resourcedefinitionversionarn
    - ``p_SubscriptionDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-subscriptiondefinitionversionarn
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::Group.GroupVersion"
    
    p_ConnectorDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-connectordefinitionversionarn"""
    p_CoreDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CoreDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-coredefinitionversionarn"""
    p_DeviceDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-devicedefinitionversionarn"""
    p_FunctionDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-functiondefinitionversionarn"""
    p_LoggerDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggerDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-loggerdefinitionversionarn"""
    p_ResourceDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-resourcedefinitionversionarn"""
    p_SubscriptionDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SubscriptionDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-group-groupversion.html#cfn-greengrass-group-groupversion-subscriptiondefinitionversionarn"""

@attr.s
class PropResourceDefinitionLocalDeviceResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.LocalDeviceResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html

    Property Document:
    
    - ``rp_SourcePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-sourcepath
    - ``p_GroupOwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-groupownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.LocalDeviceResourceData"
    
    rp_SourcePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-sourcepath"""
    p_GroupOwnerSetting: typing.Union['PropResourceDefinitionGroupOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionGroupOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionGroupOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localdeviceresourcedata.html#cfn-greengrass-resourcedefinition-localdeviceresourcedata-groupownersetting"""

@attr.s
class PropDeviceDefinitionDevice(Property):
    """
    AWS Object Type = "AWS::Greengrass::DeviceDefinition.Device"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html

    Property Document:
    
    - ``rp_CertificateArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-certificatearn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-id
    - ``rp_ThingArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-thingarn
    - ``p_SyncShadow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-syncshadow
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::DeviceDefinition.Device"
    
    rp_CertificateArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CertificateArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-certificatearn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-id"""
    rp_ThingArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ThingArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-thingarn"""
    p_SyncShadow: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SyncShadow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-device.html#cfn-greengrass-devicedefinition-device-syncshadow"""

@attr.s
class PropDeviceDefinitionDeviceDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::DeviceDefinition.DeviceDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html

    Property Document:
    
    - ``rp_Devices``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html#cfn-greengrass-devicedefinition-devicedefinitionversion-devices
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::DeviceDefinition.DeviceDefinitionVersion"
    
    rp_Devices: typing.List[typing.Union['PropDeviceDefinitionDevice', dict]] = attr.ib(
        default=None,
        converter=PropDeviceDefinitionDevice.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeviceDefinitionDevice), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Devices"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-devicedefinition-devicedefinitionversion.html#cfn-greengrass-devicedefinition-devicedefinitionversion-devices"""

@attr.s
class PropSubscriptionDefinitionSubscription(Property):
    """
    AWS Object Type = "AWS::Greengrass::SubscriptionDefinition.Subscription"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-id
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-source
    - ``rp_Subject``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-subject
    - ``rp_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-target
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::SubscriptionDefinition.Subscription"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-id"""
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-source"""
    rp_Subject: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subject"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-subject"""
    rp_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscription.html#cfn-greengrass-subscriptiondefinition-subscription-target"""

@attr.s
class PropCoreDefinitionCoreDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::CoreDefinition.CoreDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html

    Property Document:
    
    - ``rp_Cores``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html#cfn-greengrass-coredefinition-coredefinitionversion-cores
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::CoreDefinition.CoreDefinitionVersion"
    
    rp_Cores: typing.List[typing.Union['PropCoreDefinitionCore', dict]] = attr.ib(
        default=None,
        converter=PropCoreDefinitionCore.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCoreDefinitionCore), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Cores"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-coredefinition-coredefinitionversion.html#cfn-greengrass-coredefinition-coredefinitionversion-cores"""

@attr.s
class PropResourceDefinitionVersionS3MachineLearningModelResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.S3MachineLearningModelResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-destinationpath
    - ``rp_S3Uri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-s3uri
    - ``p_OwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-ownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.S3MachineLearningModelResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-destinationpath"""
    rp_S3Uri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Uri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-s3uri"""
    p_OwnerSetting: typing.Union['PropResourceDefinitionVersionResourceDownloadOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionResourceDownloadOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionResourceDownloadOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-s3machinelearningmodelresourcedata-ownersetting"""

@attr.s
class PropResourceDefinitionLocalVolumeResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.LocalVolumeResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-destinationpath
    - ``rp_SourcePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-sourcepath
    - ``p_GroupOwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-groupownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.LocalVolumeResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-destinationpath"""
    rp_SourcePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-sourcepath"""
    p_GroupOwnerSetting: typing.Union['PropResourceDefinitionGroupOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionGroupOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionGroupOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-localvolumeresourcedata.html#cfn-greengrass-resourcedefinition-localvolumeresourcedata-groupownersetting"""

@attr.s
class PropFunctionDefinitionResourceAccessPolicy(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.ResourceAccessPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html

    Property Document:
    
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid
    - ``p_Permission``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.ResourceAccessPolicy"
    
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-resourceid"""
    p_Permission: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Permission"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-resourceaccesspolicy.html#cfn-greengrass-functiondefinition-resourceaccesspolicy-permission"""

@attr.s
class PropResourceDefinitionVersionGroupOwnerSetting(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.GroupOwnerSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html

    Property Document:
    
    - ``rp_AutoAddGroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner
    - ``p_GroupOwner``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.GroupOwnerSetting"
    
    rp_AutoAddGroupOwner: bool = attr.ib(
        default=None,
        validator=attr.validators.instance_of(bool),
        metadata={AttrMeta.PROPERTY_NAME: "AutoAddGroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-autoaddgroupowner"""
    p_GroupOwner: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwner"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-groupownersetting.html#cfn-greengrass-resourcedefinitionversion-groupownersetting-groupowner"""

@attr.s
class PropFunctionDefinitionVersionResourceAccessPolicy(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.ResourceAccessPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html

    Property Document:
    
    - ``rp_ResourceId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-resourceid
    - ``p_Permission``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-permission
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.ResourceAccessPolicy"
    
    rp_ResourceId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-resourceid"""
    p_Permission: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Permission"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-resourceaccesspolicy.html#cfn-greengrass-functiondefinitionversion-resourceaccesspolicy-permission"""

@attr.s
class PropLoggerDefinitionLoggerDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::LoggerDefinition.LoggerDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html

    Property Document:
    
    - ``rp_Loggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::LoggerDefinition.LoggerDefinitionVersion"
    
    rp_Loggers: typing.List[typing.Union['PropLoggerDefinitionLogger', dict]] = attr.ib(
        default=None,
        converter=PropLoggerDefinitionLogger.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLoggerDefinitionLogger), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Loggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-loggerdefinition-loggerdefinitionversion.html#cfn-greengrass-loggerdefinition-loggerdefinitionversion-loggers"""

@attr.s
class PropConnectorDefinitionVersionConnector(Property):
    """
    AWS Object Type = "AWS::Greengrass::ConnectorDefinitionVersion.Connector"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html

    Property Document:
    
    - ``rp_ConnectorArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-connectorarn
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-id
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-parameters
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ConnectorDefinitionVersion.Connector"
    
    rp_ConnectorArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-connectorarn"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-id"""
    p_Parameters: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinitionversion-connector.html#cfn-greengrass-connectordefinitionversion-connector-parameters"""

@attr.s
class PropFunctionDefinitionVersionExecution(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.Execution"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html

    Property Document:
    
    - ``p_IsolationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-isolationmode
    - ``p_RunAs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-runas
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.Execution"
    
    p_IsolationMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IsolationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-isolationmode"""
    p_RunAs: typing.Union['PropFunctionDefinitionVersionRunAs', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionRunAs.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionVersionRunAs)),
        metadata={AttrMeta.PROPERTY_NAME: "RunAs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-execution.html#cfn-greengrass-functiondefinitionversion-execution-runas"""

@attr.s
class PropResourceDefinitionS3MachineLearningModelResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.S3MachineLearningModelResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath
    - ``rp_S3Uri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri
    - ``p_OwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.S3MachineLearningModelResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-destinationpath"""
    rp_S3Uri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3Uri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-s3uri"""
    p_OwnerSetting: typing.Union['PropResourceDefinitionResourceDownloadOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionResourceDownloadOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionResourceDownloadOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-s3machinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinition-s3machinelearningmodelresourcedata-ownersetting"""

@attr.s
class PropSubscriptionDefinitionSubscriptionDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::SubscriptionDefinition.SubscriptionDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html

    Property Document:
    
    - ``rp_Subscriptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::SubscriptionDefinition.SubscriptionDefinitionVersion"
    
    rp_Subscriptions: typing.List[typing.Union['PropSubscriptionDefinitionSubscription', dict]] = attr.ib(
        default=None,
        converter=PropSubscriptionDefinitionSubscription.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSubscriptionDefinitionSubscription), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subscriptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-subscriptiondefinition-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinition-subscriptiondefinitionversion-subscriptions"""

@attr.s
class PropResourceDefinitionVersionLocalDeviceResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.LocalDeviceResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html

    Property Document:
    
    - ``rp_SourcePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath
    - ``p_GroupOwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.LocalDeviceResourceData"
    
    rp_SourcePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-sourcepath"""
    p_GroupOwnerSetting: typing.Union['PropResourceDefinitionVersionGroupOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionGroupOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionGroupOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localdeviceresourcedata.html#cfn-greengrass-resourcedefinitionversion-localdeviceresourcedata-groupownersetting"""

@attr.s
class PropFunctionDefinitionVersionDefaultConfig(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.DefaultConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html

    Property Document:
    
    - ``rp_Execution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html#cfn-greengrass-functiondefinitionversion-defaultconfig-execution
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.DefaultConfig"
    
    rp_Execution: typing.Union['PropFunctionDefinitionVersionExecution', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionExecution.from_dict,
        validator=attr.validators.instance_of(PropFunctionDefinitionVersionExecution),
        metadata={AttrMeta.PROPERTY_NAME: "Execution"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-defaultconfig.html#cfn-greengrass-functiondefinitionversion-defaultconfig-execution"""

@attr.s
class PropConnectorDefinitionConnectorDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::ConnectorDefinition.ConnectorDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html

    Property Document:
    
    - ``rp_Connectors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ConnectorDefinition.ConnectorDefinitionVersion"
    
    rp_Connectors: typing.List[typing.Union['PropConnectorDefinitionConnector', dict]] = attr.ib(
        default=None,
        converter=PropConnectorDefinitionConnector.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConnectorDefinitionConnector), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Connectors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-connectordefinition-connectordefinitionversion.html#cfn-greengrass-connectordefinition-connectordefinitionversion-connectors"""

@attr.s
class PropResourceDefinitionVersionLocalVolumeResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.LocalVolumeResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-destinationpath
    - ``rp_SourcePath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-sourcepath
    - ``p_GroupOwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-groupownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.LocalVolumeResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-destinationpath"""
    rp_SourcePath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-sourcepath"""
    p_GroupOwnerSetting: typing.Union['PropResourceDefinitionVersionGroupOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionGroupOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionGroupOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "GroupOwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-localvolumeresourcedata.html#cfn-greengrass-resourcedefinitionversion-localvolumeresourcedata-groupownersetting"""

@attr.s
class PropFunctionDefinitionExecution(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.Execution"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html

    Property Document:
    
    - ``p_IsolationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-isolationmode
    - ``p_RunAs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-runas
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.Execution"
    
    p_IsolationMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IsolationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-isolationmode"""
    p_RunAs: typing.Union['PropFunctionDefinitionRunAs', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionRunAs.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionRunAs)),
        metadata={AttrMeta.PROPERTY_NAME: "RunAs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-execution.html#cfn-greengrass-functiondefinition-execution-runas"""

@attr.s
class PropResourceDefinitionVersionSageMakerMachineLearningModelResourceData(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.SageMakerMachineLearningModelResourceData"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html

    Property Document:
    
    - ``rp_DestinationPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-destinationpath
    - ``rp_SageMakerJobArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-sagemakerjobarn
    - ``p_OwnerSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-ownersetting
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.SageMakerMachineLearningModelResourceData"
    
    rp_DestinationPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-destinationpath"""
    rp_SageMakerJobArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SageMakerJobArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-sagemakerjobarn"""
    p_OwnerSetting: typing.Union['PropResourceDefinitionVersionResourceDownloadOwnerSetting', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionResourceDownloadOwnerSetting.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionResourceDownloadOwnerSetting)),
        metadata={AttrMeta.PROPERTY_NAME: "OwnerSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata.html#cfn-greengrass-resourcedefinitionversion-sagemakermachinelearningmodelresourcedata-ownersetting"""

@attr.s
class PropFunctionDefinitionEnvironment(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html

    Property Document:
    
    - ``p_AccessSysfs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-accesssysfs
    - ``p_Execution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-execution
    - ``p_ResourceAccessPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-resourceaccesspolicies
    - ``p_Variables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-variables
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.Environment"
    
    p_AccessSysfs: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessSysfs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-accesssysfs"""
    p_Execution: typing.Union['PropFunctionDefinitionExecution', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionExecution.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionExecution)),
        metadata={AttrMeta.PROPERTY_NAME: "Execution"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-execution"""
    p_ResourceAccessPolicies: typing.List[typing.Union['PropFunctionDefinitionResourceAccessPolicy', dict]] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionResourceAccessPolicy.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFunctionDefinitionResourceAccessPolicy), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceAccessPolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-resourceaccesspolicies"""
    p_Variables: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Variables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-environment.html#cfn-greengrass-functiondefinition-environment-variables"""

@attr.s
class PropFunctionDefinitionVersionEnvironment(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.Environment"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html

    Property Document:
    
    - ``p_AccessSysfs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-accesssysfs
    - ``p_Execution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-execution
    - ``p_ResourceAccessPolicies``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-resourceaccesspolicies
    - ``p_Variables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-variables
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.Environment"
    
    p_AccessSysfs: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessSysfs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-accesssysfs"""
    p_Execution: typing.Union['PropFunctionDefinitionVersionExecution', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionExecution.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionVersionExecution)),
        metadata={AttrMeta.PROPERTY_NAME: "Execution"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-execution"""
    p_ResourceAccessPolicies: typing.List[typing.Union['PropFunctionDefinitionVersionResourceAccessPolicy', dict]] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionResourceAccessPolicy.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFunctionDefinitionVersionResourceAccessPolicy), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceAccessPolicies"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-resourceaccesspolicies"""
    p_Variables: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Variables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-environment.html#cfn-greengrass-functiondefinitionversion-environment-variables"""

@attr.s
class PropResourceDefinitionVersionResourceDataContainer(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.ResourceDataContainer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html

    Property Document:
    
    - ``p_LocalDeviceResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata
    - ``p_LocalVolumeResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata
    - ``p_S3MachineLearningModelResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata
    - ``p_SageMakerMachineLearningModelResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata
    - ``p_SecretsManagerSecretResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.ResourceDataContainer"
    
    p_LocalDeviceResourceData: typing.Union['PropResourceDefinitionVersionLocalDeviceResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionLocalDeviceResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionLocalDeviceResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "LocalDeviceResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localdeviceresourcedata"""
    p_LocalVolumeResourceData: typing.Union['PropResourceDefinitionVersionLocalVolumeResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionLocalVolumeResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionLocalVolumeResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "LocalVolumeResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-localvolumeresourcedata"""
    p_S3MachineLearningModelResourceData: typing.Union['PropResourceDefinitionVersionS3MachineLearningModelResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionS3MachineLearningModelResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionS3MachineLearningModelResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "S3MachineLearningModelResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-s3machinelearningmodelresourcedata"""
    p_SageMakerMachineLearningModelResourceData: typing.Union['PropResourceDefinitionVersionSageMakerMachineLearningModelResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionSageMakerMachineLearningModelResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionSageMakerMachineLearningModelResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "SageMakerMachineLearningModelResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-sagemakermachinelearningmodelresourcedata"""
    p_SecretsManagerSecretResourceData: typing.Union['PropResourceDefinitionVersionSecretsManagerSecretResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionSecretsManagerSecretResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionVersionSecretsManagerSecretResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "SecretsManagerSecretResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html#cfn-greengrass-resourcedefinitionversion-resourcedatacontainer-secretsmanagersecretresourcedata"""

@attr.s
class PropResourceDefinitionResourceDataContainer(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.ResourceDataContainer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html

    Property Document:
    
    - ``p_LocalDeviceResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localdeviceresourcedata
    - ``p_LocalVolumeResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localvolumeresourcedata
    - ``p_S3MachineLearningModelResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-s3machinelearningmodelresourcedata
    - ``p_SageMakerMachineLearningModelResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-sagemakermachinelearningmodelresourcedata
    - ``p_SecretsManagerSecretResourceData``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-secretsmanagersecretresourcedata
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.ResourceDataContainer"
    
    p_LocalDeviceResourceData: typing.Union['PropResourceDefinitionLocalDeviceResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionLocalDeviceResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionLocalDeviceResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "LocalDeviceResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localdeviceresourcedata"""
    p_LocalVolumeResourceData: typing.Union['PropResourceDefinitionLocalVolumeResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionLocalVolumeResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionLocalVolumeResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "LocalVolumeResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-localvolumeresourcedata"""
    p_S3MachineLearningModelResourceData: typing.Union['PropResourceDefinitionS3MachineLearningModelResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionS3MachineLearningModelResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionS3MachineLearningModelResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "S3MachineLearningModelResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-s3machinelearningmodelresourcedata"""
    p_SageMakerMachineLearningModelResourceData: typing.Union['PropResourceDefinitionSageMakerMachineLearningModelResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionSageMakerMachineLearningModelResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionSageMakerMachineLearningModelResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "SageMakerMachineLearningModelResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-sagemakermachinelearningmodelresourcedata"""
    p_SecretsManagerSecretResourceData: typing.Union['PropResourceDefinitionSecretsManagerSecretResourceData', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionSecretsManagerSecretResourceData.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionSecretsManagerSecretResourceData)),
        metadata={AttrMeta.PROPERTY_NAME: "SecretsManagerSecretResourceData"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedatacontainer.html#cfn-greengrass-resourcedefinition-resourcedatacontainer-secretsmanagersecretresourcedata"""

@attr.s
class PropFunctionDefinitionVersionFunctionConfiguration(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.FunctionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html

    Property Document:
    
    - ``p_EncodingType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-encodingtype
    - ``p_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-environment
    - ``p_ExecArgs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-execargs
    - ``p_Executable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-executable
    - ``p_MemorySize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-memorysize
    - ``p_Pinned``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-pinned
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-timeout
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.FunctionConfiguration"
    
    p_EncodingType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncodingType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-encodingtype"""
    p_Environment: typing.Union['PropFunctionDefinitionVersionEnvironment', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionEnvironment.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionVersionEnvironment)),
        metadata={AttrMeta.PROPERTY_NAME: "Environment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-environment"""
    p_ExecArgs: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecArgs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-execargs"""
    p_Executable: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Executable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-executable"""
    p_MemorySize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MemorySize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-memorysize"""
    p_Pinned: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Pinned"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-pinned"""
    p_Timeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-functionconfiguration.html#cfn-greengrass-functiondefinitionversion-functionconfiguration-timeout"""

@attr.s
class PropResourceDefinitionVersionResourceInstance(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion.ResourceInstance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-id
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-name
    - ``rp_ResourceDataContainer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion.ResourceInstance"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-id"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-name"""
    rp_ResourceDataContainer: typing.Union['PropResourceDefinitionVersionResourceDataContainer', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionResourceDataContainer.from_dict,
        validator=attr.validators.instance_of(PropResourceDefinitionVersionResourceDataContainer),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceDataContainer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourceinstance.html#cfn-greengrass-resourcedefinitionversion-resourceinstance-resourcedatacontainer"""

@attr.s
class PropFunctionDefinitionFunctionConfiguration(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.FunctionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html

    Property Document:
    
    - ``p_EncodingType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-encodingtype
    - ``p_Environment``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-environment
    - ``p_ExecArgs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-execargs
    - ``p_Executable``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-executable
    - ``p_MemorySize``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-memorysize
    - ``p_Pinned``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-pinned
    - ``p_Timeout``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-timeout
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.FunctionConfiguration"
    
    p_EncodingType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncodingType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-encodingtype"""
    p_Environment: typing.Union['PropFunctionDefinitionEnvironment', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionEnvironment.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionEnvironment)),
        metadata={AttrMeta.PROPERTY_NAME: "Environment"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-environment"""
    p_ExecArgs: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ExecArgs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-execargs"""
    p_Executable: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Executable"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-executable"""
    p_MemorySize: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "MemorySize"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-memorysize"""
    p_Pinned: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Pinned"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-pinned"""
    p_Timeout: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Timeout"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functionconfiguration.html#cfn-greengrass-functiondefinition-functionconfiguration-timeout"""

@attr.s
class PropFunctionDefinitionVersionFunction(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion.Function"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html

    Property Document:
    
    - ``rp_FunctionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionarn
    - ``rp_FunctionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionconfiguration
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-id
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion.Function"
    
    rp_FunctionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionarn"""
    rp_FunctionConfiguration: typing.Union['PropFunctionDefinitionVersionFunctionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionFunctionConfiguration.from_dict,
        validator=attr.validators.instance_of(PropFunctionDefinitionVersionFunctionConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-functionconfiguration"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinitionversion-function.html#cfn-greengrass-functiondefinitionversion-function-id"""

@attr.s
class PropFunctionDefinitionDefaultConfig(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.DefaultConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html

    Property Document:
    
    - ``rp_Execution``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html#cfn-greengrass-functiondefinition-defaultconfig-execution
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.DefaultConfig"
    
    rp_Execution: typing.Union['PropFunctionDefinitionExecution', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionExecution.from_dict,
        validator=attr.validators.instance_of(PropFunctionDefinitionExecution),
        metadata={AttrMeta.PROPERTY_NAME: "Execution"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-defaultconfig.html#cfn-greengrass-functiondefinition-defaultconfig-execution"""

@attr.s
class PropResourceDefinitionResourceInstance(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.ResourceInstance"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html

    Property Document:
    
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-id
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-name
    - ``rp_ResourceDataContainer``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-resourcedatacontainer
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.ResourceInstance"
    
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-id"""
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-name"""
    rp_ResourceDataContainer: typing.Union['PropResourceDefinitionResourceDataContainer', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionResourceDataContainer.from_dict,
        validator=attr.validators.instance_of(PropResourceDefinitionResourceDataContainer),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceDataContainer"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourceinstance.html#cfn-greengrass-resourcedefinition-resourceinstance-resourcedatacontainer"""

@attr.s
class PropFunctionDefinitionFunction(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.Function"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html

    Property Document:
    
    - ``rp_FunctionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionarn
    - ``rp_FunctionConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionconfiguration
    - ``rp_Id``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-id
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.Function"
    
    rp_FunctionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionarn"""
    rp_FunctionConfiguration: typing.Union['PropFunctionDefinitionFunctionConfiguration', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionFunctionConfiguration.from_dict,
        validator=attr.validators.instance_of(PropFunctionDefinitionFunctionConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-functionconfiguration"""
    rp_Id: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Id"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-function.html#cfn-greengrass-functiondefinition-function-id"""

@attr.s
class PropFunctionDefinitionFunctionDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition.FunctionDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html

    Property Document:
    
    - ``rp_Functions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-functions
    - ``p_DefaultConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition.FunctionDefinitionVersion"
    
    rp_Functions: typing.List[typing.Union['PropFunctionDefinitionFunction', dict]] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionFunction.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFunctionDefinitionFunction), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Functions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-functions"""
    p_DefaultConfig: typing.Union['PropFunctionDefinitionDefaultConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionDefaultConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionDefaultConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-functiondefinition-functiondefinitionversion.html#cfn-greengrass-functiondefinition-functiondefinitionversion-defaultconfig"""

@attr.s
class PropResourceDefinitionResourceDefinitionVersion(Property):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition.ResourceDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html

    Property Document:
    
    - ``rp_Resources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition.ResourceDefinitionVersion"
    
    rp_Resources: typing.List[typing.Union['PropResourceDefinitionResourceInstance', dict]] = attr.ib(
        default=None,
        converter=PropResourceDefinitionResourceInstance.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResourceDefinitionResourceInstance), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Resources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinition-resourcedefinitionversion.html#cfn-greengrass-resourcedefinition-resourcedefinitionversion-resources"""


#--- Resource declaration ---

@attr.s
class ConnectorDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::ConnectorDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html

    Property Document:
    
    - ``rp_ConnectorDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectordefinitionid
    - ``rp_Connectors``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectors
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ConnectorDefinitionVersion"

    
    rp_ConnectorDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectordefinitionid"""
    rp_Connectors: typing.List[typing.Union['PropConnectorDefinitionVersionConnector', dict]] = attr.ib(
        default=None,
        converter=PropConnectorDefinitionVersionConnector.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConnectorDefinitionVersionConnector), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Connectors"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html#cfn-greengrass-connectordefinitionversion-connectors"""

    

@attr.s
class LoggerDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::LoggerDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html

    Property Document:
    
    - ``rp_LoggerDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggerdefinitionid
    - ``rp_Loggers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggers
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::LoggerDefinitionVersion"

    
    rp_LoggerDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LoggerDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggerdefinitionid"""
    rp_Loggers: typing.List[typing.Union['PropLoggerDefinitionVersionLogger', dict]] = attr.ib(
        default=None,
        converter=PropLoggerDefinitionVersionLogger.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLoggerDefinitionVersionLogger), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Loggers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html#cfn-greengrass-loggerdefinitionversion-loggers"""

    

@attr.s
class FunctionDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html

    Property Document:
    
    - ``rp_FunctionDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functiondefinitionid
    - ``rp_Functions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functions
    - ``p_DefaultConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-defaultconfig
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinitionVersion"

    
    rp_FunctionDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functiondefinitionid"""
    rp_Functions: typing.List[typing.Union['PropFunctionDefinitionVersionFunction', dict]] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionFunction.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFunctionDefinitionVersionFunction), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Functions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-functions"""
    p_DefaultConfig: typing.Union['PropFunctionDefinitionVersionDefaultConfig', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionVersionDefaultConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionVersionDefaultConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html#cfn-greengrass-functiondefinitionversion-defaultconfig"""

    

@attr.s
class ConnectorDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::ConnectorDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ConnectorDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-name"""
    p_InitialVersion: typing.Union['PropConnectorDefinitionConnectorDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropConnectorDefinitionConnectorDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConnectorDefinitionConnectorDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#cfn-greengrass-connectordefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#aws-resource-greengrass-connectordefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#aws-resource-greengrass-connectordefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#aws-resource-greengrass-connectordefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html#aws-resource-greengrass-connectordefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class FunctionDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::FunctionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::FunctionDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-name"""
    p_InitialVersion: typing.Union['PropFunctionDefinitionFunctionDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropFunctionDefinitionFunctionDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFunctionDefinitionFunctionDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#cfn-greengrass-functiondefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#aws-resource-greengrass-functiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#aws-resource-greengrass-functiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#aws-resource-greengrass-functiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html#aws-resource-greengrass-functiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class LoggerDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::LoggerDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::LoggerDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-name"""
    p_InitialVersion: typing.Union['PropLoggerDefinitionLoggerDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropLoggerDefinitionLoggerDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropLoggerDefinitionLoggerDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#cfn-greengrass-loggerdefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#aws-resource-greengrass-loggerdefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#aws-resource-greengrass-loggerdefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#aws-resource-greengrass-loggerdefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html#aws-resource-greengrass-loggerdefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class CoreDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::CoreDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::CoreDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-name"""
    p_InitialVersion: typing.Union['PropCoreDefinitionCoreDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropCoreDefinitionCoreDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropCoreDefinitionCoreDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#cfn-greengrass-coredefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#aws-resource-greengrass-coredefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#aws-resource-greengrass-coredefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#aws-resource-greengrass-coredefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html#aws-resource-greengrass-coredefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class DeviceDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::DeviceDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html

    Property Document:
    
    - ``rp_DeviceDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devicedefinitionid
    - ``rp_Devices``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devices
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::DeviceDefinitionVersion"

    
    rp_DeviceDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devicedefinitionid"""
    rp_Devices: typing.List[typing.Union['PropDeviceDefinitionVersionDevice', dict]] = attr.ib(
        default=None,
        converter=PropDeviceDefinitionVersionDevice.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropDeviceDefinitionVersionDevice), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Devices"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html#cfn-greengrass-devicedefinitionversion-devices"""

    

@attr.s
class ResourceDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-name"""
    p_InitialVersion: typing.Union['PropResourceDefinitionResourceDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropResourceDefinitionResourceDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropResourceDefinitionResourceDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#cfn-greengrass-resourcedefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#aws-resource-greengrass-resourcedefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#aws-resource-greengrass-resourcedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#aws-resource-greengrass-resourcedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html#aws-resource-greengrass-resourcedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class DeviceDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::DeviceDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::DeviceDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-name"""
    p_InitialVersion: typing.Union['PropDeviceDefinitionDeviceDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropDeviceDefinitionDeviceDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropDeviceDefinitionDeviceDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#cfn-greengrass-devicedefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#aws-resource-greengrass-devicedefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#aws-resource-greengrass-devicedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#aws-resource-greengrass-devicedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html#aws-resource-greengrass-devicedefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class Group(Resource):
    """
    AWS Object Type = "AWS::Greengrass::Group"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-initialversion
    - ``p_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-rolearn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::Group"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-name"""
    p_InitialVersion: typing.Union['PropGroupGroupVersion', dict] = attr.ib(
        default=None,
        converter=PropGroupGroupVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropGroupGroupVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-initialversion"""
    p_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-rolearn"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#cfn-greengrass-group-tags"""

    
    @property
    def rv_RoleAttachedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="RoleAttachedAt")
    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_RoleArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="RoleArn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html#aws-resource-greengrass-group-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class SubscriptionDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::SubscriptionDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html

    Property Document:
    
    - ``rp_SubscriptionDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptiondefinitionid
    - ``rp_Subscriptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptions
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::SubscriptionDefinitionVersion"

    
    rp_SubscriptionDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubscriptionDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptiondefinitionid"""
    rp_Subscriptions: typing.List[typing.Union['PropSubscriptionDefinitionVersionSubscription', dict]] = attr.ib(
        default=None,
        converter=PropSubscriptionDefinitionVersionSubscription.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropSubscriptionDefinitionVersionSubscription), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Subscriptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html#cfn-greengrass-subscriptiondefinitionversion-subscriptions"""

    

@attr.s
class CoreDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::CoreDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html

    Property Document:
    
    - ``rp_CoreDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-coredefinitionid
    - ``rp_Cores``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-cores
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::CoreDefinitionVersion"

    
    rp_CoreDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CoreDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-coredefinitionid"""
    rp_Cores: typing.List[typing.Union['PropCoreDefinitionVersionCore', dict]] = attr.ib(
        default=None,
        converter=PropCoreDefinitionVersionCore.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropCoreDefinitionVersionCore), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Cores"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html#cfn-greengrass-coredefinitionversion-cores"""

    

@attr.s
class SubscriptionDefinition(Resource):
    """
    AWS Object Type = "AWS::Greengrass::SubscriptionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html

    Property Document:
    
    - ``rp_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-name
    - ``p_InitialVersion``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-initialversion
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-tags
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::SubscriptionDefinition"

    
    rp_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-name"""
    p_InitialVersion: typing.Union['PropSubscriptionDefinitionSubscriptionDefinitionVersion', dict] = attr.ib(
        default=None,
        converter=PropSubscriptionDefinitionSubscriptionDefinitionVersion.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropSubscriptionDefinitionSubscriptionDefinitionVersion)),
        metadata={AttrMeta.PROPERTY_NAME: "InitialVersion"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-initialversion"""
    p_Tags: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#cfn-greengrass-subscriptiondefinition-tags"""

    
    @property
    def rv_LatestVersionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#aws-resource-greengrass-subscriptiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="LatestVersionArn")
    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#aws-resource-greengrass-subscriptiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_Arn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#aws-resource-greengrass-subscriptiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Arn")
    
    @property
    def rv_Name(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html#aws-resource-greengrass-subscriptiondefinition-return-values"""
        return GetAtt(resource=self, attr_name="Name")
    

@attr.s
class ResourceDefinitionVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::ResourceDefinitionVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html

    Property Document:
    
    - ``rp_ResourceDefinitionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resourcedefinitionid
    - ``rp_Resources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resources
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::ResourceDefinitionVersion"

    
    rp_ResourceDefinitionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceDefinitionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resourcedefinitionid"""
    rp_Resources: typing.List[typing.Union['PropResourceDefinitionVersionResourceInstance', dict]] = attr.ib(
        default=None,
        converter=PropResourceDefinitionVersionResourceInstance.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropResourceDefinitionVersionResourceInstance), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Resources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html#cfn-greengrass-resourcedefinitionversion-resources"""

    

@attr.s
class GroupVersion(Resource):
    """
    AWS Object Type = "AWS::Greengrass::GroupVersion"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html

    Property Document:
    
    - ``rp_GroupId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-groupid
    - ``p_ConnectorDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-connectordefinitionversionarn
    - ``p_CoreDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-coredefinitionversionarn
    - ``p_DeviceDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-devicedefinitionversionarn
    - ``p_FunctionDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-functiondefinitionversionarn
    - ``p_LoggerDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-loggerdefinitionversionarn
    - ``p_ResourceDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-resourcedefinitionversionarn
    - ``p_SubscriptionDefinitionVersionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-subscriptiondefinitionversionarn
    """
    AWS_OBJECT_TYPE = "AWS::Greengrass::GroupVersion"

    
    rp_GroupId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GroupId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-groupid"""
    p_ConnectorDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-connectordefinitionversionarn"""
    p_CoreDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CoreDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-coredefinitionversionarn"""
    p_DeviceDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeviceDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-devicedefinitionversionarn"""
    p_FunctionDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-functiondefinitionversionarn"""
    p_LoggerDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LoggerDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-loggerdefinitionversionarn"""
    p_ResourceDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-resourcedefinitionversionarn"""
    p_SubscriptionDefinitionVersionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SubscriptionDefinitionVersionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html#cfn-greengrass-groupversion-subscriptiondefinitionversionarn"""

    
