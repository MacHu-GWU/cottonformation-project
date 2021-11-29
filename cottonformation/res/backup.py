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
class PropBackupSelectionConditionResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupSelection.ConditionResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html

    Property Document:
    
    - ``rp_ConditionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionkey
    - ``rp_ConditionType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditiontype
    - ``rp_ConditionValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionvalue
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupSelection.ConditionResourceType"
    
    rp_ConditionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConditionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionkey"""
    rp_ConditionType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConditionType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditiontype"""
    rp_ConditionValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConditionValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionvalue"""

@attr.s
class PropBackupVaultNotificationObjectType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupVault.NotificationObjectType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html

    Property Document:
    
    - ``rp_BackupVaultEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-backupvaultevents
    - ``rp_SNSTopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-snstopicarn
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupVault.NotificationObjectType"
    
    rp_BackupVaultEvents: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "BackupVaultEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-backupvaultevents"""
    rp_SNSTopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SNSTopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-snstopicarn"""

@attr.s
class PropBackupPlanAdvancedBackupSettingResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupPlan.AdvancedBackupSettingResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html

    Property Document:
    
    - ``rp_BackupOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions
    - ``rp_ResourceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan.AdvancedBackupSettingResourceType"
    
    rp_BackupOptions: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "BackupOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions"""
    rp_ResourceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype"""

@attr.s
class PropBackupVaultLockConfigurationType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupVault.LockConfigurationType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html

    Property Document:
    
    - ``rp_MinRetentionDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-minretentiondays
    - ``p_ChangeableForDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-changeablefordays
    - ``p_MaxRetentionDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-maxretentiondays
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupVault.LockConfigurationType"
    
    rp_MinRetentionDays: float = attr.ib(
        default=None,
        validator=attr.validators.instance_of(float),
        metadata={AttrMeta.PROPERTY_NAME: "MinRetentionDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-minretentiondays"""
    p_ChangeableForDays: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ChangeableForDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-changeablefordays"""
    p_MaxRetentionDays: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MaxRetentionDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-maxretentiondays"""

@attr.s
class PropBackupPlanLifecycleResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupPlan.LifecycleResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html

    Property Document:
    
    - ``p_DeleteAfterDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays
    - ``p_MoveToColdStorageAfterDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan.LifecycleResourceType"
    
    p_DeleteAfterDays: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteAfterDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays"""
    p_MoveToColdStorageAfterDays: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "MoveToColdStorageAfterDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays"""

