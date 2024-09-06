import os

from aws_cdk import Duration, Stack
from aws_cdk.aws_sqs import Queue
from aws_cdk.aws_ssm import StringParameter
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk.aws_iam import PolicyStatement, Effect
from constructs import Construct


class DummyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    queue = Queue(
      self,
      'Queue',
      visibility_timeout=Duration.seconds(300),
    )

    StringParameter(self, 'Parameter', string_value=queue.queue_arn)

    fun = PythonFunction(
      self,
      'Function',
      entry=os.path.dirname(os.path.abspath(__file__)) + '/' + './fun',
      runtime=Runtime.PYTHON_3_9,
      index='index.py',
      handler='handler',
      environment={
        'queue_name': queue.queue_name,
        'queue_url': queue.queue_url,
      },
    )
    fun.add_to_role_policy(
      PolicyStatement(
        effect=Effect.ALLOW, actions=['sqs:SendMessage'], resources=[queue.queue_arn]
      )
    )
