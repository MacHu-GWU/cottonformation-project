# -*- coding: utf-8 -*-

import pytest
from cottonformation.core.regex import ServiceEnum


class TestServiceEnum:
    def test(self):
        assert ServiceEnum.is_aws_account_id("111122223333") is True
        assert ServiceEnum.is_aws_account_id("1111-2222-3333") is False
        assert ServiceEnum.is_aws_account_id("123") is False

        assert ServiceEnum.is_aws_service_domain("s3.amazonaws.com") is True
        assert ServiceEnum.is_aws_service_domain("ecr-public.amazonaws.com") is True
        assert ServiceEnum.is_aws_service_domain("ec2.amazon.com") is False

        assert ServiceEnum.is_s3_uri("s3://bucket") is True
        assert ServiceEnum.is_s3_uri("s3://my-bucket") is True
        assert ServiceEnum.is_s3_uri("s3://my.bucket") is True
        assert ServiceEnum.is_s3_uri("s3://my_bucket") is False

        assert ServiceEnum.is_s3_uri("s3://bucket/file.txt") is True
        assert ServiceEnum.is_s3_uri("s3://bucket/my file.txt") is True


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
