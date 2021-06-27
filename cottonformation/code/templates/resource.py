@attr.s
class {{ res_type.ResourceName }}(Resource):
    """
    AWS Object Type = "{{ res_type.Name }}"

    Resource Document: {{ res_type.Documentation }}

    Property Document:
    {% for res_prop in res_type.Properties %}
    - ``{{ res_prop.attr_name }}``: {{ res_prop.Documentation }}
    {%- endfor %}
    """
    AWS_OBJECT_TYPE = "{{ res_type.Name }}"

    {% for res_prop in res_type.Properties %}
    {{ res_prop.attr_name }}: {{ res_prop.type_hint }} = attr.ib(
        default=None,
        {%- if res_prop.converter %}
        converter={{ res_prop.converter }},
        {%- endif %}
        validator={{ res_prop.vali_def }},
        metadata={AttrMeta.PROPERTY_NAME: "{{ res_prop.Name }}"},
    )
    """Doc: {{ res_prop.Documentation }}"""
    {%- endfor %}

    {% for res_attr in res_type.Attributes %}
    @property
    def {{ res_attr.method_name }}(self) -> GetAtt:
        """Doc: {{ res_attr.Documentation }}"""
        return GetAtt(resource=self, attr_name="{{ res_attr.Name }}")
    {% endfor %}