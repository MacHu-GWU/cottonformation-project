# -*- coding: utf-8 -*-


"""
**List of AWS Managed Policy**

AWS provides a lot of pre-baked, commonly used AWS Managed IAM Policy to use
without writing your delicate IAM Policy. However, looking up the exact
ARN of those policy is very annoying. **this helper allows you to auto complete
the AWS Managed Policy ARN**.

Example:

.. code-block:: python

    import ctf

    ctf.helpers.iam.AwsManagedPolicy.AmazonEC2FullAccess # auto complete here

**List of AWS Service principal**:

IAM role requires to define the **trusted entity**. It is something like this::

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "{service_name}.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

However, it is painful to find the valid value for certain AWS Service.
``cottonformation`` **aim to enum those value so developer can easily use it
supported by auto-complete**.

Example:

.. code-block:: python

    import ctf

    ctf.helpers.iam.AssumeRolePolicyBuilder(
        ctf.helpers.iam.ServicePrincipal.awslambda() # auto complete here
    ).build()

There are three source you can use to get list of AWS Service principal

- A community maintained github gist: https://gist.github.com/shortjared/4c1e3fe52bdfa47522cfe5b41e5d6f22
- The aws cli github repository: https://github.com/aws/aws-cli/tree/develop/awscli/examples
- The botocore data set: https://raw.githubusercontent.com/boto/botocore/develop/botocore/data/endpoints.json

Confirmed by AWS, even AWS engineer doesn't know the full list. There's no such
things Personally I prefer to use the botocore data set because it is maintained by AWS.
"""

import attr
import typing

from ._iam_aws_service_principal import _ServicePrincipalMixin
from ._iam_aws_managed_policy import _AwsManagedPolicy
from ..regex import ServiceEnum


class AwsManagedPolicy(_AwsManagedPolicy):
    """
    Helper class to visit the valid AWS Managed IAM Policy ARN.

    You can view the full list of aws managed policy in the console here
    https://console.aws.amazon.com/iam/home?region=us-east-1#/policies

    or use aws cli ``aws iam list-policies --scope AWS --max-items 1000``
    to find policy name and ARN value in the response
    """


_TAB = " " * 4


def _find_all_service_name_list_from_botocore() -> list:  # pragma: no cover
    import requests
    from bs4 import BeautifulSoup

    service_name_list = list()
    path_prefix = "/boto/botocore/tree/master/botocore/data/"
    url = "https://github.com/boto/botocore/tree/master/botocore/data"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    div = soup.find("div", class_="js-details-container Details")
    for a in div.find_all("a"):
        href = a.attrs["href"]
        if href.startswith(path_prefix):
            service_name = href.replace(path_prefix, "").split("/")[0]
            service_name_list.append(service_name)
    return service_name_list


def _find_all_service_name_list_from_gist() -> typing.List[str]:  # pragma: no cover
    """

    :return:
    """
    import requests

    url = "https://gist.githubusercontent.com/shortjared/4c1e3fe52bdfa47522cfe5b41e5d6f22/raw/01238496b3105299c291e8123ae0b4c2be5addac/list.txt"
    service_name_list = [
        service_principal[:-14]
        for service_principal in requests.get(url).text.strip().split("\n")
    ]
    return service_name_list


def _generate_aws_service_principal_code(service_name_list: typing.List[str]):  # pragma: no cover
    from pathlib_mate import PathCls as Path

    lines = [
        "# -*- coding: utf-8 -*-",
        "",
        "class _ServicePrincipalMixin:",
    ]

    special_case_mapper = {
        "lambda": "awslambda",
        "codedeploy_${AWS::Region}": "codedeploy",
    }

    for service_name in service_name_list:
        attr_name = service_name.replace("-", "_").replace(".", "_")
        attr_name = special_case_mapper.get(attr_name, attr_name)
        lines.append(f"{_TAB}@classmethod")
        lines.append(
            f"{_TAB}def {attr_name}(cls): return cls._build(\"{service_name}.amazonaws.com\") # pragma: no cover")
        lines.append("")

    code = "\n".join(lines)
    Path(__file__).change(new_basename="_iam_aws_service_principal.py").write_text(code)


@attr.s
class _AwsPrincipal:
    def to_dict(self) -> dict:
        raise NotImplementedError


