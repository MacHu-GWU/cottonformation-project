# -*- coding: utf-8 -*-

import sqlalchemy
from cottonformation.stacks.rds import rds_stack

conn_str = "postgresql+psycopg2://scott:tiger@localhost/postgres"
engine = create_engine()