@attr.s
class PropBackupSelectionBackupSelectionResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupSelection.BackupSelectionResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html

    Property Document:
    
    - ``rp_IamRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-iamrolearn
    - ``rp_SelectionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-selectionname
    - ``p_Conditions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-conditions
    - ``p_ListOfTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-listoftags
    - ``p_NotResources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-notresources
    - ``p_Resources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-resources
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupSelection.BackupSelectionResourceType"
    
    rp_IamRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IamRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-iamrolearn"""
    rp_SelectionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SelectionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-selectionname"""
    p_Conditions: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "Conditions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-conditions"""
    p_ListOfTags: typing.List[typing.Union['PropBackupSelectionConditionResourceType', dict]] = attr.ib(
        default=None,
        converter=PropBackupSelectionConditionResourceType.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBackupSelectionConditionResourceType), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ListOfTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-listoftags"""
    p_NotResources: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "NotResources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-notresources"""
    p_Resources: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Resources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-resources"""

@attr.s
class PropFrameworkControlInputParameter(Property):
    """
    AWS Object Type = "AWS::Backup::Framework.ControlInputParameter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html

    Property Document:
    
    - ``rp_ParameterName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametername
    - ``rp_ParameterValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametervalue
    """
    AWS_OBJECT_TYPE = "AWS::Backup::Framework.ControlInputParameter"
    
    rp_ParameterName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametername"""
    rp_ParameterValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ParameterValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametervalue"""

@attr.s
class PropBackupPlanCopyActionResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupPlan.CopyActionResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html

    Property Document:
    
    - ``rp_DestinationBackupVaultArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-destinationbackupvaultarn
    - ``p_Lifecycle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-lifecycle
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan.CopyActionResourceType"
    
    rp_DestinationBackupVaultArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationBackupVaultArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-destinationbackupvaultarn"""
    p_Lifecycle: typing.Union['PropBackupPlanLifecycleResourceType', dict] = attr.ib(
        default=None,
        converter=PropBackupPlanLifecycleResourceType.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBackupPlanLifecycleResourceType)),
        metadata={AttrMeta.PROPERTY_NAME: "Lifecycle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-lifecycle"""

@attr.s
class PropFrameworkFrameworkControl(Property):
    """
    AWS Object Type = "AWS::Backup::Framework.FrameworkControl"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html

    Property Document:
    
    - ``rp_ControlName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlname
    - ``p_ControlInputParameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlinputparameters
    - ``p_ControlScope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlscope
    """
    AWS_OBJECT_TYPE = "AWS::Backup::Framework.FrameworkControl"
    
    rp_ControlName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ControlName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlname"""
    p_ControlInputParameters: typing.List[typing.Union['PropFrameworkControlInputParameter', dict]] = attr.ib(
        default=None,
        converter=PropFrameworkControlInputParameter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFrameworkControlInputParameter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ControlInputParameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlinputparameters"""
    p_ControlScope: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "ControlScope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlscope"""

@attr.s
class PropBackupPlanBackupRuleResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupPlan.BackupRuleResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html

    Property Document:
    
    - ``rp_RuleName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-rulename
    - ``rp_TargetBackupVault``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault
    - ``p_CompletionWindowMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes
    - ``p_CopyActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-copyactions
    - ``p_EnableContinuousBackup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup
    - ``p_Lifecycle``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-lifecycle
    - ``p_RecoveryPointTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags
    - ``p_ScheduleExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression
    - ``p_StartWindowMinutes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan.BackupRuleResourceType"
    
    rp_RuleName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-rulename"""
    rp_TargetBackupVault: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TargetBackupVault"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault"""
    p_CompletionWindowMinutes: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "CompletionWindowMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes"""
    p_CopyActions: typing.List[typing.Union['PropBackupPlanCopyActionResourceType', dict]] = attr.ib(
        default=None,
        converter=PropBackupPlanCopyActionResourceType.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBackupPlanCopyActionResourceType), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CopyActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-copyactions"""
    p_EnableContinuousBackup: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableContinuousBackup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup"""
    p_Lifecycle: typing.Union['PropBackupPlanLifecycleResourceType', dict] = attr.ib(
        default=None,
        converter=PropBackupPlanLifecycleResourceType.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBackupPlanLifecycleResourceType)),
        metadata={AttrMeta.PROPERTY_NAME: "Lifecycle"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-lifecycle"""
    p_RecoveryPointTags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "RecoveryPointTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags"""
    p_ScheduleExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression"""
    p_StartWindowMinutes: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "StartWindowMinutes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes"""

@attr.s
class PropBackupPlanBackupPlanResourceType(Property):
    """
    AWS Object Type = "AWS::Backup::BackupPlan.BackupPlanResourceType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html

    Property Document:
    
    - ``rp_BackupPlanName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanname
    - ``rp_BackupPlanRule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanrule
    - ``p_AdvancedBackupSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan.BackupPlanResourceType"
    
    rp_BackupPlanName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPlanName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanname"""
    rp_BackupPlanRule: typing.List[typing.Union['PropBackupPlanBackupRuleResourceType', dict]] = attr.ib(
        default=None,
        converter=PropBackupPlanBackupRuleResourceType.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBackupPlanBackupRuleResourceType), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPlanRule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanrule"""
    p_AdvancedBackupSettings: typing.List[typing.Union['PropBackupPlanAdvancedBackupSettingResourceType', dict]] = attr.ib(
        default=None,
        converter=PropBackupPlanAdvancedBackupSettingResourceType.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropBackupPlanAdvancedBackupSettingResourceType), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AdvancedBackupSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings"""


#--- Resource declaration ---

@attr.s
class BackupPlan(Resource):
    """
    AWS Object Type = "AWS::Backup::BackupPlan"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html

    Property Document:
    
    - ``rp_BackupPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan
    - ``p_BackupPlanTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupPlan"

    
    rp_BackupPlan: typing.Union['PropBackupPlanBackupPlanResourceType', dict] = attr.ib(
        default=None,
        converter=PropBackupPlanBackupPlanResourceType.from_dict,
        validator=attr.validators.instance_of(PropBackupPlanBackupPlanResourceType),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan"""
    p_BackupPlanTags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPlanTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags"""

    
    @property
    def rv_BackupPlanArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#aws-resource-backup-backupplan-return-values"""
        return GetAtt(resource=self, attr_name="BackupPlanArn")
    
    @property
    def rv_BackupPlanId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#aws-resource-backup-backupplan-return-values"""
        return GetAtt(resource=self, attr_name="BackupPlanId")
    
    @property
    def rv_VersionId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#aws-resource-backup-backupplan-return-values"""
        return GetAtt(resource=self, attr_name="VersionId")
    

@attr.s
class Framework(Resource):
    """
    AWS Object Type = "AWS::Backup::Framework"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html

    Property Document:
    
    - ``rp_FrameworkControls``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols
    - ``p_FrameworkDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription
    - ``p_FrameworkName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname
    - ``p_FrameworkTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags
    """
    AWS_OBJECT_TYPE = "AWS::Backup::Framework"

    
    rp_FrameworkControls: typing.List[typing.Union['PropFrameworkFrameworkControl', dict]] = attr.ib(
        default=None,
        converter=PropFrameworkFrameworkControl.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFrameworkFrameworkControl), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "FrameworkControls"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols"""
    p_FrameworkDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FrameworkDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription"""
    p_FrameworkName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FrameworkName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname"""
    p_FrameworkTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FrameworkTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags"""

    
    @property
    def rv_FrameworkArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#aws-resource-backup-framework-return-values"""
        return GetAtt(resource=self, attr_name="FrameworkArn")
    
    @property
    def rv_DeploymentStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#aws-resource-backup-framework-return-values"""
        return GetAtt(resource=self, attr_name="DeploymentStatus")
    
    @property
    def rv_CreationTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#aws-resource-backup-framework-return-values"""
        return GetAtt(resource=self, attr_name="CreationTime")
    
    @property
    def rv_FrameworkStatus(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#aws-resource-backup-framework-return-values"""
        return GetAtt(resource=self, attr_name="FrameworkStatus")
    

@attr.s
class BackupVault(Resource):
    """
    AWS Object Type = "AWS::Backup::BackupVault"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html

    Property Document:
    
    - ``rp_BackupVaultName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname
    - ``p_AccessPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy
    - ``p_BackupVaultTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags
    - ``p_EncryptionKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn
    - ``p_LockConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration
    - ``p_Notifications``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupVault"

    
    rp_BackupVaultName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BackupVaultName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname"""
    p_AccessPolicy: dict = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(dict)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy"""
    p_BackupVaultTags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "BackupVaultTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags"""
    p_EncryptionKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn"""
    p_LockConfiguration: typing.Union['PropBackupVaultLockConfigurationType', dict] = attr.ib(
        default=None,
        converter=PropBackupVaultLockConfigurationType.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBackupVaultLockConfigurationType)),
        metadata={AttrMeta.PROPERTY_NAME: "LockConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration"""
    p_Notifications: typing.Union['PropBackupVaultNotificationObjectType', dict] = attr.ib(
        default=None,
        converter=PropBackupVaultNotificationObjectType.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropBackupVaultNotificationObjectType)),
        metadata={AttrMeta.PROPERTY_NAME: "Notifications"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications"""

    
    @property
    def rv_BackupVaultName(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#aws-resource-backup-backupvault-return-values"""
        return GetAtt(resource=self, attr_name="BackupVaultName")
    
    @property
    def rv_BackupVaultArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#aws-resource-backup-backupvault-return-values"""
        return GetAtt(resource=self, attr_name="BackupVaultArn")
    

@attr.s
class ReportPlan(Resource):
    """
    AWS Object Type = "AWS::Backup::ReportPlan"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html

    Property Document:
    
    - ``rp_ReportDeliveryChannel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel
    - ``rp_ReportSetting``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting
    - ``p_ReportPlanDescription``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription
    - ``p_ReportPlanName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname
    - ``p_ReportPlanTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags
    """
    AWS_OBJECT_TYPE = "AWS::Backup::ReportPlan"

    
    rp_ReportDeliveryChannel: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "ReportDeliveryChannel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel"""
    rp_ReportSetting: dict = attr.ib(
        default=None,
        validator=attr.validators.instance_of(dict),
        metadata={AttrMeta.PROPERTY_NAME: "ReportSetting"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting"""
    p_ReportPlanDescription: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportPlanDescription"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription"""
    p_ReportPlanName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ReportPlanName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname"""
    p_ReportPlanTags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ReportPlanTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags"""

    
    @property
    def rv_ReportPlanArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#aws-resource-backup-reportplan-return-values"""
        return GetAtt(resource=self, attr_name="ReportPlanArn")
    

@attr.s
class BackupSelection(Resource):
    """
    AWS Object Type = "AWS::Backup::BackupSelection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html

    Property Document:
    
    - ``rp_BackupPlanId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid
    - ``rp_BackupSelection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection
    """
    AWS_OBJECT_TYPE = "AWS::Backup::BackupSelection"

    
    rp_BackupPlanId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BackupPlanId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid"""
    rp_BackupSelection: typing.Union['PropBackupSelectionBackupSelectionResourceType', dict] = attr.ib(
        default=None,
        converter=PropBackupSelectionBackupSelectionResourceType.from_dict,
        validator=attr.validators.instance_of(PropBackupSelectionBackupSelectionResourceType),
        metadata={AttrMeta.PROPERTY_NAME: "BackupSelection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#aws-resource-backup-backupselection-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
    @property
    def rv_BackupPlanId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#aws-resource-backup-backupselection-return-values"""
        return GetAtt(resource=self, attr_name="BackupPlanId")
    
    @property
    def rv_SelectionId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#aws-resource-backup-backupselection-return-values"""
        return GetAtt(resource=self, attr_name="SelectionId")
    
