# -*- coding: utf-8 -*-


import json
import attr
import jinja2
import typing
import requests
from pprint import pprint
from pathlib_mate import PathCls as Path
from collections import OrderedDict

_ = pprint

here = Path(__file__).parent

# --- Spec file data handling
spec_file = here.parent.parent.append_parts("cft-spec.json")


def download_spec_file():
    """
    The spec file can be found in
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html
    """
    if not spec_file.exists():
        url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
        spec_file.write_text(requests.get(url).text, encoding="utf-8")


def remove_spec_file():
    if spec_file.exists():
        spec_file.remove()


def read_spec_file() -> dict:
    return json.loads(spec_file.read_text(encoding="utf-8"))


def _get_sort_key(obj: typing.Union['Property', 'ResourceProperty']) -> str:
    """
    Sometime we need to write attribute declaration code in an order. We always]
    declare required property first, then optional required.

    This function returns a sort key for ordering purpose.
    """
    if obj.Name == "Tags":
        return "z"

    if obj.Required:  # required property first
        return f"a-{obj.Name}"
    else:
        return f"b-{obj.Name}"


def _get_attr_name(obj: typing.Union['Property', 'ResourceProperty']):
    """
    Serve as the attribute name in class declaration using attrs library.

    For example::

        @attr.b
        class User:
            # {{ attr_name }}: str
            name: str
    """
    if obj.Required:
        return "rp_{}".format(obj.Name.replace(".", ""))
    else:
        return "p_{}".format(obj.Name.replace(".", ""))


LIST_TYPE = "List"
MAP_TYPE = "Map"
TAG_TYPE = "Tag"
STR_TYPE = "String"

PRIMITIVE_TYPE_DICT = {
    "Integer": "int",
    "Long": "int",
    "Double": "float",
    "String": "str",
    "Boolean": "bool",
    "Json": "dict",
    "Timestamp": "str",
}


