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
class PropReceiptRuleBounceAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.BounceAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html

    Property Document:
    
    - ``rp_Message``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
    - ``rp_Sender``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
    - ``rp_SmtpReplyCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
    - ``p_StatusCode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.BounceAction"
    
    rp_Message: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Message"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message"""
    rp_Sender: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Sender"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender"""
    rp_SmtpReplyCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SmtpReplyCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode"""
    p_StatusCode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "StatusCode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn"""

@attr.s
class PropConfigurationSetDashboardOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.DashboardOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html

    Property Document:
    
    - ``rp_EngagementMetrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html#cfn-ses-configurationset-dashboardoptions-engagementmetrics
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.DashboardOptions"
    
    rp_EngagementMetrics: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EngagementMetrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html#cfn-ses-configurationset-dashboardoptions-engagementmetrics"""

@attr.s
class PropConfigurationSetDeliveryOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.DeliveryOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html

    Property Document:
    
    - ``p_SendingPoolName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-sendingpoolname
    - ``p_TlsPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-tlspolicy
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.DeliveryOptions"
    
    p_SendingPoolName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SendingPoolName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-sendingpoolname"""
    p_TlsPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TlsPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-tlspolicy"""

@attr.s
class PropConfigurationSetGuardianOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.GuardianOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html

    Property Document:
    
    - ``rp_OptimizedSharedDelivery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html#cfn-ses-configurationset-guardianoptions-optimizedshareddelivery
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.GuardianOptions"
    
    rp_OptimizedSharedDelivery: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OptimizedSharedDelivery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html#cfn-ses-configurationset-guardianoptions-optimizedshareddelivery"""

