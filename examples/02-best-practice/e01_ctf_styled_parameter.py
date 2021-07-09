# -*- coding: utf-8 -*-

import attr
import cottonformation as ctf
from cottonformation.res import s3


@attr.s
class Param:
    project_name: str = attr.ib()
    stage: str = attr.ib()

    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"


def create_template(param: Param) -> ctf.Template:
    tpl = ctf.Template(Description="Demo: ctf styled parameter")

    bucket = s3.Bucket("MyBucket", p_BucketName=f"{param.env_name}-my-bucket")
    tpl.add(bucket)

    tpl.batch_tagging(EnvName=param.env_name)

    return tpl


if __name__ == "__main__":
    param = Param(
        project_name="ctf-styled-param",
        stage="dev"
    )
    tpl = create_template(param)
    print(tpl.to_json())
