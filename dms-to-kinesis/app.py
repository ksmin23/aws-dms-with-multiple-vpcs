#!/usr/bin/env python3
import os
import json

import boto3

import aws_cdk as cdk

from cdk_stacks.vpc import VpcStack
from cdk_stacks.kds import KinesisDataStreamStack
from cdk_stacks.dms_aurora_mysql_to_kinesis import DMSAuroraMysqlToKinesisStack

app = cdk.App()

vpc_stack = VpcStack(app, 'DMSVpcStack',
  env=cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))

kds_stack = KinesisDataStreamStack(app, 'DMSTargetKinesisDataStreamStack')

dms_stack = DMSAuroraMysqlToKinesisStack(app, 'DMSAuroraMysqlToKinesisStack',
  vpc_stack.vpc,
  kds_stack.kinesis_stream_arn
)

app.synth()
