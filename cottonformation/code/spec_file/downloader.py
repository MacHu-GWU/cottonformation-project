# -*- coding: utf-8 -*-

import json
import requests
from .paths import path_cft_spec_json


def download_spec_file(skip_if_exists: bool = True):
    """
    The spec file download link can be found at
    https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

    By default, it overwrite the file
    """
    if path_cft_spec_json.exists():
        if skip_if_exists:
            return
    url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
    path_cft_spec_json.write_text(requests.get(url).text, encoding="utf-8")


def read_spec_file() -> dict:
    """
    Read data of the spec file.
    """
    return json.loads(path_cft_spec_json.read_text(encoding="utf-8"))
