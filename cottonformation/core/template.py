# -*- coding: utf-8 -*-

"""
This module implements the core component CloudFormation Template. Many
black magic features are provided.
"""

import json
import attr
import typing

from collections import OrderedDict
from toposort import toposort
from .model import (
    _Addable,
    Parameter, Resource, Output, Rule, Mapping, Condition, Transform, Tag,
    TypeHint,
    get_id,
    get_key_value_dict,
    remove_id_and_empty,
    serialize,
    _class_type_to_attr_mapper,
)
from .constant import MetaData
from .config import CtfConfig
from ..res.cloudformation import Stack
from .._version import __version__


@attr.s
class Template:
    """
    .. warning::

        Don't ever directly edit the Template.Parameters, Template.Resources,
        Template.Outputs inplace. Please use the Template.add, Template.remove
        api. Because there's a lot of logic been handled to maintain the state
        of the inter relationship.

    Reference:

    - Template anatomy: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html
    """
    AWSTemplateFormatVersion: str = attr.ib(default="2010-09-09")
    Description: str = attr.ib(default="No description for this template")
    Metadata: dict = attr.ib(factory=OrderedDict)
    Parameters: typing.Dict[str, Parameter] = attr.ib(factory=OrderedDict)
    Rules: typing.Dict[str, Rule] = attr.ib(factory=OrderedDict)
    Mappings: typing.Dict[str, Mapping] = attr.ib(factory=OrderedDict)
    Conditions: typing.Dict[str, Condition] = attr.ib(factory=OrderedDict)
    Resources: typing.Dict[str, Resource] = attr.ib(factory=OrderedDict)
    Outputs: typing.Dict[str, Output] = attr.ib(factory=OrderedDict)
    Transform: typing.List['Transform'] = attr.ib(factory=list)
    NestedStack: typing.Dict[str, 'Template'] = attr.ib(factory=OrderedDict)

    _deps_data_need_build_flag: bool = attr.ib(default=True)
    _deps_on_data_cache: typing.Dict[str, typing.Set[str]] = attr.ib(factory=OrderedDict)
    _deps_by_data_cache: typing.Dict[str, typing.Set[str]] = attr.ib(factory=OrderedDict)
    _deps_sort_need_build_flag: bool = attr.ib(default=True)
    _deps_sort_cache: typing.Dict[str, int] = attr.ib(factory=OrderedDict)

    # handle the inter dependency relationship among Parameter, Mapping,
    # Condition, Resource, Output
    def _encode_depends_on(self, obj_list: typing.List[TypeHint.dependency_obj]) -> typing.Set[str]:
        """
        In generic dependency resolver algorithm, we don't need object,
        we only need the gid string. This method can ensure return a list of gid.
        """
        st = set()
        for obj in obj_list:
            if isinstance(obj, str):
                st.add(self.Resources[obj].gid)
            else:
                st.add(obj.gid)
        return st

    def _iterate_addable(self) -> typing.List[typing.Tuple[str, TypeHint.addable_obj]]:
        """
        Iterate through all addable object (Parameter, Resource, Output, ...).
        """
        l = list()
        for attr_name in _class_type_to_attr_mapper.values():
            collection = getattr(self, attr_name)
            for obj in collection.values():
                l.append((obj.gid, obj))
        return l

    def _iterate_addable_keys(self) -> typing.List[str]:
        return [gid for gid, _ in self._iterate_addable()]

    def _build_deps_data(self) -> typing.Tuple[typing.Dict[str, typing.Set[str]], typing.Dict[str, typing.Set[str]]]:
        deps_on_data = OrderedDict()
        deps_by_data = OrderedDict()
        for gid, _ in self._iterate_addable():
            deps_on_data[gid] = set()
            deps_by_data[gid] = set()

        for gid, obj in self._iterate_addable():
            deps_on_data[gid] = self._encode_depends_on(obj.DependsOn)
            for parent_gid in self._encode_depends_on(obj.DependsOn):
                deps_by_data[parent_gid].add(gid)

        return deps_on_data, deps_by_data

    @property
    def deps_on_data(self) -> typing.Dict[str, typing.Set[str]]:
        if self._deps_data_need_build_flag:
            deps_on_data, deps_by_data = self._build_deps_data()
            self._deps_on_data_cache = deps_on_data
            self._deps_by_data_cache = deps_by_data
            self._deps_data_need_build_flag = False
            self._deps_sort_need_build_flag = True
        return self._deps_on_data_cache

    @property
    def deps_by_data(self) -> typing.Dict[str, typing.Set[str]]:
        if self._deps_data_need_build_flag:
            deps_on_data, deps_by_data = self._build_deps_data()
            self._deps_on_data_cache = deps_on_data
            self._deps_by_data_cache = deps_by_data
            self._deps_data_need_build_flag = False
            self._deps_sort_need_build_flag = True
        return self._deps_by_data_cache

    @property
    def deps_sort(self) -> typing.Dict[str, int]:
        if self._deps_sort_need_build_flag:
            self._deps_sort_cache = OrderedDict()
            for ind, st in enumerate(toposort(self.deps_on_data)):
                st = list(st)
                st.sort()
                for v in st:
                    self._deps_sort_cache[v] = ind
            self._deps_sort_need_build_flag = False
        return self._deps_sort_cache

    # --- handle AWS Object
    def _add(self,
             obj: TypeHint.addable_obj,
             add_or_update: bool = False,
             add_or_ignore: bool = False) -> bool:
        """
        Add a AWS object to the template. Return a bool value to indicate that
        if any change been made.

        TODO: allow auto recursive add if DependsOn is defined.
        """
        # validate argument
        if not isinstance(obj, _Addable):
            raise TypeError(f"You cannot add {obj.__class__.__name__}")

        if add_or_update and add_or_ignore:
            raise ValueError("Can't do add_or_update=True and add_or_ignore=True")

        class_type, logic_id = obj.gid.split("--")
        collection = getattr(self, _class_type_to_attr_mapper[class_type])

        if isinstance(obj, Transform): # pragma: no cover
            collection.append(obj)
            self._deps_data_need_build_flag = True
            return True

        if obj.id in collection:
            if add_or_update:
                collection[obj.id] = obj
                self._deps_data_need_build_flag = True
                return True
            elif add_or_ignore:
                return False
            else:
                if isinstance(obj, Resource):
                    type_name = Resource.__name__
                else:
                    type_name = obj.__class__.__name__
                raise ValueError(f"{type_name} logic id '{obj.id}' already exists!")
        else:
            collection[obj.id] = obj
            self._deps_data_need_build_flag = True
            return True

    def add(self, obj: TypeHint.addable_obj) -> bool:
        return self._add(obj)

    def add_or_update(self, obj: TypeHint.addable_obj) -> bool:
        return self._add(obj, add_or_update=True)

    def add_or_ignore(self, obj: TypeHint.addable_obj) -> bool:
        return self._add(obj, add_or_ignore=True)

    def _get_by_gid(self, gid: str) -> TypeHint.addable_obj:
        class_type, logic_id = gid.split("--")
        collection = getattr(self, _class_type_to_attr_mapper[class_type])
        return collection[logic_id]

    def _remove_by_gid(self,
                       gid: str,
                       ignore_not_exists: bool = False):
        class_type, logic_id = gid.split("--")
        collection = getattr(self, _class_type_to_attr_mapper[class_type])

        if class_type == Transform.CLASS_TYPE: # pragma: no cover
            return

        if logic_id in collection:
            collection.pop(logic_id)
            self._deps_data_need_build_flag = True
            return True
        elif ignore_not_exists:
            return False
        else:
            if class_type == Resource.CLASS_TYPE:
                type_name = Resource.__name__
            else:
                type_name = _class_type_to_attr_mapper[class_type][:-1]
            raise ValueError(f"{type_name} logic id '{logic_id}' not exists!")

    def _remove(self,
                obj: TypeHint.addable_obj,
                ignore_not_exists: bool = False,
                _deps_data: OrderedDict = None) -> bool:
        """
        Remove a AWS object from the template. Return a bool value to indicate that
        if any change been made.

        **If the AWS object is a dependency for other objects, then other objects
        will also be removed**.
        """
        if _deps_data is None:
            _deps_data = self.deps_on_data

        for child_gid in self.deps_by_data.get(obj.gid, set()):
            self._remove(self._get_by_gid(child_gid), ignore_not_exists)

        return self._remove_by_gid(obj.gid, ignore_not_exists)

    def remove(self, obj: TypeHint.addable_obj) -> bool:
        return self._remove(obj)

    def remove_and_ignore(self, obj: TypeHint.addable_obj) -> bool:
        return self._remove(obj, ignore_not_exists=True)

    # --- nested stack
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

    # --- serialization
    def to_dict(self) -> dict:
        self.__pre_serialize__()

        dct = get_key_value_dict(self)
        dct.pop("NestedStack")
        dct.pop("_deps_data_need_build_flag")
        dct.pop("_deps_on_data_cache")
        dct.pop("_deps_by_data_cache")
        dct.pop("_deps_sort_need_build_flag")
        dct.pop("_deps_sort_cache")
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def to_json_file(self, path):  # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_json())

    def to_yml(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def to_yml_file(self, path):  # pragma: no cover
        with open(path, "w") as f:
            f.write(self.to_yml())

    def __attrs_post_init__(self):
        if CtfConfig.Template.enable_post_init_hook:
            self._system_post_init_hook()
            self.post_init_hook()

    def _system_post_init_hook(self):
        pass

    def post_init_hook(self):
        """
        User can overwrite this method to extend cottonformation.Template
        """
        pass

    def __pre_serialize__(self):
        if CtfConfig.Template.enable_pre_serialize_hook:
            self._system_pre_serialize_hook()
            self.pre_serialize_hook()

    def _system_pre_serialize_hook(self):
        self.Metadata.setdefault(MetaData.CTF, OrderedDict())
        self.Metadata[MetaData.CTF][MetaData.Version] = __version__


    def pre_serialize_hook(self):
        """
        User can overwrite this method to extend cottonformation.Template
        """
        pass

    def batch_tagging(self, overwrite: bool = False, **kwargs):
        """
        Batch tag all resources if supporting Tags.
        """
        for r in self.Resources.values():
            if r.support_tags():
                r.update_tags(overwrite, **kwargs)
