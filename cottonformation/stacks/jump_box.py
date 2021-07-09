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
    sg_authorized_ips: typing.List[str] = attr.ib()
    jump_box_subnet_id: str = attr.ib()
    jump_box_key_name: str = attr.ib()
    private_box_subnet_id: str = attr.ib()
    private_box_key_name: str = attr.ib()

    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        return self.env_name

    def __attrs_post_init__(self):
        self.mk_pack1_sg()
        self.mk_pack2_ec2()

    def mk_pack1_sg(self):
        self.pack1_sg = ctf.ResourceGroup()
        self.sg_of_allow_all_traffic_from_authorized_ip = ec2.SecurityGroup(
            "SecurityGroupOfAllowAllTrafficFromAuthorizedIp",
            rp_GroupDescription="Allow all traffic from authorized ip usually workspace ip or developer home ip",
            p_GroupName=f"{self.env_name}/sg/allow-all-traffic-from-authorized-ip",
            p_VpcId=self.vpc_id,
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="-1",
                    p_FromPort=-1,
                    p_ToPort=-1,
                    p_CidrIp=f"{authorized_ip}/32",
                )
                for authorized_ip in self.sg_authorized_ips
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}/sg/allow-all-traffic-from-authorized-ip"
            ),
        )
        self.pack1_sg.add(self.sg_of_allow_all_traffic_from_authorized_ip)

        self.output_sg_id_of_allow_all_traffic_from_authorized_ip = ctf.Output(
            f"{self.sg_of_allow_all_traffic_from_authorized_ip.id}Id",
            Description="Security Group ID",
            Value=self.sg_of_allow_all_traffic_from_authorized_ip.rv_GroupId,
            Export=ctf.Export(
                f"{self.env_name}-{self.sg_of_allow_all_traffic_from_authorized_ip.id}-id"
            ),
            DependsOn=self.sg_of_allow_all_traffic_from_authorized_ip,
        )
        self.pack1_sg.add(self.output_sg_id_of_allow_all_traffic_from_authorized_ip)

        self.sg_of_allow_ssh_from_public_subnet = ec2.SecurityGroup(
            "SecurityGroupOfAllowSSHFromPublicSubnet",
            rp_GroupDescription="Allow ssh in from public subnet",
            p_GroupName=f"{self.env_name}/sg/allow-ssh-from-public-subnet",
            p_VpcId=self.vpc_id,
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="tcp",
                    p_FromPort=22,
                    p_ToPort=22,
                    p_CidrIp=cidr,
                )
                for cidr in self.public_subnet_cidr_block_list
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}/sg/allow-ssh-from-public-subnet"
            ),
        )
        self.pack1_sg.add(self.sg_of_allow_ssh_from_public_subnet)

        self.output_sg_id_of_allow_ssh_from_public_subnet = ctf.Output(
            f"{self.sg_of_allow_ssh_from_public_subnet.id}Id",
            Description="Security Group ID",
            Value=self.sg_of_allow_ssh_from_public_subnet.rv_GroupId,
            Export=ctf.Export(
                f"{self.env_name}-{self.sg_of_allow_ssh_from_public_subnet.id}-id"
            ),
            DependsOn=self.sg_of_allow_ssh_from_public_subnet,
        )
        self.pack1_sg.add(self.output_sg_id_of_allow_ssh_from_public_subnet)

    def mk_pack2_ec2(self):
        self.pack2_ec2 = ctf.ResourceGroup()

        self.iam_role_ec2_jump_host = iam.Role(
            "IamRoleEc2JumpBox",
            rp_AssumeRolePolicyDocument=ctf.helpers.iam.AssumeRolePolicyBuilder(
                ctf.helpers.iam.ServicePrincipal.ec2(),
            ).build(),
            p_RoleName=f"{self.env_name}-iam-role-for-ec2-jump-box",
            p_ManagedPolicyArns=[
                ctf.helpers.iam.AwsManagedPolicy.AmazonSSMManagedInstanceCore,
            ]
        )
        self.pack2_ec2.add(self.iam_role_ec2_jump_host)

        self.iam_inst_profile_ec2_jump_box = iam.InstanceProfile(
            "IamInstanceProfileEc2JumpBox",
            rp_Roles=[
                self.iam_role_ec2_jump_host.ref()
            ],
            ra_DependsOn=self.iam_role_ec2_jump_host,
        )
        self.pack2_ec2.add(self.iam_role_ec2_jump_host)

        self.ec2_jump_host = ec2.Instance(
            "EC2InstanceJumpbox",
            p_ImageId="ami-04d29b6f966df1537",
            p_KeyName=self.jump_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.jump_box_subnet_id,
            p_SecurityGroupIds=[
                self.sg_of_allow_all_traffic_from_authorized_ip.rv_GroupId
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/sdm",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=100,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    )
                ),
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/sdk",
                    p_NoDevice=ec2.PropInstanceNoDevice(),
                ),
            ],
            p_IamInstanceProfile=self.iam_inst_profile_ec2_jump_box.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-jump-box",
            ),
            ra_DependsOn=[
                self.sg_of_allow_all_traffic_from_authorized_ip,
                self.iam_inst_profile_ec2_jump_box,
            ],
        )
        self.pack2_ec2.add(self.ec2_jump_host)

        self.ec2_private_box = ec2.Instance(
            "EC2InstancePrivateBox",
            p_ImageId="ami-04d29b6f966df1537",
            p_KeyName=self.private_box_key_name,
            p_InstanceType="t2.micro",
            p_SubnetId=self.private_box_subnet_id,
            p_SecurityGroupIds=[
                self.sg_of_allow_ssh_from_public_subnet.rv_GroupId
            ],
            p_BlockDeviceMappings=[
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/sdm",
                    p_Ebs=ec2.PropInstanceEbs(
                        p_DeleteOnTermination=True,
                        p_VolumeSize=8,
                        p_VolumeType="gp2",
                        p_Encrypted=False,
                    )
                ),
                ec2.PropInstanceBlockDeviceMapping(
                    rp_DeviceName="/dev/sdk",
                    p_NoDevice=ec2.PropInstanceNoDevice(),
                ),
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}-private-box",
            ),
            ra_DependsOn=self.sg_of_allow_ssh_from_public_subnet,
        )
        self.pack2_ec2.add(self.ec2_private_box)


# ------ load secret data ------
# below is a code snippet that load secret data
# for testing, you can comment it out and manually pass in hard code value
# for ``public_db_username`` and ``public_db_password``
import pysecret
from pathlib_mate import Path

repo_dir = Path(__file__).parent.parent.parent
config_file = Path(repo_dir, "config.json")
js = pysecret.JsonSecret.new(secret_file=config_file.abspath)
# ------------------------------


jump_box_stack = JumpboxStack(
    project_name="ctf-lib-jump-box",
    stage="dev",
    vpc_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_vpc_id.id),
    public_subnet_cidr_block_list=vpc_stack.public_subnet_cidr_block_list,
    sg_authorized_ips=js.get("example-stack.rds.sg_authorized_ips"),
    jump_box_subnet_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_list_public_subnet_id[0].id),
    jump_box_key_name="eq-sanhe-dev",
    private_box_subnet_id=vpc_stack.get_output_value(boto_ses, vpc_stack.out_list_private_subnet_id[0].id),
    private_box_key_name="eq-sanhe-dev",
)

tpl = ctf.Template()
tpl.add(jump_box_stack.pack1_sg)
tpl.add(jump_box_stack.pack2_ec2)


if __name__ == "__main__":
    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=jump_box_stack.stack_name,
        bucket_name=bucket,
        include_iam=True,
    )
