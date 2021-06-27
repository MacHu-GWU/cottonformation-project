# -*- coding: utf-8 -*-

import json
import attr
import typing
from .model import (
    Parameter, Resource, Output, Rule, Mapping, Condition, Transform,
    TypeHint, TypeCheck,
    get_id,
    get_key_value_dict,
    remove_id_and_empty,
    serialize,
)
from ..res.cloudformation import Stack


@attr.s
class Template:
    """
    Reference:

    - Template anatomy: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html
    """
    AWSTemplateFormatVersion: str = attr.ib(default="2010-09-09")
    Description: str = attr.ib(default="No description for this template")
    Metadata: dict = attr.ib(factory=dict)
    Parameters: typing.Dict[str, Parameter] = attr.ib(factory=dict)
    Rules: typing.Dict[str, Rule] = attr.ib(factory=dict)
    Mappings: typing.Dict[str, Mapping] = attr.ib(factory=dict)
    Conditions: typing.Dict[str, Condition] = attr.ib(factory=dict)
    Resources: typing.Dict[str, Resource] = attr.ib(factory=dict)
    Outputs: typing.Dict[str, Output] = attr.ib(factory=dict)
    Transform: typing.List['Transform'] = attr.ib(factory=list)
    NestedStack: typing.Dict[str, 'Template'] = attr.ib(factory=dict)

    #--- handle AWS Object
    def _add(self,
             obj: TypeHint.addable_obj,
             add_or_update: bool = False,
             add_or_ignore: bool = False):
        is_resource = False
        if isinstance(obj, Parameter):
            dct = self.Parameters
        elif isinstance(obj, Resource):
            dct = self.Resources
            is_resource = True
        elif isinstance(obj, Output): # pragma: no cover
            dct = self.Outputs
        elif isinstance(obj, Rule): # pragma: no cover
            dct = self.Rules
        elif isinstance(obj, Mapping): # pragma: no cover
            dct = self.Mappings
        elif isinstance(obj, Condition): # pragma: no cover
            dct = self.Conditions
        else:
            raise TypeError(f"You cannot add {obj.__class__.__name__}")
        if obj.id in dct:
            if add_or_update:
                dct[obj.id] = obj
            elif add_or_ignore:
                pass
            else:
                if is_resource:
                    type_name = Resource.__name__
                else:
                    type_name = obj.__class__.__name__
                raise ValueError(f"{type_name} logic id '{obj.id}' is already exists!")
        else:
            dct[obj.id] = obj

    def add(self, obj: TypeHint.addable_obj):
        self._add(obj)

    def add_or_update(self, obj: TypeHint.addable_obj):
        self._add(obj, add_or_update=True)

    def add_or_ignore(self, obj: TypeHint.addable_obj):
        self._add(obj, add_or_ignore=True)

    #--- nested stack
    def add_nested_stack(self,
                         stack: typing.Union[str, Stack],
                         template: 'Template') -> bool:
        """
        Reference:

        - Nested Stack: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html
        """
        stack_logic_id = get_id(stack)
        if stack_logic_id not in self.Resources:
            raise ValueError(
                "there's no AWS::CloudFormation::Stack resource defined in "
                "the template"
            )
        self.NestedStack[stack_logic_id] = template
        return True

    #--- serialization
    def to_dict(self) -> dict:
        dct = get_key_value_dict(self)
        dct.pop("NestedStack")
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def to_json_file(self, path): # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_json())

    def to_yml(self) -> str: # pragma: no cover
        raise NotImplementedError

    def to_yml_file(self, path): # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_yml())
