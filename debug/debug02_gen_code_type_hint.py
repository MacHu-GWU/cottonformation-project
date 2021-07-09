# -*- coding: utf-8 -*-

"""
If you can not import a aws service module in ``cottonformation.res.*.py``
most likely it's because of the type hint and validator code.

This code helps developer
"""

from cottonformation.code.spec import CftSpec, _find_type_hint_and_validator

ctf_spec = CftSpec.new()
pt = ctf_spec.find_property_type("AWS::WAFv2::WebACL.ManagedRuleGroupStatement")
p = pt.find_property("ScopeDownStatement")
print(p)

type_hint, validator, converter = _find_type_hint_and_validator(
    prop=p,
    prop_type_class_name="WebACLRateBasedStatement",
    cycled_class_name_set=set()
)

print(f"type_hint = {type_hint}")
print(f"validator = {validator}")
print(f"converter = {converter}")

# try import
# import cottonformation.res._imp
# _ = cottonformation.res._imp
