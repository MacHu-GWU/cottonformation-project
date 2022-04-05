# -*- coding: utf-8 -*-

from cottonformation.core.helpers import iam

# service_name_list = iam._find_all_service_name_list_from_gist()
service_name_list = iam._find_all_service_name_list_from_botocore()
iam._generate_aws_service_principal_code(service_name_list)

aws_managed_policy_data = iam._find_all_aws_managed_policies()
iam._generate_aws_managed_policy_code(aws_managed_policy_data)