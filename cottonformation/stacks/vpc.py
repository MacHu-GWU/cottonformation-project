# -*- coding: utf-8 -*-

import typing
import attr
import cottonformation as ctf
from cottonformation.res import ec2


@attr.s
class VpcStack(ctf.Stack):
    project_name: str = attr.ib()
    stage: str = attr.ib()
    vpc_cidr_seed: int = attr.ib()
    n_az_used: int = attr.ib()
    sg_authorized_ips: typing.List[str] = attr.ib()

    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"

    @property
    def stack_name(self):
        return f"{self.env_name}-vpc"

    @property
    def vpc_cidr_block(self):
        return f"10.{self.vpc_cidr_seed}.0.0/16"

    @property
    def public_subnet_cidr_block_list(self):
        return [
            "10.{}.{}.0/24".format(
                self.vpc_cidr_seed,
                ind * 2,
            )
            for ind in range(1, self.n_az_used + 1)
        ]

    def __attrs_post_init__(self):
        self.mk_rg1_vpc()
        self.mk_rg2_subnet()
        self.mk_rg3_route()
        self.mk_pk4_security_group()

    def mk_rg1_vpc(self):
        self.rg1_vpc = ctf.ResourceGroup()
        self.vpc = ec2.VPC(
            "VPC",
            rp_CidrBlock=self.vpc_cidr_block,
            p_EnableDnsHostnames=True,
            p_Tags=ctf.Tag.make_many(
                Name=ctf.Sub.from_params(f"{self.env_name}-vpc"),
                Description=ctf.Sub.from_params(f"The main vpc for {self.env_name}"),
            ),
        )

        self.out_vpc_id = ctf.Output(
            "VpcId",
            Description="VPC Id",
            Value=self.vpc.ref(),
            Export=ctf.Export(f"{self.env_name}-vpc-id"),
            DependsOn=self.vpc,
        )

        self.out_vpc_cidr_block = ctf.Output(
            "VpcCidrBlock",
            Description="VPC Cidr Block",
            Value=self.vpc.rv_CidrBlock,
            Export=ctf.Export(f"{self.env_name}-vpc-cidr-block"),
            DependsOn=self.vpc,
        )
        self.rg1_vpc.DependsOn.extend([self.vpc, self.out_vpc_id, self.out_vpc_cidr_block])

    def mk_rg2_subnet(self):
        self.rg2_subnet = ctf.ResourceGroup()

        self.public_subnet_list: typing.List[ec2.Subnet] = list()
        self.out_list_public_subnet_id: typing.List[ctf.Output] = list()
        for ind in range(1, self.n_az_used + 1):
            public_subnet = ec2.Subnet(
                f"PublicSubnet{ind}",
                rp_CidrBlock="10.{}.{}.0/24".format(
                    self.vpc_cidr_seed,
                    ind * 2 - 1,
                ),
                rp_VpcId=self.vpc.ref(),
                p_AvailabilityZone=ctf.GetAZs.n_th(ind),
                p_MapPublicIpOnLaunch=True,
                p_Tags=ctf.Tag.make_many(
                    Name=f"{self.env_name}/public/{ind}",
                ),
                ra_DependsOn=self.vpc,
            )
            self.public_subnet_list.append(public_subnet)

            out = ctf.Output(
                f"{public_subnet.id}Id",
                Description=f"{public_subnet.id} Id",
                Value=public_subnet.ref(),
                Export=ctf.Export(
                    "{}-{}-id".format(
                        self.env_name,
                        public_subnet.id.lower().replace("subnet", "-subnet-")
                    ),
                ),
                DependsOn=public_subnet,
            )
            self.out_list_public_subnet_id.append(out)

            self.rg2_subnet.DependsOn.append(public_subnet)
            self.rg2_subnet.DependsOn.append(out)

        self.private_subnet_list: typing.List[ec2.Subnet] = list()
        self.out_list_private_subnet_id: typing.List[ctf.Output] = list()
        for ind in range(1, self.n_az_used + 1):
            private_subnet = ec2.Subnet(
                f"PrivateSubnet{ind}",
                rp_CidrBlock="10.{}.{}.0/24".format(
                    self.vpc_cidr_seed,
                    ind * 2,
                ),
                rp_VpcId=self.vpc.ref(),
                p_AvailabilityZone=ctf.GetAZs.n_th(ind),
                p_MapPublicIpOnLaunch=False,
                p_Tags=ctf.Tag.make_many(
                    Name=f"{self.env_name}/private/{ind}",
                ),
                ra_DependsOn=self.vpc,
            )
            self.private_subnet_list.append(private_subnet)

            out = ctf.Output(
                f"{private_subnet.id}Id",
                Description=f"{private_subnet.id} Id",
                Value=private_subnet.ref(),
                Export=ctf.Export(
                    "{}-{}-id".format(
                        self.env_name,
                        private_subnet.id.lower().replace("subnet", "-subnet-")
                    ),
                ),
                DependsOn=private_subnet,
            )
            self.out_list_private_subnet_id.append(out)

            self.rg2_subnet.DependsOn.append(private_subnet)
            self.rg2_subnet.DependsOn.append(out)

        self.out_list_subnet_cidr_block: typing.List[ctf.Output] = list()
        for subnet in (self.public_subnet_list + self.private_subnet_list):
            out = ctf.Output(
                f"{subnet.id}CidrBlock",
                Description=f"{subnet.id} Cidr Block",
                Value=subnet.rp_CidrBlock,
                Export=ctf.Export(
                    "{}-{}-cidr-block".format(
                        self.env_name,
                        subnet.id.lower().replace("subnet", "-subnet-")
                    ),
                ),
                DependsOn=subnet,
            )
            self.out_list_subnet_cidr_block.append(out)
            self.rg2_subnet.DependsOn.append(out)

    def mk_rg3_route(self):
        self.rg3_route = ctf.ResourceGroup()

        self.igw = ec2.InternetGateway(
            "IGW",
            p_Tags=ctf.Tag.make_many(
                Name=self.env_name,
            ),
        )

        self.igw_attach_vpc = ec2.VPCGatewayAttachment(
            "IGWAttachVpc",
            rp_VpcId=self.vpc.ref(),
            p_InternetGatewayId=self.igw.ref(),
            ra_DependsOn=[self.vpc, self.igw]
        )

        self.eip = ec2.EIP(
            "EIP",
            p_Domain="vpc",
            p_Tags=ctf.Tag.make_many(
                Name=self.env_name,
            ),
            ra_DependsOn=self.vpc,
        )

        self.ngw = ec2.NatGateway(
            "NGW",
            rp_SubnetId=self.public_subnet_list[0].ref(),
            p_AllocationId=self.eip.rv_AllocationId,
            p_Tags=ctf.Tag.make_many(
                Name=self.env_name,
            ),
            ra_DependsOn=self.eip,
        )

        self.rg3_route.DependsOn.extend([self.igw, self.igw_attach_vpc, self.eip, self.ngw])

        # public / private route table
        self.public_route_table = ec2.RouteTable(
            "PublicRouteTable",
            rp_VpcId=self.vpc.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=self.env_name,
            ),
            ra_DependsOn=self.vpc,
        )

        self.public_route_default = ec2.Route(
            "PublicRouteDefault",
            rp_RouteTableId=self.public_route_table.ref(),
            p_DestinationCidrBlock="0.0.0.0/0",
            p_GatewayId=self.igw.ref(),
            ra_DependsOn=[self.public_route_table, self.igw],
        )

        self.rg3_route.DependsOn.extend([self.public_route_table, self.public_route_default])

        for ind, subnet in enumerate(self.public_subnet_list):
            route_table_association = ec2.SubnetRouteTableAssociation(
                "PublicSubnet{}RouteTableAssociation".format(ind + 1),
                rp_RouteTableId=self.public_route_table.ref(),
                rp_SubnetId=subnet.ref(),
                ra_DependsOn=[self.public_route_table, subnet],
            )
            self.rg3_route.DependsOn.append(route_table_association)

        self.private_route_table = ec2.RouteTable(
            "PrivateRouteTable",
            rp_VpcId=self.vpc.ref(),
            p_Tags=ctf.Tag.make_many(
                Name=self.env_name,
            ),
            ra_DependsOn=self.vpc,
        )

        self.private_route_default = ec2.Route(
            "PrivateRouteDefault",
            rp_RouteTableId=self.private_route_table.ref(),
            p_DestinationCidrBlock="0.0.0.0/0",
            p_NatGatewayId=self.ngw.ref(),
            ra_DependsOn=[self.private_route_table, self.ngw],
        )

        self.rg3_route.DependsOn.extend([self.private_route_table, self.private_route_default])

        for ind, subnet in enumerate(self.private_subnet_list):
            route_table_association = ec2.SubnetRouteTableAssociation(
                "PrivateSubnet{}RouteTableAssociation".format(ind + 1),
                rp_RouteTableId=self.private_route_table.ref(),
                rp_SubnetId=subnet.ref(),
                ra_DependsOn=[self.private_route_table, subnet],
            )
            self.rg3_route.DependsOn.append(route_table_association)

    def mk_pk4_security_group(self):
        self.rg4_security_group = ctf.ResourceGroup()
        self.sg_of_allow_restricted_traffic_from_authorized_ip = ec2.SecurityGroup(
            "SecurityGroupOfAllowRestrictedTrafficFromAuthorizedIp",
            rp_GroupDescription="Allow restricted traffic from authorized ip usually workspace ip or developer home ip",
            p_GroupName=f"{self.env_name}/sg/allow-restricted-traffic-from-authorized-ip",
            p_VpcId=self.vpc.ref(),
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="tcp",
                    p_FromPort=22,
                    p_ToPort=22,
                    p_CidrIp=f"{authorized_ip}/32",
                )
                for authorized_ip in self.sg_authorized_ips
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}/sg/allow-restricted-traffic-from-authorized-ip"
            ),
            ra_DependsOn=self.vpc,
        )
        self.rg4_security_group.add(self.sg_of_allow_restricted_traffic_from_authorized_ip)

        self.output_sg_id_of_allow_all_traffic_from_authorized_ip = ctf.Output(
            f"{self.sg_of_allow_restricted_traffic_from_authorized_ip.id}Id",
            Description="Security Group ID",
            Value=self.sg_of_allow_restricted_traffic_from_authorized_ip.rv_GroupId,
            Export=ctf.Export(
                f"{self.env_name}-{self.sg_of_allow_restricted_traffic_from_authorized_ip.id}-id"
            ),
            DependsOn=self.sg_of_allow_restricted_traffic_from_authorized_ip,
        )
        self.rg4_security_group.add(self.output_sg_id_of_allow_all_traffic_from_authorized_ip)

        self.sg_of_allow_ssh_from_public_subnet = ec2.SecurityGroup(
            "SecurityGroupOfAllowSSHFromPublicSubnet",
            rp_GroupDescription="Allow ssh in from public subnet",
            p_GroupName=f"{self.env_name}/sg/allow-ssh-from-public-subnet",
            p_VpcId=self.vpc.ref(),
            p_SecurityGroupIngress=[
                ec2.PropSecurityGroupIngress(
                    rp_IpProtocol="tcp",
                    p_FromPort=22,
                    p_ToPort=22,
                    p_CidrIp=subnet.rp_CidrBlock,
                )
                for subnet in self.public_subnet_list
            ],
            p_Tags=ctf.Tag.make_many(
                Name=f"{self.env_name}/sg/allow-ssh-from-public-subnet"
            ),
            ra_DependsOn=[self.vpc, ] + self.public_subnet_list,
        )
        self.rg4_security_group.add(self.sg_of_allow_ssh_from_public_subnet)

        self.output_sg_id_of_allow_ssh_from_public_subnet = ctf.Output(
            f"{self.sg_of_allow_ssh_from_public_subnet.id}Id",
            Description="Security Group ID",
            Value=self.sg_of_allow_ssh_from_public_subnet.rv_GroupId,
            Export=ctf.Export(
                f"{self.env_name}-{self.sg_of_allow_ssh_from_public_subnet.id}-id"
            ),
            DependsOn=self.sg_of_allow_ssh_from_public_subnet,
        )
        self.rg4_security_group.add(self.output_sg_id_of_allow_ssh_from_public_subnet)


