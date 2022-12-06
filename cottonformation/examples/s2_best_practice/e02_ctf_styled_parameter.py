# -*- coding: utf-8 -*-

import attr
import cottonformation as ctf
from cottonformation.res import s3


# declare a Parameter object
@attr.s
class Params:
    project_name: str = attr.ib()
    stage: str = attr.ib()

    # a derived value as a prefix for all naming convention and tag
    @property
    def env_name(self):
        return f"{self.project_name}-{self.stage}"


# declare a function that creates Template object from Parameters, Mappings,
# Conditions, Rules ...
def create_template(params: Params) -> ctf.Template:
    tpl = ctf.Template(Description="Demo: ctf styled parameter")

    bucket = s3.Bucket("MyBucket", p_BucketName=f"{params.env_name}-my-bucket")
    tpl.add(bucket)

    tpl.batch_tagging(dict(EnvName=params.env_name))

    return tpl


if __name__ == "__main__":
    # give values to parameters
    param = Params(
        project_name="ctf-styled-param",
        stage="dev"
    )
    tpl = create_template(param)
    print(tpl.to_json())