def _find_type_hint_and_validator(prop: typing.Union['Property', 'ResourceProperty'],
                                  prop_type_class_name: str,
                                  cycled_class_name_set: typing.Set[str]) -> typing.Tuple[
    str, typing.Union[str, None], typing.Union[str, None]]:
    """
    We need to define type hint and validators for attrs.

    Those syntax is generally based on the type, primitive_type, item_type,
    primitive_item_type of the property. This method implements the logic to
    generate type hint and validator python code.

    **I know the logic is complicate, and there's a lots of edge case need to be
    handled properly. This is the best I can do now**.
    """
    # --- Debug ---
    # if prop_type_class_name == "InstanceGroupConfigConfiguration":
    # if prop_type_class_name == "InstanceGroupConfigConfiguration" and prop.Name == "Configuration":
    # if prop.ResourceName == "WebACL" and prop.Name == "ScopeDownStatement":
    #     print(prop.Type, prop.PrimitiveType, prop.ItemType, prop.PrimitiveItemType)

    # -------------
    need_validator = True
    if (prop.Type == LIST_TYPE) and (prop.ItemType == TAG_TYPE):
        type_hint = f"typing.List[typing.Union[{TAG_TYPE}, dict]]"
        validator = f"attr.validators.deep_iterable(member_validator=attr.validators.instance_of({TAG_TYPE}), iterable_validator=attr.validators.instance_of(list))"
        converter = f"{TAG_TYPE}.from_list"

    elif (prop.Type == LIST_TYPE) and bool(prop.ItemType):
        parent_class_name = prop.ResourceName + prop.ItemType
        type_hint = "typing.List[typing.Union['{}', dict]]".format("Prop" + parent_class_name)
        if (parent_class_name == prop_type_class_name) or (
            parent_class_name in cycled_class_name_set):  # self depends on self or cycle depends
            validator = "attr.validators.instance_of(list)"
            converter = None
        else:
            validator = "attr.validators.deep_iterable(member_validator=attr.validators.instance_of({}), iterable_validator=attr.validators.instance_of(list))".format(
                "Prop" + parent_class_name)
            converter = "{}.from_list".format("Prop" + parent_class_name)

    elif (prop.Type == LIST_TYPE) and bool(prop.PrimitiveItemType) and (prop.PrimitiveItemType == STR_TYPE):
        type_hint = "typing.List[TypeHint.intrinsic_str]"
        validator = "attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))"
        converter = None

    elif (prop.Type == LIST_TYPE) and bool(prop.PrimitiveItemType):
        type_hint = "typing.List[{}]".format(PRIMITIVE_TYPE_DICT[prop.PrimitiveItemType])
        validator = "attr.validators.deep_iterable(member_validator=attr.validators.instance_of({}), iterable_validator=attr.validators.instance_of(list))".format(
            PRIMITIVE_TYPE_DICT[prop.PrimitiveItemType])
        converter = None

    elif (prop.Type == MAP_TYPE) and bool(prop.ItemType):
        parent_class_name = prop.ResourceName + prop.ItemType
        type_hint = "typing.Union['{}', dict]".format("Prop" + parent_class_name)
        if (parent_class_name == prop_type_class_name) or (
            parent_class_name in cycled_class_name_set):  # self depends on self or cycle depends
            validator = None
            need_validator = False
            converter = None
        else:
            validator = "attr.validators.instance_of({})".format("Prop" + parent_class_name)
            converter = "{}.from_list".format("Prop" + parent_class_name)

    elif (prop.Type == MAP_TYPE) and bool(prop.PrimitiveItemType) and (prop.PrimitiveItemType == STR_TYPE):
        type_hint = "typing.Dict[str, TypeHint.intrinsic_str]"
        validator = "attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))"
        converter = None

    elif (prop.Type == MAP_TYPE) and bool(prop.PrimitiveItemType):
        type_hint = "typing.Dict[str, {}]".format(PRIMITIVE_TYPE_DICT[prop.PrimitiveItemType])
        validator = "attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of({}))".format(
            PRIMITIVE_TYPE_DICT[prop.PrimitiveItemType]
        )
        converter = None

    elif bool(prop.Type):
        parent_class_name = prop.ResourceName + prop.Type
        type_hint = "typing.Union['{}', dict]".format("Prop" + parent_class_name)
        if (parent_class_name == prop_type_class_name) or (
            parent_class_name in cycled_class_name_set):  # self depends on self or cycle depends
            validator = None
            need_validator = False
            converter = None
        else:
            validator = "attr.validators.instance_of({})".format("Prop" + parent_class_name)
            converter = "{}.from_dict".format("Prop" + parent_class_name)

    elif bool(prop.PrimitiveType) and (prop.PrimitiveType == STR_TYPE):
        type_hint = "TypeHint.intrinsic_str"
        validator = "attr.validators.instance_of(TypeCheck.intrinsic_str_type)"
        converter = None

    elif bool(prop.PrimitiveType):
        type_hint = PRIMITIVE_TYPE_DICT[prop.PrimitiveType]
        validator = "attr.validators.instance_of({})".format(PRIMITIVE_TYPE_DICT[prop.PrimitiveType])
        converter = None

    else:
        raise ValueError

    if need_validator and (not bool(prop.Required)):
        validator = f"attr.validators.optional({validator})"

    return type_hint, validator, converter


def _get_type_hint(prop: typing.Union['Property', 'ResourceProperty'],
                   prop_type_class_name: str,
                   cycled_class_name_set: typing.Set[str]) -> str:
    """
    For example::

        @attr.b
        class User:
            # name: {{ type_hint }}
            name: str
    """
    return _find_type_hint_and_validator(prop, prop_type_class_name, cycled_class_name_set)[0]


def _get_vali_def(prop: typing.Union['Property', 'ResourceProperty'],
                  prop_type_class_name: str,
                  cycled_class_name_set: typing.Set[str]) -> str:
    """
    For example::

        @attr.b
        class User:
            # name: str = attr.ib(validators={{ vali_def }})
            name: str = attr.ib(validators=attr.validators.instance_of(str))
    """
    return _find_type_hint_and_validator(prop, prop_type_class_name, cycled_class_name_set)[1]


def _get_converter(prop: typing.Union['Property', 'ResourceProperty'],
                   prop_type_class_name: str,
                   cycled_class_name_set: typing.Set[str]) -> typing.Union[str, None]:
    """
    For example::

        @attr.b
        class User:
            # name: str = attr.ib(validators={{ vali_def }})
            name: str = attr.ib(validators=attr.validators.instance_of(str))
    """
    return _find_type_hint_and_validator(prop, prop_type_class_name, cycled_class_name_set)[2]


