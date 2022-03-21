# -*- coding: utf-8 -*-

import cottonformation as cft
from cottonformation.res import iam

tpl = cft.Template()

# declare Parameter
param_project_name = cft.Parameter(
    "ProjectName",
    Type=cft.Parameter.TypeEnum.String,
)
tpl.add(param_project_name)

iam_policy = iam.ManagedPolicy(
    "IamPolicy",
    # use
    p_ManagedPolicyName=cft.Sub(
        string="${aws_account_id}-${project_name}",
        data=dict(
            aws_account_id=cft.AWS_ACCOUNT_ID,
            project_name=param_project_name.ref(),
        )
    ),
    rp_PolicyDocument={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::a-bucket-never-exists"
            }
        ]
    },
)
tpl.add(iam_policy)

if __name__ == "__main__":
    project_name = "cottonformation-example"

    param_project_name.set_value(project_name)

    env = cft.Env()
    env.deploy(
        template=tpl,
        stack_name=project_name,
        stack_parameters=tpl.get_param_values(),
        include_iam=True,
    )
