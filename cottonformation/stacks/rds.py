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


    # vpc_id: str = attr.ib()

    # sg_authorized_ips: typing.List[str] = attr.ib()
    # jump_box_subnet_id: str = attr.ib()
    # jump_box_key_name: str = attr.ib()
    # private_box_subnet_id: str = attr.ib()
    # private_box_key_name: str = attr.ib()
    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        return self.env_name

    def __attrs_post_init__(self):
        self.mk_pack1_public_db()

    def mk_pack1_public_db(self):
        self.pack1_public_db = ctf.Pack()
        self.public_db_security_group = ec2.SecurityGroup(
            "SecurityGroupForPublicDB",
            rp_GroupDescription="Security Group used for Public accessible DB Instance",
            p_GroupName=f"{self.env_name}-public-db",
            p_VpcId=ctf.ImportValue(vpc_stack.out_vpc_id.Export.Name),
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="-1",
                    p_Description="Allow authorized ip to connect",
                    p_FromPort=-1,
                    p_ToPort=-1,
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
        )
        self.pack1_public_db.add(self.public_db_subnet_group)

        self.public_db_instance = rds.DBInstance(
            "DBInstancePubliicDB",
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
        )
        self.pack1_public_db.add(self.public_db_instance)


rds_stack = RdsStack(
    project_name="ctf-lib-rds",
    stage="dev",
    public_db_username="username",
    public_db_password="password"
)

tpl = ctf.Template()
tpl.add(rds_stack.pack1_public_db)

if __name__ == "__main__":
    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=rds_stack.stack_name,
        bucket_name=bucket,
    )
