# -*- coding: utf-8 -*-

"""
This module implements the core component CloudFormation Template. Many
black magic features are provided.
"""

import json
import attr
import typing
from collections import OrderedDict

import cfn_flip
from toposort import toposort

from .model import (
    _Addable,
    Parameter, Resource, Output, Rule, Mapping, Condition, Transform, ResourceGroup, Tag,
    TypeHint,
    get_id,
    get_key_value_dict,
    remove_id_and_empty,
    serialize,
    _class_type_to_attr_mapper,
)
from .constant import MetaData, CloudFomation
from .config import CtfConfig
from .exc import (
    AWSObjectLogicIdConflictError,
    AWSObjectNotExistsError,
)
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
    Groups: typing.Dict[str, 'ResourceGroup'] = attr.ib(factory=OrderedDict)

    _deps_data_need_build_flag: bool = attr.ib(default=True)
    _deps_on_data_cache: typing.Dict[str, typing.Set[str]] = attr.ib(factory=OrderedDict)
    _deps_by_data_cache: typing.Dict[str, typing.Set[str]] = attr.ib(factory=OrderedDict)
    _deps_sort_need_build_flag: bool = attr.ib(default=True)
    _deps_sort_cache: typing.Dict[str, int] = attr.ib(factory=OrderedDict)

    @property
    def n_parameter(self):
        """
        Return number of Parameters declared.
        """
        return len(self.Parameters)

    @property
    def n_resource(self):
        """
        Return number of Resources declared.
        """
        return len(self.Resources)

    @property
    def n_output(self):
        """
        Return number of Outputs declared.
        """
        return len(self.Outputs)

    @property
    def n_rule(self):
        """
        Return number of Rules declared.
        """
        return len(self.Rules)

    @property
    def n_mapping(self):
        """
        Return number of Mappings declared.
        """
        return len(self.Mappings)

    @property
    def n_condition(self):
        """
        Return number of Conditions declared.
        """
        return len(self.Conditions)

    @property
    def n_transform(self):
        """
        Return number of Transform declared.
        """
        return len(self.Transform)

    @property
    def n_named_object(self):
        """
        Return number of named object declared in this template. For example,
        Parameter, Resource, Output, Rule, Mapping, Condition are named object,
        because they have a logic id.
        """
        return sum([
            self.n_parameter, self.n_resource, self.n_output,
            self.n_rule, self.n_mapping, self.n_condition,
        ])

    # handle the inter dependency relationship among Parameter, Mapping,
    # Condition, Resource, Output
    def _encode_depends_on(
        self,
        obj_list: typing.List[TypeHint.dependency_obj],
    ) -> typing.Set[str]:
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

    def _iterate_addable(
        self,
        include_resource_group: bool = False,
    ) -> typing.List[
        typing.Tuple[str, TypeHint.addable_obj]]:
        """
        Iterate through all addable object (Parameter, Resource, Output, ...).
        """
        l = list()
        for class_type, attr_name in _class_type_to_attr_mapper.items():
            if (class_type == ResourceGroup.CLASS_TYPE):
                if include_resource_group is False:
                    continue

            collection = getattr(self, attr_name)
            for obj in collection.values():
                l.append((obj.gid, obj))
        return l

    def _iterate_addable_keys(
        self,
        include_resource_group: bool = False,
    ) -> typing.List[str]:
        return [gid for gid, _ in self._iterate_addable(include_resource_group)]

    def _build_deps_data(self) -> typing.Tuple[
        typing.Dict[str, typing.Set[str]],
        typing.Dict[str, typing.Set[str]]
    ]:
        deps_on_data = OrderedDict()
        deps_by_data = OrderedDict()
        for gid, _ in self._iterate_addable(include_resource_group=True):
            deps_on_data[gid] = set()
            deps_by_data[gid] = set()

        for gid, obj in self._iterate_addable(include_resource_group=True):
            deps_on_data[gid] = self._encode_depends_on(obj.DependsOn)
            for parent_gid in self._encode_depends_on(obj.DependsOn):
                deps_by_data[parent_gid].add(gid)

        return deps_on_data, deps_by_data

    @property
    def deps_on_data(self) -> typing.Dict[str, typing.Set[str]]:
        """
        Depends on data is a dictionary structure. It shows the dependency
        relationship in this way (child depends on parent)::

            {
                child_id_1: {parent_id_11, parent_id_12, ...},
                child_id_2: {parent_id_21, parent_id_22, ...},
                ...
            }
        """
        if self._deps_data_need_build_flag:
            deps_on_data, deps_by_data = self._build_deps_data()
            self._deps_on_data_cache = deps_on_data
            self._deps_by_data_cache = deps_by_data
            self._deps_data_need_build_flag = False
            self._deps_sort_need_build_flag = True
        return self._deps_on_data_cache

    @property
    def deps_by_data(self) -> typing.Dict[str, typing.Set[str]]:
        """
        Depends on data is a dictionary structure. It shows the dependency
        relationship in this way (child depends on parent)::

            {
                parent_id_1: {child_id_11, child_id_12, ...},
                parent_id_2: {child_id_21, child_id_22, ...},
                ...
            }
        """
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
    def add_one(
        self,
        obj: TypeHint.addable_obj,
        add_or_update: bool = False,
        add_or_ignore: bool = False,
    ) -> bool:
        """
        Add single object to Template. If there is a existing object with
        the same logic id and no flag is passed, exception will be raised.

        :param obj: The object you add to template.
        :param add_or_update: if True, will overwrite other object with
            the same logic id
        :param add_or_ignore: if True, will ignore and pass if there's
            existing object with the same logic id

        :return: a boolean flag indicates that whether change is made.
        """
        # validate argument
        if not isinstance(obj, _Addable):
            raise TypeError(f"You cannot add a {obj.__class__.__name__} object to template")

        if add_or_update and add_or_ignore:
            raise ValueError("Can't do add_or_update=True and add_or_ignore=True")

        obj: TypeHint.addable_obj

        # find values for future use
        collection: typing.Union[
            typing.Dict[str, TypeHint.addable_obj], typing.List[Transform],
        ] = getattr(
            self, _class_type_to_attr_mapper[obj.CLASS_TYPE])

        # add this object
        if obj.id in collection:  # handle logic id conflict
            if add_or_update:
                collection[obj.id] = obj
                self._deps_data_need_build_flag = True
                return True
            elif add_or_ignore:
                return False
            else:  # raise exception
                if isinstance(obj, Resource):
                    type_name = Resource.__name__
                else:
                    type_name = obj.__class__.__name__
                raise AWSObjectLogicIdConflictError(
                    f"{type_name} logic id '{obj.id}' already exists!")
        else:
            collection[obj.id] = obj
            self._deps_data_need_build_flag = True
            return True

    def add(
        self,
        obj: TypeHint.addable_obj,
        _objects_to_update: typing.Dict[str, TypeHint.addable_obj] = None,
    ):
        """
        Add a AWS object to the template. If the obj declared some dependency
        AWS Objects like Parameter, Mapping, Condition, it will also add
        those objects.

        If there's any logic id conflict include the root object or those
        dependency objects, the new object will overwrite the existing one.

        This method is atomic. In other word, either all objects succeed or
        non.
        """
        if _objects_to_update is None:
            is_first_call = True
            _objects_to_update = OrderedDict()
        else:
            is_first_call = False

        _objects_to_update[obj.gid] = obj

        # add dependency objects
        if (obj.DependsOn is not None):
            for dep_obj in obj.DependsOn:
                if isinstance(dep_obj, str):
                    if self.Resources:
                        pass
                    if dep_obj not in self.Resources:
                        raise AWSObjectNotExistsError.make(
                            obj_type=CloudFomation.Resources,
                            logic_id=dep_obj,
                        )
                    dep_obj = self.Resources[dep_obj]
                self.add(dep_obj, _objects_to_update=_objects_to_update)

        if is_first_call:
            # validate type before making the change
            for obj in _objects_to_update.values():
                if not isinstance(obj, _Addable):
                    raise TypeError(f"You cannot add a {obj.__class__.__name__} object to template")

            for obj in _objects_to_update.values():
                self.add_one(obj, add_or_update=True)

    def _get_by_gid(
        self,
        gid: str,
    ) -> TypeHint.addable_obj:
        """
        Get aws object by global id.
        """
        class_type, logic_id = gid.split("--")
        collection = getattr(self, _class_type_to_attr_mapper[class_type])
        return collection[logic_id]

    def remove_one(
        self,
        obj: TypeHint.addable_obj,
        ignore_not_exists: bool = False,
    ) -> bool:
        """
        Remove single object from  Template. If there is no a existing object with
        the same logic id and no flag is passed, exception will be raised.

        :param obj: The object you remove template.
        :param ignore_not_exists: if True, will ignore and pass if there's
            NO existing object with the same logic id

        :return: a boolean flag indicates that whether change is made.
        """
        # validate argument
        if not isinstance(obj, _Addable):
            raise TypeError(f"You cannot remove a {obj.__class__.__name__} object from template")

        obj: TypeHint.addable_obj
        collection = getattr(self, _class_type_to_attr_mapper[obj.CLASS_TYPE])

        # remove object
        if obj.id in collection:
            collection.pop(obj.id)
            self._deps_data_need_build_flag = True
            return True
        elif ignore_not_exists:
            return False
        else:
            raise AWSObjectNotExistsError.make(
                obj_type=obj.CLASS_TYPE, logic_id=obj.id)

    def remove(
        self,
        obj: TypeHint.addable_obj,
        _deps_by_data: OrderedDict = None,
        _objects_to_remove: typing.Dict[str, TypeHint.addable_obj] = None,
    ):
        """
        Remove a AWS object from the template. If there are other objects depend
        on this object, it will also remove other objects.

        This method is atomic. In other word, either all objects succeed or
        non.
        """
        if _objects_to_remove is None:
            is_first_call = True
            _objects_to_remove = OrderedDict()
        else:
            is_first_call = False

        if _deps_by_data is None:
            _deps_by_data = self.deps_by_data

        _objects_to_remove[obj.gid] = obj

        # handle other object depends on this
        for child_gid in self.deps_by_data.get(obj.gid, set()):
            try:
                child_obj = self._get_by_gid(child_gid)
                self.remove(
                    child_obj,
                    _deps_by_data=_deps_by_data,
                    _objects_to_remove=_objects_to_remove,
                )
            except KeyError:
                pass

        # if it is resource group, aws objects in the DependsOn list should
        # also be removed
        if isinstance(obj, ResourceGroup):
            for child_obj in obj.DependsOn:
                if (not isinstance(child_obj, ResourceGroup)) and (child_obj.gid not in _objects_to_remove):
                    self.remove(
                        child_obj,
                        _deps_by_data=_deps_by_data,
                        _objects_to_remove=_objects_to_remove,
                    )

        if is_first_call:
            # validate type before making the change
            for obj in _objects_to_remove.values():
                if not isinstance(obj, _Addable):
                    raise TypeError(f"You cannot remove a {obj.__class__.__name__} object to template")

            for obj in _objects_to_remove.values():
                self.remove_one(obj, ignore_not_exists=True)

    # --- parameter handling
    def get_param_values(self) -> typing.Dict[str, typing.Any]:
        return OrderedDict([
            (p.id, p.get_value())
            for p in self.Parameters.values()
        ])

    # --- nested stack
    def add_nested_stack(
        self,
        stack: typing.Union[str, Stack],
        template: 'Template',
    ) -> bool:
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
        """
        Serialize the template, convert it to python dict.
        """
        self.__pre_serialize__()

        dct = get_key_value_dict(self)
        dct.pop("NestedStack")
        dct.pop("Groups")
        dct.pop("_deps_data_need_build_flag")
        dct.pop("_deps_on_data_cache")
        dct.pop("_deps_by_data_cache")
        dct.pop("_deps_sort_need_build_flag")
        dct.pop("_deps_sort_cache")
        dct = remove_id_and_empty(dct)
        dct = serialize(dct)
        return dct

    def to_json(
        self,
        human_readable: bool = True,
    ) -> str:
        """
        Convert template to json string.
        """
        if human_readable:
            indent = 4
        else:  # pragma: no cover
            indent = None
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def to_json_file(
        self,
        path: str,
    ):  # pragma: no cover
        """
        Dump template to json file.
        """
        with open(path, "w") as f:
            f.write(self.to_json())

    def to_yml(self) -> str:  # pragma: no cover
        """
        Convert template to yaml string
        """
        return cfn_flip.to_yaml(
            self.to_json(human_readable=True),
            clean_up=False,
            long_form=False
        )

    def to_yml_file(
        self,
        path: str,
    ):  # pragma: no cover
        """
        Dump template to yaml file.
        """
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

    def batch_tagging(
        self,
        overwrite: bool = False,
        **kwargs
    ):
        """
        Batch tag all resources if supporting Tags.
        """
        for r in self.Resources.values():
            if r.support_tags():
                r.update_tags(overwrite, **kwargs)

    # factory method
    @classmethod
    def from_many_objects(
        cls,
        objects: typing.Iterable[TypeHint.addable_obj],
    ) -> 'Template':
        """
        A factory method can create a Template object from many AWS Objects.
        """
        tpl = cls()
        for obj in objects:
            tpl.add(obj)
        return tpl
