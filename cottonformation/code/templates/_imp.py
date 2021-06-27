# -*- coding: utf-8 -*-

from . import (
{%- for service_name in service_list %}
    {{ service_name }},
{%- endfor %}
)

