# -*- coding: utf-8 -*-

"""
Generate the ssh command to connect to ec2 for you.

Ref:

- Default user name for AMI: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html#connection-prereqs-get-info-about-instance

- For Amazon Linux 2 or the Amazon Linux AMI, the user name is ec2-user.
- For a CentOS AMI, the user name is centos.
- For a Debian AMI, the user name is admin.
- For a Fedora AMI, the user name is ec2-user or fedora.
- For a RHEL AMI, the user name is ec2-user or root.
- For a SUSE AMI, the user name is ec2-user or root.
- For an Ubuntu AMI, the user name is ubuntu.
"""

from __future__ import print_function
import boto3
from pprint import pprint

#------------------------- File in value here -------------------------
aws_profile = "aws_data_lab_sanhe"
region = "us-east-1"
ec2_name = "sanhe-infra-dev-jump-box"
ec2_pem = "~/ec2-pem/aws-data-lab-sanhe-dev.pem"
#----------------------------------------------------------------------

boto_ses = boto3.session.Session(profile_name=aws_profile, region_name=region)
ec2_client = boto_ses.client("ec2")

res = ec2_client.describe_instances(Filters=[dict(Name="tag:Name", Values=[ec2_name,])])

inst_dict_list = list()
for res_dict in res["Reservations"]:
    for inst_dict in res_dict["Instances"]:
        inst_dict_list.append(inst_dict)

inst_dict = None
for _inst_dict in inst_dict_list:
    if _inst_dict["State"]["Name"] == "running":
        inst_dict = _inst_dict

if inst_dict is None:
    print("there's no running EC2 named '{}' in aws region {}".format(ec2_name, region))
    exit(1)

public_ip = inst_dict["PublicIpAddress"]
image_id = inst_dict["ImageId"]

image_dct = ec2_client.describe_images(ImageIds=[image_id,])["Images"][0]
image_name = image_dct["Name"]
if image_name.startswith("amzn"):
    username = "ec2-user"
elif image_name.startswith("RHEL"):
    username = "ec2-user"
elif image_name.startswith("suse"):
    username = "ec2-user"
elif image_name.startswith("fedora"):
    username = "ec2-user"
elif image_name.startswith("ubuntu"):
    username = "ubuntu"
elif image_name.startswith("debian"):
    username = "admin"
else:
    username = "ec2-user"

cmd = "ssh -i {ec2_pem} {username}@{public_ip}".format(
    ec2_pem=ec2_pem, username=username, public_ip=public_ip)
print(cmd)