@attr.s
class PropReceiptFilterIpFilter(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptFilter.IpFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html

    Property Document:
    
    - ``rp_Cidr``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr
    - ``rp_Policy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptFilter.IpFilter"
    
    rp_Cidr: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Cidr"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr"""
    rp_Policy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Policy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy"""

@attr.s
class PropConfigurationSetSuppressionOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.SuppressionOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html

    Property Document:
    
    - ``p_SuppressedReasons``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html#cfn-ses-configurationset-suppressionoptions-suppressedreasons
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.SuppressionOptions"
    
    p_SuppressedReasons: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SuppressedReasons"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html#cfn-ses-configurationset-suppressionoptions-suppressedreasons"""

@attr.s
class PropConfigurationSetVdmOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.VdmOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html

    Property Document:
    
    - ``p_DashboardOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-dashboardoptions
    - ``p_GuardianOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-guardianoptions
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.VdmOptions"
    
    p_DashboardOptions: typing.Union['PropConfigurationSetDashboardOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetDashboardOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetDashboardOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "DashboardOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-dashboardoptions"""
    p_GuardianOptions: typing.Union['PropConfigurationSetGuardianOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetGuardianOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetGuardianOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "GuardianOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-guardianoptions"""

@attr.s
class PropEmailIdentityFeedbackAttributes(Property):
    """
    AWS Object Type = "AWS::SES::EmailIdentity.FeedbackAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html

    Property Document:
    
    - ``p_EmailForwardingEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity.FeedbackAttributes"
    
    p_EmailForwardingEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EmailForwardingEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled"""

@attr.s
class PropEmailIdentityDkimSigningAttributes(Property):
    """
    AWS Object Type = "AWS::SES::EmailIdentity.DkimSigningAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html

    Property Document:
    
    - ``p_DomainSigningPrivateKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningprivatekey
    - ``p_DomainSigningSelector``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningselector
    - ``p_NextSigningKeyLength``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-nextsigningkeylength
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity.DkimSigningAttributes"
    
    p_DomainSigningPrivateKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainSigningPrivateKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningprivatekey"""
    p_DomainSigningSelector: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DomainSigningSelector"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningselector"""
    p_NextSigningKeyLength: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "NextSigningKeyLength"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-nextsigningkeylength"""

@attr.s
class PropTemplateTemplate(Property):
    """
    AWS Object Type = "AWS::SES::Template.Template"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html

    Property Document:
    
    - ``rp_SubjectPart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart
    - ``p_HtmlPart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart
    - ``p_TemplateName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename
    - ``p_TextPart``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart
    """
    AWS_OBJECT_TYPE = "AWS::SES::Template.Template"
    
    rp_SubjectPart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubjectPart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart"""
    p_HtmlPart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HtmlPart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart"""
    p_TemplateName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename"""
    p_TextPart: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TextPart"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart"""

@attr.s
class PropContactListTopic(Property):
    """
    AWS Object Type = "AWS::SES::ContactList.Topic"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html

    Property Document:
    
    - ``rp_DefaultSubscriptionStatus``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus
    - ``rp_DisplayName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname
    - ``rp_TopicName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description
    """
    AWS_OBJECT_TYPE = "AWS::SES::ContactList.Topic"
    
    rp_DefaultSubscriptionStatus: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultSubscriptionStatus"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus"""
    rp_DisplayName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DisplayName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname"""
    rp_TopicName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TopicName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description"""

@attr.s
class PropReceiptRuleWorkmailAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.WorkmailAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html

    Property Document:
    
    - ``rp_OrganizationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.WorkmailAction"
    
    rp_OrganizationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OrganizationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn"""

@attr.s
class PropReceiptRuleAddHeaderAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.AddHeaderAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html

    Property Document:
    
    - ``rp_HeaderName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
    - ``rp_HeaderValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.AddHeaderAction"
    
    rp_HeaderName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername"""
    rp_HeaderValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "HeaderValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue"""

@attr.s
class PropConfigurationSetEventDestinationDimensionConfiguration(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination.DimensionConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html

    Property Document:
    
    - ``rp_DefaultDimensionValue``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
    - ``rp_DimensionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname
    - ``rp_DimensionValueSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination.DimensionConfiguration"
    
    rp_DefaultDimensionValue: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultDimensionValue"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue"""
    rp_DimensionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname"""
    rp_DimensionValueSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionValueSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource"""

@attr.s
class PropReceiptRuleStopAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.StopAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html

    Property Document:
    
    - ``rp_Scope``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.StopAction"
    
    rp_Scope: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Scope"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn"""

@attr.s
class PropConfigurationSetReputationOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.ReputationOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html

    Property Document:
    
    - ``p_ReputationMetricsEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.ReputationOptions"
    
    p_ReputationMetricsEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ReputationMetricsEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled"""

@attr.s
class PropEmailIdentityMailFromAttributes(Property):
    """
    AWS Object Type = "AWS::SES::EmailIdentity.MailFromAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html

    Property Document:
    
    - ``p_BehaviorOnMxFailure``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-behavioronmxfailure
    - ``p_MailFromDomain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-mailfromdomain
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity.MailFromAttributes"
    
    p_BehaviorOnMxFailure: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BehaviorOnMxFailure"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-behavioronmxfailure"""
    p_MailFromDomain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "MailFromDomain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-mailfromdomain"""

@attr.s
class PropReceiptRuleSNSAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.SNSAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html

    Property Document:
    
    - ``p_Encoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.SNSAction"
    
    p_Encoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Encoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn"""

@attr.s
class PropConfigurationSetTrackingOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.TrackingOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html

    Property Document:
    
    - ``p_CustomRedirectDomain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html#cfn-ses-configurationset-trackingoptions-customredirectdomain
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.TrackingOptions"
    
    p_CustomRedirectDomain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomRedirectDomain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html#cfn-ses-configurationset-trackingoptions-customredirectdomain"""

@attr.s
class PropConfigurationSetSendingOptions(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet.SendingOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html

    Property Document:
    
    - ``p_SendingEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html#cfn-ses-configurationset-sendingoptions-sendingenabled
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet.SendingOptions"
    
    p_SendingEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SendingEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html#cfn-ses-configurationset-sendingoptions-sendingenabled"""

@attr.s
class PropConfigurationSetEventDestinationKinesisFirehoseDestination(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination.KinesisFirehoseDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html

    Property Document:
    
    - ``rp_DeliveryStreamARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
    - ``rp_IAMRoleARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination.KinesisFirehoseDestination"
    
    rp_DeliveryStreamARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DeliveryStreamARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn"""
    rp_IAMRoleARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IAMRoleARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn"""

@attr.s
class PropVdmAttributesDashboardAttributes(Property):
    """
    AWS Object Type = "AWS::SES::VdmAttributes.DashboardAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html

    Property Document:
    
    - ``p_EngagementMetrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics
    """
    AWS_OBJECT_TYPE = "AWS::SES::VdmAttributes.DashboardAttributes"
    
    p_EngagementMetrics: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EngagementMetrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics"""

@attr.s
class PropEmailIdentityDkimAttributes(Property):
    """
    AWS Object Type = "AWS::SES::EmailIdentity.DkimAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html

    Property Document:
    
    - ``p_SigningEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html#cfn-ses-emailidentity-dkimattributes-signingenabled
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity.DkimAttributes"
    
    p_SigningEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SigningEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html#cfn-ses-emailidentity-dkimattributes-signingenabled"""

@attr.s
class PropConfigurationSetEventDestinationSnsDestination(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination.SnsDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html

    Property Document:
    
    - ``rp_TopicARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html#cfn-ses-configurationseteventdestination-snsdestination-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination.SnsDestination"
    
    rp_TopicARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TopicARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html#cfn-ses-configurationseteventdestination-snsdestination-topicarn"""

@attr.s
class PropVdmAttributesGuardianAttributes(Property):
    """
    AWS Object Type = "AWS::SES::VdmAttributes.GuardianAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html

    Property Document:
    
    - ``p_OptimizedSharedDelivery``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery
    """
    AWS_OBJECT_TYPE = "AWS::SES::VdmAttributes.GuardianAttributes"
    
    p_OptimizedSharedDelivery: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OptimizedSharedDelivery"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery"""

@attr.s
class PropReceiptRuleS3Action(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.S3Action"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html

    Property Document:
    
    - ``rp_BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
    - ``p_KmsKeyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
    - ``p_ObjectKeyPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.S3Action"
    
    rp_BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname"""
    p_KmsKeyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn"""
    p_ObjectKeyPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectKeyPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn"""

@attr.s
class PropEmailIdentityConfigurationSetAttributes(Property):
    """
    AWS Object Type = "AWS::SES::EmailIdentity.ConfigurationSetAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html

    Property Document:
    
    - ``p_ConfigurationSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html#cfn-ses-emailidentity-configurationsetattributes-configurationsetname
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity.ConfigurationSetAttributes"
    
    p_ConfigurationSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationSetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html#cfn-ses-emailidentity-configurationsetattributes-configurationsetname"""

@attr.s
class PropReceiptRuleLambdaAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.LambdaAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html

    Property Document:
    
    - ``rp_FunctionArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
    - ``p_InvocationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
    - ``p_TopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.LambdaAction"
    
    rp_FunctionArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FunctionArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn"""
    p_InvocationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "InvocationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype"""
    p_TopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn"""

@attr.s
class PropReceiptRuleAction(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.Action"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html

    Property Document:
    
    - ``p_AddHeaderAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction
    - ``p_BounceAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction
    - ``p_LambdaAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction
    - ``p_S3Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action
    - ``p_SNSAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction
    - ``p_StopAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction
    - ``p_WorkmailAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.Action"
    
    p_AddHeaderAction: typing.Union['PropReceiptRuleAddHeaderAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleAddHeaderAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleAddHeaderAction)),
        metadata={AttrMeta.PROPERTY_NAME: "AddHeaderAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction"""
    p_BounceAction: typing.Union['PropReceiptRuleBounceAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleBounceAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleBounceAction)),
        metadata={AttrMeta.PROPERTY_NAME: "BounceAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction"""
    p_LambdaAction: typing.Union['PropReceiptRuleLambdaAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleLambdaAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleLambdaAction)),
        metadata={AttrMeta.PROPERTY_NAME: "LambdaAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction"""
    p_S3Action: typing.Union['PropReceiptRuleS3Action', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleS3Action.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleS3Action)),
        metadata={AttrMeta.PROPERTY_NAME: "S3Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action"""
    p_SNSAction: typing.Union['PropReceiptRuleSNSAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleSNSAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleSNSAction)),
        metadata={AttrMeta.PROPERTY_NAME: "SNSAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction"""
    p_StopAction: typing.Union['PropReceiptRuleStopAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleStopAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleStopAction)),
        metadata={AttrMeta.PROPERTY_NAME: "StopAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction"""
    p_WorkmailAction: typing.Union['PropReceiptRuleWorkmailAction', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleWorkmailAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropReceiptRuleWorkmailAction)),
        metadata={AttrMeta.PROPERTY_NAME: "WorkmailAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction"""

@attr.s
class PropReceiptFilterFilter(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptFilter.Filter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html

    Property Document:
    
    - ``rp_IpFilter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptFilter.Filter"
    
    rp_IpFilter: typing.Union['PropReceiptFilterIpFilter', dict] = attr.ib(
        default=None,
        converter=PropReceiptFilterIpFilter.from_dict,
        validator=attr.validators.instance_of(PropReceiptFilterIpFilter),
        metadata={AttrMeta.PROPERTY_NAME: "IpFilter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name"""

@attr.s
class PropConfigurationSetEventDestinationCloudWatchDestination(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination.CloudWatchDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html

    Property Document:
    
    - ``p_DimensionConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination.CloudWatchDestination"
    
    p_DimensionConfigurations: typing.List[typing.Union['PropConfigurationSetEventDestinationDimensionConfiguration', dict]] = attr.ib(
        default=None,
        converter=PropConfigurationSetEventDestinationDimensionConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropConfigurationSetEventDestinationDimensionConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DimensionConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations"""

@attr.s
class PropReceiptRuleRule(Property):
    """
    AWS Object Type = "AWS::SES::ReceiptRule.Rule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html

    Property Document:
    
    - ``p_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name
    - ``p_Recipients``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients
    - ``p_ScanEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled
    - ``p_TlsPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule.Rule"
    
    p_Actions: typing.List[typing.Union['PropReceiptRuleAction', dict]] = attr.ib(
        default=None,
        converter=PropReceiptRuleAction.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropReceiptRuleAction), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name"""
    p_Recipients: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Recipients"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients"""
    p_ScanEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "ScanEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled"""
    p_TlsPolicy: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TlsPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy"""

@attr.s
class PropConfigurationSetEventDestinationEventDestination(Property):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination.EventDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html

    Property Document:
    
    - ``rp_MatchingEventTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes
    - ``p_CloudWatchDestination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination
    - ``p_Enabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled
    - ``p_KinesisFirehoseDestination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name
    - ``p_SnsDestination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-snsdestination
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination.EventDestination"
    
    rp_MatchingEventTypes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "MatchingEventTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes"""
    p_CloudWatchDestination: typing.Union['PropConfigurationSetEventDestinationCloudWatchDestination', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetEventDestinationCloudWatchDestination.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetEventDestinationCloudWatchDestination)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchDestination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination"""
    p_Enabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "Enabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled"""
    p_KinesisFirehoseDestination: typing.Union['PropConfigurationSetEventDestinationKinesisFirehoseDestination', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetEventDestinationKinesisFirehoseDestination.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetEventDestinationKinesisFirehoseDestination)),
        metadata={AttrMeta.PROPERTY_NAME: "KinesisFirehoseDestination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name"""
    p_SnsDestination: typing.Union['PropConfigurationSetEventDestinationSnsDestination', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetEventDestinationSnsDestination.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetEventDestinationSnsDestination)),
        metadata={AttrMeta.PROPERTY_NAME: "SnsDestination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-snsdestination"""


#--- Resource declaration ---

@attr.s
class ContactList(Resource):
    """
    AWS Object Type = "AWS::SES::ContactList"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html

    Property Document:
    
    - ``p_ContactListName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
    - ``p_Topics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
    """
    AWS_OBJECT_TYPE = "AWS::SES::ContactList"

    
    p_ContactListName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ContactListName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Description",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description"""
    p_Topics: typing.List[typing.Union['PropContactListTopic', dict]] = attr.ib(
        default=None,
        converter=PropContactListTopic.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropContactListTopic), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Topics",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Topic',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={
            AttrMeta.PROPERTY_NAME: "Tags",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'List',
                "ItemType": 'Tag',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags"""

    

@attr.s
class ConfigurationSetEventDestination(Resource):
    """
    AWS Object Type = "AWS::SES::ConfigurationSetEventDestination"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html

    Property Document:
    
    - ``rp_ConfigurationSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
    - ``rp_EventDestination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSetEventDestination"

    
    rp_ConfigurationSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "ConfigurationSetName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname"""
    rp_EventDestination: typing.Union['PropConfigurationSetEventDestinationEventDestination', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetEventDestinationEventDestination.from_dict,
        validator=attr.validators.instance_of(PropConfigurationSetEventDestinationEventDestination),
        metadata={
            AttrMeta.PROPERTY_NAME: "EventDestination",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": True,
                "Type": 'EventDestination',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#aws-resource-ses-configurationseteventdestination-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class Template(Resource):
    """
    AWS Object Type = "AWS::SES::Template"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html

    Property Document:
    
    - ``p_Template``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
    """
    AWS_OBJECT_TYPE = "AWS::SES::Template"

    
    p_Template: typing.Union['PropTemplateTemplate', dict] = attr.ib(
        default=None,
        converter=PropTemplateTemplate.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropTemplateTemplate)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Template",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'Template',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#aws-resource-ses-template-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    

@attr.s
class ConfigurationSet(Resource):
    """
    AWS Object Type = "AWS::SES::ConfigurationSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html

    Property Document:
    
    - ``p_DeliveryOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
    - ``p_ReputationOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions
    - ``p_SendingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions
    - ``p_SuppressionOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions
    - ``p_TrackingOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions
    - ``p_VdmOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-vdmoptions
    """
    AWS_OBJECT_TYPE = "AWS::SES::ConfigurationSet"

    
    p_DeliveryOptions: typing.Union['PropConfigurationSetDeliveryOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetDeliveryOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetDeliveryOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DeliveryOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DeliveryOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "Name",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name"""
    p_ReputationOptions: typing.Union['PropConfigurationSetReputationOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetReputationOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetReputationOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ReputationOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'ReputationOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions"""
    p_SendingOptions: typing.Union['PropConfigurationSetSendingOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetSendingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetSendingOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SendingOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'SendingOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions"""
    p_SuppressionOptions: typing.Union['PropConfigurationSetSuppressionOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetSuppressionOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetSuppressionOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "SuppressionOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'SuppressionOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions"""
    p_TrackingOptions: typing.Union['PropConfigurationSetTrackingOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetTrackingOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetTrackingOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "TrackingOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'TrackingOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions"""
    p_VdmOptions: typing.Union['PropConfigurationSetVdmOptions', dict] = attr.ib(
        default=None,
        converter=PropConfigurationSetVdmOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropConfigurationSetVdmOptions)),
        metadata={
            AttrMeta.PROPERTY_NAME: "VdmOptions",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'VdmOptions',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-vdmoptions"""

    

@attr.s
class DedicatedIpPool(Resource):
    """
    AWS Object Type = "AWS::SES::DedicatedIpPool"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html

    Property Document:
    
    - ``p_PoolName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname
    - ``p_ScalingMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-scalingmode
    """
    AWS_OBJECT_TYPE = "AWS::SES::DedicatedIpPool"

    
    p_PoolName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "PoolName",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname"""
    p_ScalingMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ScalingMode",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": False,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-scalingmode"""

    

@attr.s
class ReceiptRuleSet(Resource):
    """
    AWS Object Type = "AWS::SES::ReceiptRuleSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html

    Property Document:
    
    - ``p_RuleSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRuleSet"

    
    p_RuleSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "RuleSetName",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname"""

    

@attr.s
class ReceiptFilter(Resource):
    """
    AWS Object Type = "AWS::SES::ReceiptFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html

    Property Document:
    
    - ``rp_Filter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptFilter"

    
    rp_Filter: typing.Union['PropReceiptFilterFilter', dict] = attr.ib(
        default=None,
        converter=PropReceiptFilterFilter.from_dict,
        validator=attr.validators.instance_of(PropReceiptFilterFilter),
        metadata={
            AttrMeta.PROPERTY_NAME: "Filter",
            AttrMeta.DATA: {
                "Type": 'Filter',
                "Required": True,
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter"""

    

@attr.s
class VdmAttributes(Resource):
    """
    AWS Object Type = "AWS::SES::VdmAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html

    Property Document:
    
    - ``p_DashboardAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-dashboardattributes
    - ``p_GuardianAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-guardianattributes
    """
    AWS_OBJECT_TYPE = "AWS::SES::VdmAttributes"

    
    p_DashboardAttributes: typing.Union['PropVdmAttributesDashboardAttributes', dict] = attr.ib(
        default=None,
        converter=PropVdmAttributesDashboardAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVdmAttributesDashboardAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DashboardAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DashboardAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-dashboardattributes"""
    p_GuardianAttributes: typing.Union['PropVdmAttributesGuardianAttributes', dict] = attr.ib(
        default=None,
        converter=PropVdmAttributesGuardianAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropVdmAttributesGuardianAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "GuardianAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'GuardianAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-guardianattributes"""

    
    @property
    def rv_VdmAttributesResourceId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#aws-resource-ses-vdmattributes-return-values"""
        return GetAtt(resource=self, attr_name="VdmAttributesResourceId")
    

@attr.s
class ReceiptRule(Resource):
    """
    AWS Object Type = "AWS::SES::ReceiptRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html

    Property Document:
    
    - ``rp_Rule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
    - ``rp_RuleSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
    - ``p_After``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
    """
    AWS_OBJECT_TYPE = "AWS::SES::ReceiptRule"

    
    rp_Rule: typing.Union['PropReceiptRuleRule', dict] = attr.ib(
        default=None,
        converter=PropReceiptRuleRule.from_dict,
        validator=attr.validators.instance_of(PropReceiptRuleRule),
        metadata={
            AttrMeta.PROPERTY_NAME: "Rule",
            AttrMeta.DATA: {
                "Type": 'Rule',
                "Required": True,
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule"""
    rp_RuleSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "RuleSetName",
            AttrMeta.DATA: {
                "Required": True,
                "PrimitiveType": 'String',
                "UpdateType": 'Immutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname"""
    p_After: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={
            AttrMeta.PROPERTY_NAME: "After",
            AttrMeta.DATA: {
                "Required": False,
                "PrimitiveType": 'String',
                "UpdateType": 'Mutable',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after"""

    

@attr.s
class EmailIdentity(Resource):
    """
    AWS Object Type = "AWS::SES::EmailIdentity"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html

    Property Document:
    
    - ``rp_EmailIdentity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity
    - ``p_ConfigurationSetAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes
    - ``p_DkimAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes
    - ``p_DkimSigningAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes
    - ``p_FeedbackAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes
    - ``p_MailFromAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes
    """
    AWS_OBJECT_TYPE = "AWS::SES::EmailIdentity"

    
    rp_EmailIdentity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={
            AttrMeta.PROPERTY_NAME: "EmailIdentity",
            AttrMeta.DATA: {
                "UpdateType": 'Immutable',
                "Required": True,
                "PrimitiveType": 'String',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity"""
    p_ConfigurationSetAttributes: typing.Union['PropEmailIdentityConfigurationSetAttributes', dict] = attr.ib(
        default=None,
        converter=PropEmailIdentityConfigurationSetAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEmailIdentityConfigurationSetAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "ConfigurationSetAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'ConfigurationSetAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes"""
    p_DkimAttributes: typing.Union['PropEmailIdentityDkimAttributes', dict] = attr.ib(
        default=None,
        converter=PropEmailIdentityDkimAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEmailIdentityDkimAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DkimAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DkimAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes"""
    p_DkimSigningAttributes: typing.Union['PropEmailIdentityDkimSigningAttributes', dict] = attr.ib(
        default=None,
        converter=PropEmailIdentityDkimSigningAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEmailIdentityDkimSigningAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "DkimSigningAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'DkimSigningAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes"""
    p_FeedbackAttributes: typing.Union['PropEmailIdentityFeedbackAttributes', dict] = attr.ib(
        default=None,
        converter=PropEmailIdentityFeedbackAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEmailIdentityFeedbackAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "FeedbackAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'FeedbackAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes"""
    p_MailFromAttributes: typing.Union['PropEmailIdentityMailFromAttributes', dict] = attr.ib(
        default=None,
        converter=PropEmailIdentityMailFromAttributes.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropEmailIdentityMailFromAttributes)),
        metadata={
            AttrMeta.PROPERTY_NAME: "MailFromAttributes",
            AttrMeta.DATA: {
                "UpdateType": 'Mutable',
                "Required": False,
                "Type": 'MailFromAttributes',
            }
        },
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes"""

    
    @property
    def rv_DkimDNSTokenName1(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenName1")
    
    @property
    def rv_DkimDNSTokenName2(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenName2")
    
    @property
    def rv_DkimDNSTokenName3(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenName3")
    
    @property
    def rv_DkimDNSTokenValue1(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenValue1")
    
    @property
    def rv_DkimDNSTokenValue2(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenValue2")
    
    @property
    def rv_DkimDNSTokenValue3(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#aws-resource-ses-emailidentity-return-values"""
        return GetAtt(resource=self, attr_name="DkimDNSTokenValue3")
    
