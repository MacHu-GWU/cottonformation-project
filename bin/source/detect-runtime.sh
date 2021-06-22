#!/bin/bash
# -*- coding: utf-8 -*-

curl -s http://169.254.169.254/latest/dynamic/instance-identity/ -m 1 > /tmp/null # timeout 1 second
if [ $? -eq 0 ]; then # if has response
    is_ec2="Y"
else
    is_ec2="N"
fi

if [ -n "$CI" ]; then # if has value
    is_ci="Y"
else
    is_ci="N"
fi

if [ -n "$TRAVIS" ]; then # if has value
    is_travisci="Y"
else
    is_travisci="N"
fi

if [ -n "$CIRCLECI" ]; then # if has value
    is_circleci="Y"
else
    is_circleci="N"
fi

if [ -n "$CODEBUILD_BUILD_ID" ]; then # if has value
    is_aws_codebuild="Y"
else
    is_aws_codebuild="N"
fi
