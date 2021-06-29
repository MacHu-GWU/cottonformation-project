# -*- coding: utf-8 -*-

class LambdaRuntime:
    """
    Aws Lambda related constant helpers.

    This data is based on https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
    """
    nodejs14 = "nodejs14.x"
    nodejs12 = "nodejs12.x"
    nodejs10 = "nodejs10.x"

    python38 = "python3.8"
    python37 = "python3.7"
    python36 = "python3.6"
    python27 = "python2.7"

    ruby27 = "ruby2.7"
    ruby25 = "ruby2.5"

    java11 = "java11"
    java8amzlinux2 = "java8.al2"
    java8amzlinux1 = "java8"

    go1x = "go1.x"

    dotnet31 = "dotnetcore3.1"
    dotnet21 = "dotnetcore2.1"

    custom_amzlinux2 = "provided.al2"
    custom_amzlinux1 = "provided"
