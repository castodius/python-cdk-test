#!/usr/bin/env python3
from aws_cdk import App
from src.dummy_stack import DummyStack

app = App()

DummyStack(
  app,
  'MyStack',
  stack_name='python-cdk-test',
  description='Trying out the CDK and Python',
  analytics_reporting=False,
)

app.synth()