def _make_template(filename):
    return jinja2.Template(
        Path(here, "templates", filename).read_text(encoding="utf-8")
    )


resource_def_template = _make_template("resource.py")
property_def_template = _make_template("property.py")
service_def_template = _make_template("service.py")
init_template = _make_template("init.py")
import_template = _make_template("_imp.py")


@attr.s
class Property:
    Name: str = attr.field(default=None)
    SystemName: str = attr.field(default=None)
    ServiceName: str = attr.field(default=None)
    ResourceName: str = attr.field(default=None)
    PropertyName: str = attr.field(default=None)
    PropertyFullName: str = attr.field(default=None)

    Required: bool = attr.field(default=None)
    Type: str = attr.field(default=None)
    PrimitiveType: str = attr.field(default=None)
    ItemType: str = attr.field(default=None)
    PrimitiveItemType: str = attr.field(default=None)
    Documentation: str = attr.field(default=None)
    UpdateType: str = attr.field(default=None)
    DuplicatesAllowed: str = attr.field(default=None)

    PropertyTypeClassName: str = attr.field(default=None)
    CycledClassNameSet: typing.Set[str] = attr.field(default=None)

    @property
    def sort_key(self):
        return _get_sort_key(self)

    @property
    def attr_name(self):
        return _get_attr_name(self)

    @property
    def class_name(self):
        return self.PropertyFullName.replace(".", "")

    @property
    def type_hint(self):
        return _get_type_hint(self, self.PropertyTypeClassName, self.CycledClassNameSet)

    @property
    def vali_def(self):
        return _get_vali_def(self, self.PropertyTypeClassName, self.CycledClassNameSet)

    @property
    def converter(self):
        return _get_converter(self, self.PropertyTypeClassName, self.CycledClassNameSet)


@attr.s
class PropertyType:
    Name: str = attr.field(default=None)
    SystemName: str = attr.field(default=None)
    ServiceName: str = attr.field(default=None)
    ResourceName: str = attr.field(default=None)
    PropertyName: str = attr.field(default=None)
    PropertyFullName: str = attr.field(default=None)
    Required: bool = attr.field(default=None)
    Type: str = attr.field(default=None)
    PrimitiveType: str = attr.field(default=None)
    ItemType: str = attr.field(default=None)
    PrimitiveItemType: str = attr.field(default=None)
    Documentation: str = attr.field(default=None)
    UpdateType: str = attr.field(default=None)

    Properties: typing.List[Property] = attr.field(default=None)

    @property
    def class_name(self):
        return "Prop" + self.PropertyFullName.replace(".", "")

    def render(self):
        return property_def_template.render(prop_type=self)

    def find_property(self, name):
        for property in self.Properties:
            if property.Name == name:
                return property
        raise ValueError


@attr.s
class ResourceProperty:
    Name: str = attr.field(default=None)
    SystemName: str = attr.field(default=None)
    ServiceName: str = attr.field(default=None)
    ResourceName: str = attr.field(default=None)
    PropertyName: str = attr.field(default=None)
    PropertyFullName: str = attr.field(default=None)
    Required: bool = attr.field(default=None)
    Type: str = attr.field(default=None)
    PrimitiveType: str = attr.field(default=None)
    ItemType: str = attr.field(default=None)
    PrimitiveItemType: str = attr.field(default=None)
    Documentation: str = attr.field(default=None)
    UpdateType: str = attr.field(default=None)
    DuplicatesAllowed: str = attr.field(default=None)

    @property
    def sort_key(self):
        return _get_sort_key(self)

    @property
    def attr_name(self):
        return _get_attr_name(self)

    @property
    def type_hint(self):
        return _get_type_hint(self, "NEVER_HAPPEN", set())

    @property
    def vali_def(self):
        return _get_vali_def(self, "NEVER_HAPPEN", set())

    @property
    def converter(self):
        return _get_converter(self, "NEVER_HAPPEN", set())


