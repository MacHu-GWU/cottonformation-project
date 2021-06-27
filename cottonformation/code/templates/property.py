@attr.s
class {{ prop_type.class_name }}(Property):
    """
    AWS Object Type = "{{ prop_type.Name }}"

    Resource Document: {{ prop_type.Documentation }}

    Property Document:
    {% for prop_prop in prop_type.Properties %}
    - ``{{ prop_prop.attr_name }}``: {{ prop_prop.Documentation }}
    {%- endfor %}
    """
    AWS_OBJECT_TYPE = "{{ prop_type.Name }}"
    {% for prop_prop in prop_type.Properties %}
    {{ prop_prop.attr_name }}: {{ prop_prop.type_hint }} = attr.ib(
        default=None,
        {%- if prop_prop.converter %}
        converter={{ prop_prop.converter }},
        {%- endif %}
        validator={{ prop_prop.vali_def }},
        metadata={AttrMeta.PROPERTY_NAME: "{{ prop_prop.Name }}"},
    )
    """Doc: {{ prop_prop.Documentation }}"""
    {%- endfor %}