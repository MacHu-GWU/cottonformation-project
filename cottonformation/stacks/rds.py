# -*- coding: utf-8 -*-

import typing
import attr
import cottonformation as ctf
from cottonformation.res import ec2, rds
from cottonformation.stacks.vpc import vpc_stack
from cottonformation.stacks.jump_box import jump_box_stack
from cottonformation.tests.boto_ses import boto_ses, bucket


@attr.s
class RdsStack(ctf.Stack):
    project_name: str = attr.ib()
    stage: str = attr.ib()

    public_db_username: str = attr.ib(default=None)
    public_db_password: str = attr.ib(default=None)
    private_db_username: str = attr.ib(default=None)
    private_db_password: str = attr.ib(default=None)

    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        return self.env_name

    def __attrs_post_init__(self):
        self.mk_pack1_public_db()

    def mk_pack1_public_db(self):
        self.pack1_public_db = ctf.ResourceGroup()
        self.public_db_security_group = ec2.SecurityGroup(
            "SecurityGroupForPublicDB",
            rp_GroupDescription="Security Group used for Public accessible DB Instance",
            p_GroupName=f"{self.env_name}-public-db",
            p_VpcId=ctf.ImportValue(vpc_stack.out_vpc_id.Export.Name),
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="TCP",
                    p_Description="Allow authorized ip to connect",
                    p_FromPort=5432,
                    p_ToPort=5432,
                    p_CidrIp=f"{ip}/32",
                )
                for ip in jump_box_stack.sg_authorized_ips
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
            p_Tags=ctf.Tag.make_many(Name=f"{self.project_name}-{self.env_name}")
        )
        self.pack1_public_db.add(self.public_db_security_group)

        self.public_db_subnet_group = rds.DBSubnetGroup(
            "DBSubnetGroupForPublicDB",
            rp_DBSubnetGroupDescription="DB Subnet Group for Public accessible DB",
            rp_SubnetIds=[
                ctf.ImportValue(out.Export.Name)
                for out in vpc_stack.out_list_public_subnet_id
            ],
            p_DBSubnetGroupName=f"{self.env_name}-dev-db",
            ra_DependsOn=self.public_db_security_group,
        )
        self.pack1_public_db.add(self.public_db_subnet_group)

        self.public_db_instance = rds.DBInstance(
            "DBInstancePublicDB",
            rp_DBInstanceClass="db.t3.micro",
            p_DBInstanceIdentifier=f"{self.env_name}-dev-db",
            p_Engine="postgres",
            p_EngineVersion="11.9",
            p_MultiAZ=False,
            p_AllocatedStorage="100",
            p_DBSubnetGroupName=self.public_db_subnet_group.ref(),
            p_VPCSecurityGroups=[
                self.public_db_security_group.rv_GroupId,
            ],
            p_MasterUsername=self.public_db_username,
            p_MasterUserPassword=self.public_db_password,
            p_PubliclyAccessible=True,
            ra_DependsOn=self.public_db_security_group,
        )
        self.pack1_public_db.add(self.public_db_instance)

        self.out_public_db_endpoint = ctf.Output(
            "PublicDbEndpoint",
            Value=self.public_db_instance.rv_EndpointAddress,
        )
        self.pack1_public_db.add(self.out_public_db_endpoint)

        self.out_public_db_port = ctf.Output(
            "PublicDbPort",
            Value=self.public_db_instance.rv_EndpointPort,
        )
        self.pack1_public_db.add(self.out_public_db_port)


    def mk_pack2_private_db(self):
        self.pack2_private_db = ctf.ResourceGroup()
        self.private_db_security_group = ec2.SecurityGroup(
            "SecurityGroupForPrivateDB",
            rp_GroupDescription="Security Group used for DB Instance on Private Subnet",
            p_GroupName=f"{self.env_name}-private-db",
            p_VpcId=ctf.ImportValue(vpc_stack.out_vpc_id.Export.Name),
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="TCP",
                    p_Description="Allow db connection from public subnet",
                    p_FromPort=5432,
                    p_ToPort=5432,
                    p_CidrIp=public_subnet_cidr,
                )
                for public_subnet_cidr in vpc_stack.public_subnet_cidr_block_list
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
            p_Tags=ctf.Tag.make_many(Name=f"{self.project_name}-{self.env_name}")
        )
        self.pack2_private_db.add(self.private_db_security_group)

        self.private_db_subnet_group = rds.DBSubnetGroup(
            "DBSubnetGroupForPrivateDB",
            rp_DBSubnetGroupDescription="DB Subnet Group for DB Instance on Private Subnet",
            rp_SubnetIds=[
                ctf.ImportValue(out.Export.Name)
                for out in vpc_stack.out_list_private_subnet_id
            ],
            p_DBSubnetGroupName=f"{self.env_name}-dev-db",
            ra_DependsOn=self.private_db_security_group,
        )
        self.pack2_private_db.add(self.private_db_subnet_group)

        self.private_db_instance = rds.DBInstance(
            "DBInstancePrivateDB",
            rp_DBInstanceClass="db.t3.micro",
            p_DBInstanceIdentifier=f"{self.env_name}-dev-db",
            p_Engine="postgres",
            p_EngineVersion="11.9",
            p_MultiAZ=False,
            p_AllocatedStorage="100",
            p_DBSubnetGroupName=self.private_db_subnet_group.ref(),
            p_VPCSecurityGroups=[
                self.private_db_security_group.rv_GroupId,
            ],
            p_MasterUsername=self.private_db_username,
            p_MasterUserPassword=self.private_db_password,
            p_PubliclyAccessible=True,
            ra_DependsOn=[
                self.private_db_security_group,
                self.public_db_subnet_group
            ]
        )
        self.pack2_private_db.add(self.private_db_subnet_group)

        self.out_private_db_endpoint = ctf.Output(
            "PrivateDbEndpoint",
            Value=self.private_db_instance.rv_EndpointAddress,
        )
        self.pack2_private_db.add(self.out_private_db_endpoint)

        self.out_pivate_db_port = ctf.Output(
            "PrivateDbPort",
            Value=self.private_db_instance.rv_EndpointPort,
        )
        self.pack2_private_db.add(self.out_pivate_db_port)


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

rds_stack = RdsStack(
    project_name="ctf-lib-rds",
    stage="dev",
    public_db_username=js.get("example-stack.rds.public_db_username"),
    public_db_password=js.get("example-stack.rds.public_db_password"),
)

tpl = ctf.Template()
tpl.add(rds_stack.pack1_public_db)
tpl.add(rds_stack.pack2_private_db)
tpl.batch_tagging(ProjectName=rds_stack.project_name, Stage=rds_stack.stage)


if __name__ == "__main__":
    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=rds_stack.stack_name,
        bucket_name=bucket,
    )
