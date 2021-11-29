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
class PropRuleGroupTCPFlagField(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.TCPFlagField"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html

    Property Document:
    
    - ``rp_Flags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-flags
    - ``p_Masks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-masks
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.TCPFlagField"
    
    rp_Flags: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Flags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-flags"""
    p_Masks: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Masks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-tcpflagfield.html#cfn-networkfirewall-rulegroup-tcpflagfield-masks"""

@attr.s
class PropLoggingConfigurationLogDestinationConfig(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html

    Property Document:
    
    - ``rp_LogDestination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination
    - ``rp_LogDestinationType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype
    - ``rp_LogType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::LoggingConfiguration.LogDestinationConfig"
    
    rp_LogDestination: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogDestination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestination"""
    rp_LogDestinationType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogDestinationType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logdestinationtype"""
    rp_LogType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-logdestinationconfig.html#cfn-networkfirewall-loggingconfiguration-logdestinationconfig-logtype"""

@attr.s
class PropRuleGroupHeader(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.Header"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html

    Property Document:
    
    - ``rp_Destination``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destination
    - ``rp_DestinationPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destinationport
    - ``rp_Direction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-direction
    - ``rp_Protocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-protocol
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-source
    - ``rp_SourcePort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-sourceport
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.Header"
    
    rp_Destination: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Destination"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destination"""
    rp_DestinationPort: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-destinationport"""
    rp_Direction: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Direction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-direction"""
    rp_Protocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Protocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-protocol"""
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-source"""
    rp_SourcePort: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-header.html#cfn-networkfirewall-rulegroup-header-sourceport"""

@attr.s
class PropRuleGroupDimension(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.Dimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html#cfn-networkfirewall-rulegroup-dimension-value
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.Dimension"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-dimension.html#cfn-networkfirewall-rulegroup-dimension-value"""

@attr.s
class PropFirewallPolicyStatelessRuleGroupReference(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-priority
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-resourcearn
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.StatelessRuleGroupReference"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-priority"""
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statelessrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statelessrulegroupreference-resourcearn"""

@attr.s
class PropFirewallPolicyStatefulRuleGroupReference(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html

    Property Document:
    
    - ``rp_ResourceArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-resourcearn
    - ``p_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-priority
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.StatefulRuleGroupReference"
    
    rp_ResourceArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-resourcearn"""
    p_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulrulegroupreference.html#cfn-networkfirewall-firewallpolicy-statefulrulegroupreference-priority"""

@attr.s
class PropRuleGroupRuleOption(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RuleOption"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html

    Property Document:
    
    - ``rp_Keyword``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-keyword
    - ``p_Settings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-settings
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RuleOption"
    
    rp_Keyword: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Keyword"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-keyword"""
    p_Settings: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Settings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruleoption.html#cfn-networkfirewall-rulegroup-ruleoption-settings"""

@attr.s
class PropFirewallSubnetMapping(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::Firewall.SubnetMapping"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html

    Property Document:
    
    - ``rp_SubnetId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-subnetid
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::Firewall.SubnetMapping"
    
    rp_SubnetId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewall-subnetmapping.html#cfn-networkfirewall-firewall-subnetmapping-subnetid"""

@attr.s
class PropRuleGroupRulesSourceList(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RulesSourceList"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html

    Property Document:
    
    - ``rp_GeneratedRulesType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype
    - ``rp_TargetTypes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes
    - ``rp_Targets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targets
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RulesSourceList"
    
    rp_GeneratedRulesType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "GeneratedRulesType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-generatedrulestype"""
    rp_TargetTypes: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "TargetTypes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targettypes"""
    rp_Targets: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Targets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessourcelist.html#cfn-networkfirewall-rulegroup-rulessourcelist-targets"""

@attr.s
class PropFirewallPolicyDimension(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.Dimension"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html

    Property Document:
    
    - ``rp_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html#cfn-networkfirewall-firewallpolicy-dimension-value
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.Dimension"
    
    rp_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-dimension.html#cfn-networkfirewall-firewallpolicy-dimension-value"""

@attr.s
class PropRuleGroupPortRange(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.PortRange"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html

    Property Document:
    
    - ``rp_FromPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-fromport
    - ``rp_ToPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-toport
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.PortRange"
    
    rp_FromPort: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "FromPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-fromport"""
    rp_ToPort: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "ToPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portrange.html#cfn-networkfirewall-rulegroup-portrange-toport"""

@attr.s
class PropRuleGroupIPSet(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.IPSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html

    Property Document:
    
    - ``p_Definition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.IPSet"
    
    p_Definition: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Definition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ipset.html#cfn-networkfirewall-rulegroup-ipset-definition"""

@attr.s
class PropLoggingConfigurationLoggingConfiguration(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html

    Property Document:
    
    - ``rp_LogDestinationConfigs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration-logdestinationconfigs
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::LoggingConfiguration.LoggingConfiguration"
    
    rp_LogDestinationConfigs: typing.List[typing.Union['PropLoggingConfigurationLogDestinationConfig', dict]] = attr.ib(
        default=None,
        converter=PropLoggingConfigurationLogDestinationConfig.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropLoggingConfigurationLogDestinationConfig), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "LogDestinationConfigs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-loggingconfiguration-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration-logdestinationconfigs"""

@attr.s
class PropFirewallPolicyStatefulEngineOptions(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.StatefulEngineOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html

    Property Document:
    
    - ``p_RuleOrder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.StatefulEngineOptions"
    
    p_RuleOrder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleOrder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-statefulengineoptions.html#cfn-networkfirewall-firewallpolicy-statefulengineoptions-ruleorder"""

@attr.s
class PropRuleGroupStatefulRuleOptions(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.StatefulRuleOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html

    Property Document:
    
    - ``p_RuleOrder``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html#cfn-networkfirewall-rulegroup-statefulruleoptions-ruleorder
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.StatefulRuleOptions"
    
    p_RuleOrder: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleOrder"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulruleoptions.html#cfn-networkfirewall-rulegroup-statefulruleoptions-ruleorder"""

@attr.s
class PropRuleGroupPortSet(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.PortSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html

    Property Document:
    
    - ``p_Definition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html#cfn-networkfirewall-rulegroup-portset-definition
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.PortSet"
    
    p_Definition: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Definition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-portset.html#cfn-networkfirewall-rulegroup-portset-definition"""

@attr.s
class PropRuleGroupRuleVariables(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RuleVariables"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html

    Property Document:
    
    - ``p_IPSets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-ipsets
    - ``p_PortSets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-portsets
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RuleVariables"
    
    p_IPSets: typing.Union['PropRuleGroupIPSet', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupIPSet.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupIPSet)),
        metadata={AttrMeta.PROPERTY_NAME: "IPSets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-ipsets"""
    p_PortSets: typing.Union['PropRuleGroupPortSet', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupPortSet.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupPortSet)),
        metadata={AttrMeta.PROPERTY_NAME: "PortSets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulevariables.html#cfn-networkfirewall-rulegroup-rulevariables-portsets"""

@attr.s
class PropRuleGroupPublishMetricAction(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.PublishMetricAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html

    Property Document:
    
    - ``rp_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.PublishMetricAction"
    
    rp_Dimensions: typing.List[typing.Union['PropRuleGroupDimension', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupDimension.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupDimension), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-publishmetricaction.html#cfn-networkfirewall-rulegroup-publishmetricaction-dimensions"""

@attr.s
class PropRuleGroupAddress(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.Address"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html

    Property Document:
    
    - ``rp_AddressDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html#cfn-networkfirewall-rulegroup-address-addressdefinition
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.Address"
    
    rp_AddressDefinition: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AddressDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-address.html#cfn-networkfirewall-rulegroup-address-addressdefinition"""

@attr.s
class PropRuleGroupStatefulRule(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.StatefulRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html

    Property Document:
    
    - ``rp_Action``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-action
    - ``rp_Header``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-header
    - ``rp_RuleOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.StatefulRule"
    
    rp_Action: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Action"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-action"""
    rp_Header: typing.Union['PropRuleGroupHeader', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupHeader.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupHeader),
        metadata={AttrMeta.PROPERTY_NAME: "Header"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-header"""
    rp_RuleOptions: typing.List[typing.Union['PropRuleGroupRuleOption', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupRuleOption.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupRuleOption), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html#cfn-networkfirewall-rulegroup-statefulrule-ruleoptions"""

@attr.s
class PropRuleGroupActionDefinition(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.ActionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html

    Property Document:
    
    - ``p_PublishMetricAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.ActionDefinition"
    
    p_PublishMetricAction: typing.Union['PropRuleGroupPublishMetricAction', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupPublishMetricAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupPublishMetricAction)),
        metadata={AttrMeta.PROPERTY_NAME: "PublishMetricAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-actiondefinition.html#cfn-networkfirewall-rulegroup-actiondefinition-publishmetricaction"""

@attr.s
class PropFirewallPolicyPublishMetricAction(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html

    Property Document:
    
    - ``rp_Dimensions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.PublishMetricAction"
    
    rp_Dimensions: typing.List[typing.Union['PropFirewallPolicyDimension', dict]] = attr.ib(
        default=None,
        converter=PropFirewallPolicyDimension.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallPolicyDimension), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Dimensions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-publishmetricaction.html#cfn-networkfirewall-firewallpolicy-publishmetricaction-dimensions"""

@attr.s
class PropFirewallPolicyActionDefinition(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.ActionDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html

    Property Document:
    
    - ``p_PublishMetricAction``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html#cfn-networkfirewall-firewallpolicy-actiondefinition-publishmetricaction
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.ActionDefinition"
    
    p_PublishMetricAction: typing.Union['PropFirewallPolicyPublishMetricAction', dict] = attr.ib(
        default=None,
        converter=PropFirewallPolicyPublishMetricAction.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFirewallPolicyPublishMetricAction)),
        metadata={AttrMeta.PROPERTY_NAME: "PublishMetricAction"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-actiondefinition.html#cfn-networkfirewall-firewallpolicy-actiondefinition-publishmetricaction"""

@attr.s
class PropRuleGroupCustomAction(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.CustomAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html

    Property Document:
    
    - ``rp_ActionDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actiondefinition
    - ``rp_ActionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actionname
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.CustomAction"
    
    rp_ActionDefinition: typing.Union['PropRuleGroupActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupActionDefinition.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupActionDefinition),
        metadata={AttrMeta.PROPERTY_NAME: "ActionDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actiondefinition"""
    rp_ActionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ActionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-customaction.html#cfn-networkfirewall-rulegroup-customaction-actionname"""

@attr.s
class PropRuleGroupMatchAttributes(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.MatchAttributes"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html

    Property Document:
    
    - ``p_DestinationPorts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinationports
    - ``p_Destinations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinations
    - ``p_Protocols``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-protocols
    - ``p_SourcePorts``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sourceports
    - ``p_Sources``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sources
    - ``p_TCPFlags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-tcpflags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.MatchAttributes"
    
    p_DestinationPorts: typing.List[typing.Union['PropRuleGroupPortRange', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupPortRange.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupPortRange), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationPorts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinationports"""
    p_Destinations: typing.List[typing.Union['PropRuleGroupAddress', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupAddress.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupAddress), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Destinations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-destinations"""
    p_Protocols: typing.List[int] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(int), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Protocols"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-protocols"""
    p_SourcePorts: typing.List[typing.Union['PropRuleGroupPortRange', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupPortRange.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupPortRange), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SourcePorts"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sourceports"""
    p_Sources: typing.List[typing.Union['PropRuleGroupAddress', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupAddress.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupAddress), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Sources"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-sources"""
    p_TCPFlags: typing.List[typing.Union['PropRuleGroupTCPFlagField', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupTCPFlagField.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupTCPFlagField), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TCPFlags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-matchattributes.html#cfn-networkfirewall-rulegroup-matchattributes-tcpflags"""

@attr.s
class PropFirewallPolicyCustomAction(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.CustomAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html

    Property Document:
    
    - ``rp_ActionDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actiondefinition
    - ``rp_ActionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actionname
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.CustomAction"
    
    rp_ActionDefinition: typing.Union['PropFirewallPolicyActionDefinition', dict] = attr.ib(
        default=None,
        converter=PropFirewallPolicyActionDefinition.from_dict,
        validator=attr.validators.instance_of(PropFirewallPolicyActionDefinition),
        metadata={AttrMeta.PROPERTY_NAME: "ActionDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actiondefinition"""
    rp_ActionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ActionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-customaction.html#cfn-networkfirewall-firewallpolicy-customaction-actionname"""

@attr.s
class PropRuleGroupRuleDefinition(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RuleDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html

    Property Document:
    
    - ``rp_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-actions
    - ``rp_MatchAttributes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-matchattributes
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RuleDefinition"
    
    rp_Actions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-actions"""
    rp_MatchAttributes: typing.Union['PropRuleGroupMatchAttributes', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupMatchAttributes.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupMatchAttributes),
        metadata={AttrMeta.PROPERTY_NAME: "MatchAttributes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-ruledefinition.html#cfn-networkfirewall-rulegroup-ruledefinition-matchattributes"""

@attr.s
class PropRuleGroupStatelessRule(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.StatelessRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html

    Property Document:
    
    - ``rp_Priority``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-priority
    - ``rp_RuleDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-ruledefinition
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.StatelessRule"
    
    rp_Priority: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Priority"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-priority"""
    rp_RuleDefinition: typing.Union['PropRuleGroupRuleDefinition', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRuleDefinition.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupRuleDefinition),
        metadata={AttrMeta.PROPERTY_NAME: "RuleDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrule.html#cfn-networkfirewall-rulegroup-statelessrule-ruledefinition"""

@attr.s
class PropFirewallPolicyFirewallPolicy(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html

    Property Document:
    
    - ``rp_StatelessDefaultActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions
    - ``rp_StatelessFragmentDefaultActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions
    - ``p_StatefulDefaultActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions
    - ``p_StatefulEngineOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions
    - ``p_StatefulRuleGroupReferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences
    - ``p_StatelessCustomActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions
    - ``p_StatelessRuleGroupReferences``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy.FirewallPolicy"
    
    rp_StatelessDefaultActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessDefaultActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessdefaultactions"""
    rp_StatelessFragmentDefaultActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessFragmentDefaultActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessfragmentdefaultactions"""
    p_StatefulDefaultActions: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StatefulDefaultActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefuldefaultactions"""
    p_StatefulEngineOptions: typing.Union['PropFirewallPolicyStatefulEngineOptions', dict] = attr.ib(
        default=None,
        converter=PropFirewallPolicyStatefulEngineOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropFirewallPolicyStatefulEngineOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "StatefulEngineOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulengineoptions"""
    p_StatefulRuleGroupReferences: typing.List[typing.Union['PropFirewallPolicyStatefulRuleGroupReference', dict]] = attr.ib(
        default=None,
        converter=PropFirewallPolicyStatefulRuleGroupReference.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallPolicyStatefulRuleGroupReference), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StatefulRuleGroupReferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statefulrulegroupreferences"""
    p_StatelessCustomActions: typing.List[typing.Union['PropFirewallPolicyCustomAction', dict]] = attr.ib(
        default=None,
        converter=PropFirewallPolicyCustomAction.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallPolicyCustomAction), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessCustomActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelesscustomactions"""
    p_StatelessRuleGroupReferences: typing.List[typing.Union['PropFirewallPolicyStatelessRuleGroupReference', dict]] = attr.ib(
        default=None,
        converter=PropFirewallPolicyStatelessRuleGroupReference.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallPolicyStatelessRuleGroupReference), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessRuleGroupReferences"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-firewallpolicy-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy-statelessrulegroupreferences"""

@attr.s
class PropRuleGroupStatelessRulesAndCustomActions(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html

    Property Document:
    
    - ``rp_StatelessRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules
    - ``p_CustomActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.StatelessRulesAndCustomActions"
    
    rp_StatelessRules: typing.List[typing.Union['PropRuleGroupStatelessRule', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupStatelessRule.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupStatelessRule), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-statelessrules"""
    p_CustomActions: typing.List[typing.Union['PropRuleGroupCustomAction', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupCustomAction.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupCustomAction), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statelessrulesandcustomactions.html#cfn-networkfirewall-rulegroup-statelessrulesandcustomactions-customactions"""

@attr.s
class PropRuleGroupRulesSource(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RulesSource"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html

    Property Document:
    
    - ``p_RulesSourceList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist
    - ``p_RulesString``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring
    - ``p_StatefulRules``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules
    - ``p_StatelessRulesAndCustomActions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RulesSource"
    
    p_RulesSourceList: typing.Union['PropRuleGroupRulesSourceList', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRulesSourceList.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRulesSourceList)),
        metadata={AttrMeta.PROPERTY_NAME: "RulesSourceList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulessourcelist"""
    p_RulesString: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "RulesString"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-rulesstring"""
    p_StatefulRules: typing.List[typing.Union['PropRuleGroupStatefulRule', dict]] = attr.ib(
        default=None,
        converter=PropRuleGroupStatefulRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropRuleGroupStatefulRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StatefulRules"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statefulrules"""
    p_StatelessRulesAndCustomActions: typing.Union['PropRuleGroupStatelessRulesAndCustomActions', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupStatelessRulesAndCustomActions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupStatelessRulesAndCustomActions)),
        metadata={AttrMeta.PROPERTY_NAME: "StatelessRulesAndCustomActions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulessource.html#cfn-networkfirewall-rulegroup-rulessource-statelessrulesandcustomactions"""

@attr.s
class PropRuleGroupRuleGroup(Property):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup.RuleGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html

    Property Document:
    
    - ``rp_RulesSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulessource
    - ``p_RuleVariables``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulevariables
    - ``p_StatefulRuleOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-statefulruleoptions
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup.RuleGroup"
    
    rp_RulesSource: typing.Union['PropRuleGroupRulesSource', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRulesSource.from_dict,
        validator=attr.validators.instance_of(PropRuleGroupRulesSource),
        metadata={AttrMeta.PROPERTY_NAME: "RulesSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulessource"""
    p_RuleVariables: typing.Union['PropRuleGroupRuleVariables', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRuleVariables.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRuleVariables)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleVariables"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-rulevariables"""
    p_StatefulRuleOptions: typing.Union['PropRuleGroupStatefulRuleOptions', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupStatefulRuleOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupStatefulRuleOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "StatefulRuleOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup-statefulruleoptions"""


#--- Resource declaration ---

@attr.s
class FirewallPolicy(Resource):
    """
    AWS Object Type = "AWS::NetworkFirewall::FirewallPolicy"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html

    Property Document:
    
    - ``rp_FirewallPolicy``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy
    - ``rp_FirewallPolicyName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::FirewallPolicy"

    
    rp_FirewallPolicy: typing.Union['PropFirewallPolicyFirewallPolicy', dict] = attr.ib(
        default=None,
        converter=PropFirewallPolicyFirewallPolicy.from_dict,
        validator=attr.validators.instance_of(PropFirewallPolicyFirewallPolicy),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallPolicy"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicy"""
    rp_FirewallPolicyName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallPolicyName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-firewallpolicyname"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-description"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#cfn-networkfirewall-firewallpolicy-tags"""

    
    @property
    def rv_FirewallPolicyArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#aws-resource-networkfirewall-firewallpolicy-return-values"""
        return GetAtt(resource=self, attr_name="FirewallPolicyArn")
    
    @property
    def rv_FirewallPolicyId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewallpolicy.html#aws-resource-networkfirewall-firewallpolicy-return-values"""
        return GetAtt(resource=self, attr_name="FirewallPolicyId")
    

@attr.s
class Firewall(Resource):
    """
    AWS Object Type = "AWS::NetworkFirewall::Firewall"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html

    Property Document:
    
    - ``rp_FirewallName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname
    - ``rp_FirewallPolicyArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn
    - ``rp_SubnetMappings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings
    - ``rp_VpcId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid
    - ``p_DeleteProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description
    - ``p_FirewallPolicyChangeProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection
    - ``p_SubnetChangeProtection``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::Firewall"

    
    rp_FirewallName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallname"""
    rp_FirewallPolicyArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallPolicyArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicyarn"""
    rp_SubnetMappings: typing.List[typing.Union['PropFirewallSubnetMapping', dict]] = attr.ib(
        default=None,
        converter=PropFirewallSubnetMapping.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(PropFirewallSubnetMapping), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetMappings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetmappings"""
    rp_VpcId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "VpcId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-vpcid"""
    p_DeleteProtection: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "DeleteProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-deleteprotection"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-description"""
    p_FirewallPolicyChangeProtection: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallPolicyChangeProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-firewallpolicychangeprotection"""
    p_SubnetChangeProtection: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetChangeProtection"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-subnetchangeprotection"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#cfn-networkfirewall-firewall-tags"""

    
    @property
    def rv_FirewallArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#aws-resource-networkfirewall-firewall-return-values"""
        return GetAtt(resource=self, attr_name="FirewallArn")
    
    @property
    def rv_FirewallId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#aws-resource-networkfirewall-firewall-return-values"""
        return GetAtt(resource=self, attr_name="FirewallId")
    
    @property
    def rv_EndpointIds(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-firewall.html#aws-resource-networkfirewall-firewall-return-values"""
        return GetAtt(resource=self, attr_name="EndpointIds")
    

@attr.s
class LoggingConfiguration(Resource):
    """
    AWS Object Type = "AWS::NetworkFirewall::LoggingConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html

    Property Document:
    
    - ``rp_FirewallArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn
    - ``rp_LoggingConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration
    - ``p_FirewallName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::LoggingConfiguration"

    
    rp_FirewallArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallarn"""
    rp_LoggingConfiguration: typing.Union['PropLoggingConfigurationLoggingConfiguration', dict] = attr.ib(
        default=None,
        converter=PropLoggingConfigurationLoggingConfiguration.from_dict,
        validator=attr.validators.instance_of(PropLoggingConfigurationLoggingConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "LoggingConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-loggingconfiguration"""
    p_FirewallName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FirewallName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-loggingconfiguration.html#cfn-networkfirewall-loggingconfiguration-firewallname"""

    

@attr.s
class RuleGroup(Resource):
    """
    AWS Object Type = "AWS::NetworkFirewall::RuleGroup"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html

    Property Document:
    
    - ``rp_Capacity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity
    - ``rp_RuleGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname
    - ``rp_Type``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description
    - ``p_RuleGroup``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags
    """
    AWS_OBJECT_TYPE = "AWS::NetworkFirewall::RuleGroup"

    
    rp_Capacity: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Capacity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-capacity"""
    rp_RuleGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RuleGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroupname"""
    rp_Type: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Type"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-type"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-description"""
    p_RuleGroup: typing.Union['PropRuleGroupRuleGroup', dict] = attr.ib(
        default=None,
        converter=PropRuleGroupRuleGroup.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PropRuleGroupRuleGroup)),
        metadata={AttrMeta.PROPERTY_NAME: "RuleGroup"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-rulegroup"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#cfn-networkfirewall-rulegroup-tags"""

    
    @property
    def rv_RuleGroupArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#aws-resource-networkfirewall-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="RuleGroupArn")
    
    @property
    def rv_RuleGroupId(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkfirewall-rulegroup.html#aws-resource-networkfirewall-rulegroup-return-values"""
        return GetAtt(resource=self, attr_name="RuleGroupId")
    
