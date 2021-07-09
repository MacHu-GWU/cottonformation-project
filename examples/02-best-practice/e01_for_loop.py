# -*- coding: utf-8 -*-

"""
Since cottonformation is simply Python code, you can use for loop to create
many AWS object (Parameter, Resource, Output, etc...) in batch.
"""

import typing
import cottonformation as ctf
from cottonformation.res import ec2

tpl = ctf.Template()

NOT_IMPORTANT_IN_THIS_EXAMPLE = "not-important-in-this-example"

# example 1. make many AWS resource using for loop
n_subnet = 3
subnet_list: typing.List[ec2.Subnet] = list()
for index in range(1, n_subnet + 1):
    subnet = ec2.Subnet(
        f"Subnet{index}",
        rp_CidrBlock=f"10.1.{index}.0/24", # the first subnet is 10.1.1.0/24, second is 10.1.2.0/24, ...
        rp_VpcId=NOT_IMPORTANT_IN_THIS_EXAMPLE,
        p_AvailabilityZone=ctf.GetAZs.n_th(index-1), # deploy subnet to different availability zone for high availability.
    )
    subnet_list.append(subnet)

# example 2. define many resource property using for loop
authorized_ip_list = [
    "0.0.0.1",
    "0.0.0.2",
    "0.0.0.3",
]
sg = ec2.SecurityGroup(
    "SecurityGroup",
    rp_GroupDescription="not-important-in-this-example",
    p_GroupName="allow-authorized-ip-ssh",
    p_VpcId="not-important-in-this-example",
    p_SecurityGroupIngress=[
        # make many security group ingress rule
        ec2.PropSecurityGroupIngress(
            rp_IpProtocol="SSH",
            p_FromPort=22,
            p_ToPort=22,
            p_CidrIp=f"{ip}/32",
        )
        for ip in authorized_ip_list
    ],
    p_SecurityGroupEgress=[
        ec2.PropSecurityGroupEgress(
            rp_IpProtocol="-1",
            p_Description="Allow any access out",
            p_FromPort=-1,
            p_ToPort=-1,
            p_CidrIp="0.0.0.0/0",
        )
    ],
)