@attr.s
class ServicePrincipal(_AwsPrincipal, _ServicePrincipalMixin):
    """
    Policy document looks like this::

        {
            "Effect": "Allow",
            "Principal": {
                "Service": "{service_name}.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    """
    service_principal: str = attr.ib()

    def to_dict(self) -> dict:
        return {
            "Effect": "Allow",
            "Principal": {
                "Service": self.service_principal
            },
            "Action": "sts:AssumeRole"
        }

    @classmethod
    def _build(cls, service_principal):
        return cls(service_principal)


@attr.s
class AccountPrincipal(_AwsPrincipal):
    """
    Policy document looks like this::

        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::110330507156:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "your-external-id"
                },
                "Bool": {
                    "aws:MultiFactorAuthPresent": "true"
                }
            }
        }
    """
    account_id: str = attr.ib()
    external_id: str = attr.ib(default=None)
    mfa_auth: bool = attr.ib(default=False)

    def to_dict(self) -> dict:
        dct = {
            "Effect": "Allow",
            "Principal": {
                "AWS": f"arn:aws:iam::{self.account_id}:root"
            },
            "Action": "sts:AssumeRole",
        }
        condition_dct = dict()
        if self.external_id:
            condition_dct["StringEquals"] = {"sts:ExternalId": self.external_id}
        if self.mfa_auth:
            condition_dct["Bool"] = {"aws:MultiFactorAuthPresent": "true"}
        if len(condition_dct):
            dct["Condition"] = condition_dct
        return dct


@attr.s
class WebIdentityPrincipal(_AwsPrincipal):
    """
    TODO

    Policy document looks like this::

        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "cognito-identity.amazonaws.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "cognito-identity.amazonaws.com:key1": "value2",
                    "cognito-identity.amazonaws.com:key2": "value2"
                }
            }
        }
    """


@attr.s
class SamlPrincipal(_AwsPrincipal):
    """
    TODO
    """


class AssumeRolePolicyBuilder:
    """
    Helper class to build IAM trusted entity / assume role policy.
    """

    def __init__(self, *args: typing.Union[_AwsPrincipal, str]):
        self.principal_list: typing.List[typing.Union[_AwsPrincipal, str]] = args

    def build(self):
        service_principal_list: typing.List[str] = list()
        statements: typing.List[dict] = list()
        for principal in self.principal_list:
            if isinstance(principal, ServicePrincipal):
                service_principal_list.append(principal.service_principal)
            elif isinstance(principal, AccountPrincipal):
                statements.append(principal.to_dict())
            elif isinstance(principal, str):  # pragma: no cover
                if ServiceEnum.is_aws_account_id(principal):
                    statements.append(AccountPrincipal(account_id=principal).to_dict())
                elif ServiceEnum.is_aws_service_domain(principal):
                    service_principal_list.append(principal)
                else: # pragma: no cover
                    raise NotImplementedError
            else:  # pragma: no cover
                raise NotImplementedError
        statements.append({
            "Effect": "Allow",
            "Principal": {
                "Service": service_principal_list
            },
            "Action": "sts:AssumeRole"
        })
        return {
            "Version": "2012-10-17",
            "Statement": statements,
        }


def _find_all_aws_managed_policies() -> typing.List[typing.Tuple[str, str]]:  # pragma: no cover
    import boto3

    aws_profile = "sanhe"
    iam_client = boto3.session.Session(
        profile_name=aws_profile, region_name="us-east-1").client("iam")
    res = iam_client.list_policies(Scope="AWS", MaxItems=1000)
    data = list()
    for policy_dct in res["Policies"]:
        name = policy_dct["PolicyName"].replace("-", "_")
        arn = policy_dct["Arn"]
        data.append((name, arn))
    return data


def _generate_aws_managed_policy_code(aws_managed_policy_data: typing.List[typing.Tuple[str, str]]):  # pragma: no cover
    from pathlib_mate import PathCls as Path

    lines = [
        "# -*- coding: utf-8 -*-",
        "",
        "class _AwsManagedPolicy:",
    ]
    for name, arn in aws_managed_policy_data:
        line = f"{_TAB}{name} = \"{arn}\""
        lines.append(line)

    code = "\n".join(lines)
    Path(__file__).change(new_basename="_iam_aws_managed_policy.py").write_text(code)