@attr.s
class ResourceAttribute:
    Name: str = attr.ib(default=None)
    SystemName: str = attr.field(default=None)
    ServiceName: str = attr.field(default=None)
    ResourceName: str = attr.field(default=None)
    AttributeName: str = attr.field(default=None)
    Type: str = attr.field(default=None)
    PrimitiveType: str = attr.field(default=None)
    ItemType: str = attr.field(default=None)
    PrimitiveItemType: str = attr.field(default=None)
    Documentation: str = attr.field(default=None)
    DuplicatesAllowed: str = attr.field(default=None)

    @property
    def method_name(self):
        return "rv_{}".format(self.Name.replace(".", ""))


@attr.s
class ResourceType:
    """
    """
    Name: str = attr.field(default=None)
    SystemName: str = attr.field(default=None)
    ServiceName: str = attr.field(default=None)
    ResourceName: str = attr.field(default=None)
    Documentation: str = attr.field(default=None)
    Properties: typing.List[ResourceProperty] = attr.field(default=None)
    Attributes: typing.List[ResourceAttribute] = attr.field(default=None)
    AdditionalProperties: bool = attr.field(default=None)

    @property
    def class_name(self):
        return self.ResourceName

    def render(self):
        return resource_def_template.render(res_type=self)


@attr.s
class CftSpec:
    PropertyTypes: typing.List[PropertyType] = attr.field(default=None)
    ResourceTypes: typing.List[ResourceType] = attr.field(default=None)

    @classmethod
    def new(cls) -> 'CftSpec':
        download_spec_file()
        spec_data = read_spec_file()

        # --- PropertyTypes section ---
        property_type_list: typing.List[PropertyType] = list()
        for property_type_name, property_type_dct in spec_data["PropertyTypes"].items():
            # print(f"=== {property_type_name} ===")
            if property_type_name == "Tag":
                continue
            SystemName, ServiceName, PropertyFullName = property_type_name.split("::")
            ResourceName, PropertyName = PropertyFullName.split(".")
            property_properties = list()
            for property_name, property_dct in property_type_dct.get("Properties", {}).items():
                # print(f"--- {property_name} ---")
                property_dct["Name"] = property_name
                property_dct["SystemName"] = SystemName
                property_dct["ServiceName"] = ServiceName
                property_dct["ResourceName"] = ResourceName
                property_dct["PropertyName"] = property_name
                property_dct["PropertyFullName"] = ResourceName + "." + property_name
                property_dct["PropertyTypeClassName"] = ResourceName + PropertyName
                property = Property(**property_dct)
                property_properties.append(property)

                # --- Debug ---
                # if property_type_name == "AWS::EMR::InstanceGroupConfig.Configuration" and property_name == "Configurations":
                #     print(property_dct["PropertyTypeClassName"])
                # -------------

            property_properties = list(
                sorted(
                    property_properties,
                    key=lambda pp: pp.sort_key
                )
            )

            property_type_dct["Name"] = property_type_name
            property_type_dct["SystemName"] = SystemName
            property_type_dct["ServiceName"] = ServiceName
            property_type_dct["ResourceName"] = ResourceName
            property_type_dct["PropertyName"] = PropertyName
            property_type_dct["PropertyFullName"] = PropertyFullName
            property_type_dct["Properties"] = property_properties
            property_type = PropertyType(**property_type_dct)

            property_type_list.append(property_type)

        # --- ResourceTypes section ---
        resource_type_list: typing.List[ResourceType] = list()
        for resource_type_name, resource_type_dct in spec_data["ResourceTypes"].items():
            # print(f"=== {resource_type_name} ===")
            SystemName, ServiceName, ResourceName = resource_type_name.split("::")
            resource_properties = list()
            for resource_property_name, resource_property_dct in resource_type_dct.get("Properties", {}).items():
                # print(f"--- {resource_property_name} ---")
                resource_property_dct["Name"] = resource_property_name
                resource_property_dct["SystemName"] = SystemName
                resource_property_dct["ServiceName"] = ServiceName
                resource_property_dct["ResourceName"] = ResourceName
                resource_property_dct["PropertyName"] = resource_property_name
                resource_property_dct["PropertyFullName"] = ResourceName + "." + resource_property_name
                resource_property = ResourceProperty(**resource_property_dct)
                resource_properties.append(resource_property)

                # sometime, both Type and PrimitiveType exists, in this case
                # Type = a special one and PrimitiveType = json
                # in other word, our type hint should rely on Type over PrimitiveType
                # if (bool(resource_property.Type) + bool(resource_property.PrimitiveType)) != 1:
                # print(resource_type_name, resource_property_name, resource_property.Type,
                #       resource_property.PrimitiveType)

            resource_attributes = list()
            for resource_attribute_name, resource_attribute_dct in resource_type_dct.get("Attributes", {}).items():
                # print(f"--- {resource_attribute_name} ---")
                resource_doc_url = resource_type_dct["Documentation"]
                resource_attribute_doc_url = resource_doc_url + "#" + resource_doc_url.split("/")[-1].split(".")[
                    0] + "-return-values"

                resource_attribute_dct["Name"] = resource_attribute_name
                resource_attribute_dct["SystemName"] = SystemName
                resource_attribute_dct["ServiceName"] = ServiceName
                resource_attribute_dct["ResourceName"] = ResourceName
                resource_attribute_dct["AttributeName"] = resource_attribute_name
                resource_attribute_dct["Documentation"] = resource_attribute_doc_url
                resource_attribute = ResourceAttribute(**resource_attribute_dct)
                resource_attributes.append(resource_attribute)

            resource_properties = list(
                sorted(
                    resource_properties,
                    key=lambda rp: rp.sort_key
                )
            )

            resource_type_dct["Name"] = resource_type_name
            resource_type_dct["SystemName"] = SystemName
            resource_type_dct["ServiceName"] = ServiceName
            resource_type_dct["ResourceName"] = ResourceName
            resource_type_dct["Properties"] = resource_properties
            resource_type_dct["Attributes"] = resource_attributes
            resource_type_list.append(ResourceType(**resource_type_dct))

        return cls(
            PropertyTypes=property_type_list,
            ResourceTypes=resource_type_list,
        )

    def find_property_type(self, name) -> PropertyType:
        for pt in self.PropertyTypes:
            if pt.Name == name:
                return pt
        raise ValueError

    def find_resource_type(self, name) -> ResourceType:
        for rt in self.ResourceTypes:
            if rt.Name == name:
                return rt
        raise ValueError


