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

import boto3

#------------------------- File in value here -------------------------
aws_profile = "eq_sanhe"
region = "us-east-1"
ec2_name = "ctf-lib-jump-box-dev-jump-box"
ec2_pem = "~/ec2-pem/eq-sanhe-dev.pem"
#----------------------------------------------------------------------

boto_ses = boto3.session.Session(profile_name=aws_profile, region_name=region)
ec2_client = boto_ses.client("ec2")

res = ec2_client.describe_instances(Filters=[dict(Name="tag:Name", Values=[ec2_name,])])
inst_dict = res["Reservations"][0]["Instances"][0]
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
