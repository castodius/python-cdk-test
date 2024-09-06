from aws_cdk import App
import aws_cdk.assertions as assertions
from src.dummy_stack import DummyStack


def test_sqs_queue_created():
  app = App()
  stack = DummyStack(app, 'python-cdk-test')
  template = assertions.Template.from_stack(stack)

  template.has_resource_properties('AWS::SQS::Queue', {'VisibilityTimeout': 300})