@attr.s
class Service:
    """
    Represent a ``cottonformation/res/{service_name}.py`` file.

    It renders all property and resource python code.
    """
    name: str = attr.field(default=None)
    properties: typing.List[PropertyType] = attr.field(default=None)
    resources: typing.List[ResourceType] = attr.field(default=None)

    def render(self):
        return service_def_template.render(service=self)


def _standardize_service_name(service_name):
    mapper = {
        "Lambda": "AwsLambda",
    }
    return mapper.get(service_name, service_name)


def order_by_dependencies(dependency_mapper: typing.Dict[str, typing.Set[str]]) \
    -> typing.Tuple[typing.List[str], typing.List[str]]:
    """
    You have to make sure there's no cycle dependency.
    """
    ordered_dict = OrderedDict()
    for _ in range(1000):
        # if there's no child's len(parent_set) == 0, there's no change
        # so we can stop now
        can_we_stop = True
        for child, parent_set in list(dependency_mapper.items()):
            if len(parent_set) == 0:
                ordered_dict[child] = 1
                for parent_set in dependency_mapper.values():
                    if child in parent_set:
                        parent_set.remove(child)
            else:
                can_we_stop = False

        if can_we_stop:
            break

    # if there's cycled dependency, they will be put at the end of the list
    # and we collect this information for future use
    cycled_keys = list()
    for child in dependency_mapper:
        if child not in ordered_dict:
            ordered_dict[child] = 1
            cycled_keys.append(child)

    ordered_keys = list(ordered_dict)
    return ordered_keys, cycled_keys


