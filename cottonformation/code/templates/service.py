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
{% for p in service.properties %}
{{ p.render() }}
{% endfor %}

#--- Resource declaration ---
{% for r in service.resources %}
{{ r.render() }}
{% endfor %}
