# -*- coding: utf-8 -*-

import cottonformation as cf
from cottonformation.res import iam, cloudformation


def make_tpl_1() -> cf.Template:
    tpl = cf.Template()

    policy1 = iam.ManagedPolicy(
        "Policy1",
        p_ManagedPolicyName="cf-int-test-policy-1",
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
        p_ManagedPolicyName="cf-int-test-policy-2",
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
        p_ManagedPolicyName="cf-int-test-policy-3",
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

    # sub template
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
    policy11 = iam.ManagedPolicy(
        "Policy11",
        p_ManagedPolicyName="cf-int-test-policy-1-1",
        rp_PolicyDocument=policy_document,
    )
    tpl1.add(policy11)

    tpl2 = cf.Template()
    policy21 = iam.ManagedPolicy(
        "Policy21",
        p_ManagedPolicyName="cf-int-test-policy-2-1",
        rp_PolicyDocument=policy_document,
    )
    tpl2.add(policy21)

    # add sub template to main template
    stack1 = cloudformation.Stack(
        "SubStack1",
        rp_TemplateURL="",
    )
    tpl.add(stack1)
    tpl.add_nested_stack(stack1, tpl1)

    stack2 = cloudformation.Stack(
        "SubStack2",
        rp_TemplateURL="",
    )
    tpl.add(stack2)
    tpl.add_nested_stack(stack2, tpl2)

    return tpl


