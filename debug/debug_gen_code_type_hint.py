# -*- coding: utf-8 -*-

"""
"""

from cottonformation.code.spec import CftSpec, _find_type_hint_and_validator

ctf_spec = CftSpec.new()
pt = ctf_spec.find_property_type("AWS::WAFv2::WebACL.ManagedRuleGroupStatement")
p = pt.find_property("ScopeDownStatement")
print(p)

print(
    _find_type_hint_and_validator(
        prop=p,
        prop_type_class_name="WebACLRateBasedStatement",
        cycled_class_name_set=set()
    )
)
# import cottonformation.res._imp
# _ = cottonformation.res._imp
