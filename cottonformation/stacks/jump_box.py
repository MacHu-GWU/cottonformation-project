# -*- coding: utf-8 -*-

import typing
import attr
import cottonformation as ctf
from cottonformation.res import ec2, iam
from cottonformation.stacks.vpc import vpc_stack
from cottonformation.tests.boto_ses import boto_ses, bucket


@attr.s
class JumpboxStack(ctf.Stack):
    project_name: str = attr.ib()
    stage: str = attr.ib()
    vpc_id: str = attr.ib()
    public_subnet_cidr_block_list: typing.List[str] = attr.ib()
    jump_box_subnet_id: str = attr.ib()
    jump_box_key_name: str = attr.ib()
    private_box_subnet_id: str = attr.ib()
    private_box_key_name: str = attr.ib()

    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        return f"{self.env_name}-jump-box"

    def __attrs_post_init__(self):
        self.mk_rg1_jump_box()
        self.mk_rg2_private_box()
        self.mk_rg3_redhat_box()
        self.mk_rg4_ubuntu_box()

    def mk_rg1_jump_box(self):
        """
        Create a Jumpbox on Public Subnet for developer to use.
        """
        self.rg1_jump_box = ctf.ResourceGroup()

        self.iam_role_ec2_jump_host = iam.Role(
            "IamRoleEc2JumpBox",
            rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
                ctf.helpers.iam.ServicePrincipal.ec2(),
            ).build(),
            p_RoleName=f"{self.env_name}-iam-role-for-ec2-jump-box",
            p_ManagedPolicyArns=[
                ctf.helpers.iam.AwsManagedPolicy.AdministratorAccess,
            ]
        )
        self.rg1_jump_box.add(self.iam_role_ec2_jump_host)

        self.iam_inst_profile_ec2_jump_box = iam.InstanceProfile(
            "IamInstanceProfileEc2JumpBox",
            rp_Roles=[
                self.iam_role_ec2_jump_host.ref()
            ],
            ra_DependsOn=self.iam_role_ec2_jump_host,
        )
        self.rg1_jump_box.add(self.iam_role_ec2_jump_host)

        self.ec2_jump_host = ec2.Instance(
            "EC2InstanceJumpbox",
            p_ImageId="ami-04d29b6f966df1537", # amz linux 2 hvm
            p_KeyName=self.jump_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.jump_box_subnet_id,
            p_SecurityGroupIds=[
                ctf.ImportValue(name=vpc_stack.output_sg_id_of_allow_all_traffic_from_authorized_ip.Export.Name),
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/xvda",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=256,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    ),
                ),
            ],
            p_IamInstanceProfile=self.iam_inst_profile_ec2_jump_box.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-jump-box",
            ),
            ra_DependsOn=[
                self.iam_inst_profile_ec2_jump_box,
            ],
        )
        self.rg1_jump_box.add(self.ec2_jump_host)

        self.eip = ec2.EIP(
            "EIP",
            p_Domain="vpc",
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-jump-box",
            ),
        )
        self.rg1_jump_box.add(self.eip)
        self.eip_asso = ec2.EIPAssociation(
            "EIPAssociation",
            p_AllocationId=self.eip.rv_AllocationId,
            p_InstanceId=self.ec2_jump_host.ref(),
            ra_DependsOn=[
                self.eip,
                self.ec2_jump_host,
            ]
        )
        self.rg1_jump_box.add(self.eip_asso)

    def mk_rg2_private_box(self):
        self.rg2_private_box = ctf.ResourceGroup()
        self.ec2_private_box = ec2.Instance(
            "EC2InstancePrivateBox",
            p_ImageId="ami-04d29b6f966df1537",
            p_KeyName=self.private_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.private_box_subnet_id,
            p_SecurityGroupIds=[
                ctf.ImportValue(name=vpc_stack.output_sg_id_of_allow_ssh_from_public_subnet.Export.Name),
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/xvda",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=256,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    ),
                ),
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-private-box",
            ),
        )
        self.rg2_private_box.add(self.ec2_private_box)

    def mk_rg3_redhat_box(self):
        self.rg3_redhat = ctf.ResourceGroup()
        self.ec2_redhat_box = ec2.Instance(
            "EC2InstanceMacBox",
            p_ImageId="ami-af3577fe5e3532", # Redhat 8 hvm
            p_KeyName=self.jump_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.jump_box_subnet_id,
            p_SecurityGroupIds=[
                ctf.ImportValue(name=vpc_stack.output_sg_id_of_allow_all_traffic_from_authorized_ip.Export.Name),
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/xvda",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=30,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    ),
                ),
            ],
            p_IamInstanceProfile=self.iam_inst_profile_ec2_jump_box.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-redhat-box",
            ),
        )
        self.rg3_redhat.add(self.ec2_redhat_box)

    def mk_rg4_ubuntu_box(self):
        self.rg4_ubuntu_box = ctf.ResourceGroup()
        self.ec2_ubuntu_box = ec2.Instance(
            "EC2InstanceUbuntuBox",
            p_ImageId="ami-0747bdcabd34c712a", # Ubuntu 18.04 LTS hvm
            p_KeyName=self.jump_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.jump_box_subnet_id,
            p_SecurityGroupIds=[
                ctf.ImportValue(name=vpc_stack.output_sg_id_of_allow_all_traffic_from_authorized_ip.Export.Name),
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/xvda",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=30,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    ),
                ),
            ],
            p_IamInstanceProfile=self.iam_inst_profile_ec2_jump_box.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-ubuntu-box",
            ),
        )
        self.rg4_ubuntu_box.add(self.ec2_ubuntu_box)


# ------ load secret data ------
# below is a code snippet that load secret data
# for testing, you can comment it out and manually pass in hard code value
# for ``public_db_username`` and ``public_db_password``
import pysecret
from pathlib_mate import Path

here = Path(__file__).parent
config_file = Path(here, "config.json")
config = pysecret.JsonSecret.new(secret_file=config_file.abspath)
# ------------------------------

jump_box_stack = JumpboxStack(
    project_name=config.get("example-stack.jump_box.project_name"),
    stage=config.get("example-stack.jump_box.stage"),
    vpc_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_vpc_id.id),
    public_subnet_cidr_block_list=vpc_stack.public_subnet_cidr_block_list,
    jump_box_subnet_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_list_public_subnet_id[0].id),
    jump_box_key_name=config.get("example-stack.jump_box.key_name"),
    private_box_subnet_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_list_private_subnet_id[0].id),
    private_box_key_name=config.get("example-stack.jump_box.key_name"),
)

tpl = ctf.Template()
tpl.add(jump_box_stack.rg1_jump_box)
# tpl.add(jump_box_stack.rg2_private_box)
# tpl.add(jump_box_stack.rg3_redhat)
# tpl.add(jump_box_stack.rg4_ubuntu_box)

tpl.batch_tagging(ProjectName=jump_box_stack.project_name, Stage=jump_box_stack.stage)


if __name__ == "__main__":
    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=jump_box_stack.stack_name,
        bucket_name=bucket,
        include_iam=True,
    )