def group_by_service(cft_spec: CftSpec) -> typing.List[Service]:
    """
    Convert the cft_spec object to list of service object. So we can use it
    to create tons of python script.
    """

    # 1. group PropertyType and ResourceType by service
    service_dict: typing.Dict[str, Service] = dict()
    for p in cft_spec.PropertyTypes:
        if p.ServiceName:
            service_name = _standardize_service_name(p.ServiceName)
            try:
                service_dict[service_name].properties.append(p)
            except:
                service_dict[service_name] = Service(
                    name=service_name,
                    properties=[p, ],
                    resources=[],
                )

    for r in cft_spec.ResourceTypes:
        if r.ServiceName:
            service_name = _standardize_service_name(r.ServiceName)
            try:
                service_dict[service_name].resources.append(r)
            except:
                service_dict[service_name] = Service(
                    name=service_name,
                    properties=[],
                    resources=[r, ],
                )

    # 2. re order property_type by dependencies
    for service_name, service in service_dict.items():
        # print(f"==={service_name}===")
        property_type_key_view: typing.Dict[str, PropertyType] = {
            property_type.Name: property_type
            for property_type in service.properties
        }

        # build dependency mapper
        dependency_mapper: typing.Dict[str, typing.Set[str]] = dict()
        for pt in service.properties:
            child_key = pt.Name
            dependency_mapper[child_key] = set()
            for p in pt.Properties:
                if p.Type == "List" and bool(p.ItemType):
                    if p.ItemType == "Tag":
                        continue
                    parent_key = "{}::{}::{}.{}".format(
                        pt.SystemName,
                        pt.ServiceName,
                        pt.ResourceName,
                        p.ItemType
                    )
                    if child_key != parent_key:
                        dependency_mapper[child_key].add(parent_key)
                elif p.Type == "List" and bool(p.PrimitiveItemType):
                    pass
                elif p.Type == "Map" and bool(p.ItemType):
                    parent_key = "{}::{}::{}.{}".format(
                        pt.SystemName,
                        pt.ServiceName,
                        pt.ResourceName,
                        p.ItemType
                    )
                    if child_key != parent_key:
                        dependency_mapper[child_key].add(parent_key)
                elif p.Type == "Map" and bool(p.PrimitiveItemType):
                    pass
                elif bool(p.Type):
                    parent_key = "{}::{}::{}.{}".format(
                        pt.SystemName,
                        pt.ServiceName,
                        pt.ResourceName,
                        p.Type,
                    )
                    if child_key != parent_key:
                        dependency_mapper[child_key].add(parent_key)
                else:
                    pass

        property_type_key_list, cycled_key_list = order_by_dependencies(dependency_mapper)
        cycled_class_name_set = {
            key.split("::")[2].replace(".", "")
            for key in cycled_key_list
        }

        # --- Debug ----
        # if service_name == "WAFv2":
        #     print("AWS::WAFv2::RuleGroup.Rule" in dependency_mapper)
        #     print("AWS::WAFv2::RuleGroup.Rule" in property_type_key_list)
        #     pprint(dependency_mapper)
        # --------------

        new_properties = list()
        for property_type_key in property_type_key_list:
            property_type = property_type_key_view[property_type_key]
            for property in property_type.Properties:
                property.CycledClassNameSet = cycled_class_name_set
            new_properties.append(property_type)
        service.properties = new_properties

    # --- Debug code ---
    # print("--- property type ---")
    # for p in service_dict["XRay"].properties:
    #     print(p)
    # print("--- resource type ---")
    # for r in service_dict["XRay"].resources:
    #     print(r)
    # ------------------

    return list(service_dict.values())


res_dir = here.change(new_basename="res")


def remove_all_file():
    """
    remove all file in cottonformation/res dir
    """
    for p in res_dir.select_file():
        p.remove()


def gen_code(dry_run=True):
    """

    :param dry_run:
    :return:
    """
    cft_spec = CftSpec.new()
    service_list = group_by_service(cft_spec)

    for service in service_list:
        # --- Debug ---
        # if service.name != "S3":
        #     continue
        # -------------
        filename = "{}.py".format(service.name.lower())
        p = Path(res_dir, filename)
        content = service.render()
        if dry_run is False:
            p.write_text(content, encoding="utf-8")

    p = Path(res_dir, "_imp.py")
    content = import_template.render(
        service_list=[
            service.name.lower()
            for service in service_list
        ]
    )
    p.write_text(content, encoding="utf-8")

    p = Path(res_dir, "__init__.py")
    content = init_template.render()
    p.write_text(content, encoding="utf-8")
