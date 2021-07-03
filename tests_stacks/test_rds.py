# -*- coding: utf-8 -*-

import sqlalchemy
from cottonformation.stacks.rds import rds_stack
from cottonformation.tests.boto_ses import boto_ses
import pysecret
from pathlib_mate import Path

repo_dir = Path(__file__).parent.parent.parent
config_file = Path(repo_dir, "config.json")
js = pysecret.JsonSecret.new(secret_file=config_file.abspath)


def test_public_db():
    conn_str = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}".format(
        host=rds_stack.get_output_value(boto_ses, rds_stack.out_public_db_endpoint.id),
        port=rds_stack.get_output_value(boto_ses, rds_stack.out_public_db_port.id),
        database="postgres",
        username=js.get("example-stack.rds.public_db_username"),
        password=js.get("example-stack.rds.public_db_password"),
    )
    engine = sqlalchemy.create_engine(conn_str, connect_args={"connect_timeout": 6})

    with engine.connect() as conn:
        res = conn.execute("select 999").one()
        assert res[0] == 999


def test_private_db():
    """
    Run this command to create an ssh tunnel. So you can use jumpbox
    to forward your traffic to rds.

    ``ssh -i /path-to-your-pem-file.pem -f -N -L {local_port_for_db_connect}:{rds_endpoint}:{rds_port} {linux_username}@{jumpbox_public-ip} -v``
    :return:
    """
    conn_str = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}".format(
        host="127.0.0.1",
        port=10028,
        database="postgres",
        username=js.get("example-stack.rds.public_db_username"),
        password=js.get("example-stack.rds.public_db_password"),
    )
    engine = sqlalchemy.create_engine(conn_str, connect_args={"connect_timeout": 6})

    with engine.connect() as conn:
        res = conn.execute("select 999").one()
        print(res)
        assert res[0] == 999


if __name__ == "__main__":
    pass
    test_public_db()
    test_private_db()
