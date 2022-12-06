# -*- coding: utf-8 -*-

"""
PropertyTypes:

- Special:
    - PropertyTypes.Properties.Type:
        - List
        - Tags
    - PropertyTypes.Properties.ItemType:
        - Tag
        - Tags

ResourceTypes:
"""

from cottonformation.code.spec_file.downloader import download_spec_file, read_spec_file
from cottonformation.code.spec_file.inspect import (
    see_top_level_fields,
    see_property_types,
    see_resource_types,
    see_resource_tags,
    see_property_prop_type_is_self,
)
# download_spec_file(skip_if_exists=True)

# --- inspec spec file
spec_file_data = read_spec_file()

# see_top_level_fields(spec_file_data)
# see_property_types(spec_file_data)
# see_resource_types(spec_file_data)
# see_resource_tags(spec_file_data)
see_property_prop_type_is_self(spec_file_data)