# ------ load secret data ------
# below is a code snippet that load config and secret data
# for testing, you can comment it out and manually pass in hard code value
import pysecret
from pathlib_mate import Path

here = Path(__file__).parent
config_file = Path(here, "config.json")
config = pysecret.JsonSecret.new(secret_file=config_file.abspath)
# ------------------------------

vpc_stack = VpcStack(
    project_name=config.get("example-stack.vpc.project_name"),
    stage=config.get("example-stack.vpc.stage"),
    vpc_cidr_seed=config.get("example-stack.vpc.vpc_cidr_seed"),
    n_az_used=config.get("example-stack.vpc.n_az_used"),
    sg_authorized_ips=config.get("example-stack.vpc.sg_authorized_ips")
)

tpl = ctf.Template()
tpl.add(vpc_stack.rg1_vpc)
tpl.add(vpc_stack.rg2_subnet)
tpl.add(vpc_stack.rg3_route)
tpl.add(vpc_stack.rg4_security_group)

tpl.batch_tagging(ProjectName=vpc_stack.project_name, Stage=vpc_stack.stage)


if __name__ == "__main__":
    from cottonformation.tests.boto_ses import boto_ses, bucket

    env = ctf.Env(boto_ses=boto_ses)
    env.deploy(
        template=tpl,
        stack_name=vpc_stack.stack_name,
        bucket_name=bucket,
    )
