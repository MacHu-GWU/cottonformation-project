# -*- coding: utf-8 -*-

import cottonformation as cf
from cottonformation.res import iam, cloudformation


def make_tpl_1() -> cf.Template:
    tpl = cf.Template()

    param_project_name = cf.Parameter(
        "ProjectName",
        Type=cf.Parameter.TypeEnum.String,
    )
    tpl.add(param_project_name)

    policy1 = iam.ManagedPolicy(
        "Policy1",
        p_ManagedPolicyName=cf.Sub.from_params(
            "{}-policy-1",
            param_project_name,
        ),
        rp_PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists.txt"
                }
            ]
        },
    )
    tpl.add(policy1)

    return tpl


def make_tpl_2() -> cf.Template:
    tpl = make_tpl_1()

    policy1: iam.ManagedPolicy = tpl.Resources["Policy1"]
    policy1.rp_PolicyDocument["Statement"][0]["Resource"] = [
        "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists-1.txt",
        "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists-2.txt",
    ]
    policy1.p_Tag = [
        cf.Tag(p_Key="Description", p_Value="this is policy 1"),
    ]

    policy2 = iam.ManagedPolicy(
        "Policy222",
        p_ManagedPolicyName=cf.Sub.from_params(
            "{}-policy-2",
            tpl.Parameters["ProjectName"],
        ),
        rp_PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists.txt"
                }
            ]
        },
    )
    tpl.add(policy2)

    output_policy2_arn = cf.Output(
        "Policy222Arn",
        Value=policy2.ref(),
        Export=cf.Export(
            Name=cf.Sub.from_params(
                "{}-policy-2-arn",
                tpl.Parameters["ProjectName"],
            )
        )
    )
    tpl.add(output_policy2_arn)

    return tpl


def make_tpl_3() -> cf.Template:
    tpl = make_tpl_2()

    tpl.remove(tpl.Resources["Policy1"])

    policy2: iam.ManagedPolicy = tpl.Resources["Policy222"]
    policy2.rp_PolicyDocument["Statement"][0]["Resource"] = [
        "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists-21.txt",
        "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists-22.txt",
    ]
    policy2.p_Tag = [
        cf.Tag(p_Key="Description", p_Value="this is policy 2"),
    ]

    policy3 = iam.ManagedPolicy(
        "Policy33333",
        p_ManagedPolicyName=cf.Sub.from_params(
            "{}-policy-3",
            tpl.Parameters["ProjectName"],
        ),
        rp_PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists.txt"
                }
            ]
        },
    )
    tpl.add(policy3)

    return tpl


def make_tpl_4() -> cf.Template:
    tpl = make_tpl_3()

    policy4 = iam.ManagedPolicy(
        "Policy4",
        p_ManagedPolicyName=cf.Sub.from_params(
            "{}-policy-4",
            tpl.Parameters["ProjectName"],
        ),
        rp_PolicyDocument={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists.txt"
                }
            ]
        },
    )
    tpl.add(policy4)

    # sub template 1
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::this-bucket-not-exists/this-file-not-exists.txt"
            }
        ]
    }

    tpl1 = cf.Template()

    param_project_name = cf.Parameter(
        "ProjectName",
        Type=cf.Parameter.TypeEnum.String,
    )
    tpl1.add(param_project_name)

    policy11 = iam.ManagedPolicy(
        "Policy11",
        p_ManagedPolicyName=cf.Sub.from_params("{}-policy-1-1", param_project_name),
        rp_PolicyDocument=policy_document,
    )
    tpl1.add(policy11)

    # add sub template 1 to main template
    stack1 = cloudformation.Stack(
        "SubStack1",
        rp_TemplateURL="",
        p_Parameters={
            "ProjectName": tpl.Parameters["ProjectName"].ref()
        },
    )
    tpl.add(stack1)
    tpl.add_nested_stack(stack1, tpl1)

    # sub template 11
    tpl11 = cf.Template()

    param_project_name = cf.Parameter(
        "ProjectName",
        Type=cf.Parameter.TypeEnum.String,
    )
    tpl11.add(param_project_name)

    policy111 = iam.ManagedPolicy(
        "Policy111",
        p_ManagedPolicyName=cf.Sub.from_params("{}-policy-1-1-1", param_project_name),
        rp_PolicyDocument=policy_document,
    )
    tpl11.add(policy111)

    # add sub template 11 to sub template 1
    stack11 = cloudformation.Stack(
        "SubStack11",
        rp_TemplateURL="",
        p_Parameters={
            "ProjectName": tpl1.Parameters["ProjectName"].ref()
        },
    )
    tpl1.add(stack11)
    tpl1.add_nested_stack(stack11, tpl11)

    return tpl
