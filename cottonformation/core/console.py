# -*- coding: utf-8 -*-

"""
AWS Console Url related function.
"""

import typing as T


def split_s3_uri(
    s3_uri: str,
) -> T.Tuple[str, str]:  # pragma: no cover
    """
    Split AWS S3 URI, returns bucket and key.

    :param s3_uri: example, ``"s3://my-bucket/my-folder/data.json"``
    """
    parts = s3_uri.split("/")
    bucket = parts[2]
    key = "/".join(parts[3:])
    return bucket, key


def get_s3_console_url(
    bucket: T.Optional[str] = None,
    prefix: T.Optional[str] = None,
    s3_uri: T.Optional[str] = None,
    is_us_gov_cloud: bool = False,
) -> str:  # pragma: no cover
    """
    Return an AWS Console url that you can use to open it in your browser.

    :param bucket: example, ``"my-bucket"``
    :param prefix: example, ``"my-folder/"``
    :param s3_uri: example, ``"s3://my-bucket/my-folder/data.json"``
    :param is_us_gov_cloud: whether it is a gov cloud

    Example::
        >>> get_s3_console_url(s3_uri="s3://my-bucket/my-folder/data.json")
        https://s3.console.aws.amazon.com/s3/object/my-bucket?prefix=my-folder/data.json
    """
    if s3_uri is None:
        if not ((bucket is not None) and (prefix is not None)):
            raise ValueError
    else:
        if not ((bucket is None) and (prefix is None)):
            raise ValueError
        bucket, prefix = split_s3_uri(s3_uri)

    if len(prefix) == 0:
        return "https://console.aws.amazon.com/s3/buckets/{}?tab=objects".format(
            bucket,
        )
    elif prefix.endswith("/"):
        s3_type = "buckets"
    else:
        s3_type = "object"

    if is_us_gov_cloud:
        endpoint = "console.amazonaws-us-gov.com"
    else:
        endpoint = "console.aws.amazon.com"

    return "https://{endpoint}/s3/{s3_type}/{bucket}?prefix={prefix}".format(
        endpoint=endpoint, s3_type=s3_type, bucket=bucket, prefix=prefix
    )
