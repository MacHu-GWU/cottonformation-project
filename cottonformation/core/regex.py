# -*- coding: utf-8 -*-

import re
import enum

_p_aws_account_id = re.compile("\d{12,12}")
_p_aws_service_domain = re.compile("[a-z0-9\-]{2,12}\.amazonaws\.com")
_p_s3_uri = re.compile("s3://[a-zA-Z0-9-.]{3,63}[\d\D]*")


class ServiceEnum(enum.Enum):
    """
    .. versionadded:: verion

        0.0.6
    """
    aws_account_id = "aws_account_id"
    aws_service_domain = "aws_service_domain"
    aws_service_endpoint = "aws_service_endpoint"
    arn = "arn"
    iam_arn = "iam_arn"
    s3_arn = "s3_arn"
    s3_uri = "s3_uri"

    @classmethod
    def detect(cls, s: str) -> 'ServiceEnum': # pragma: no cover
        raise NotImplementedError

    @classmethod
    def is_aws_account_id(cls, s: str) -> bool:
        return re.fullmatch(_p_aws_account_id, s) is not None

    @classmethod
    def is_aws_service_domain(cls, s: str) -> bool:
        return re.fullmatch(_p_aws_service_domain, s) is not None

    @classmethod
    def is_s3_uri(cls, s: str) -> bool:
        return re.fullmatch(_p_s3_uri, s) is not None
