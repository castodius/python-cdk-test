from os import getenv

import boto3

sqs = boto3.client('sqs')
queue_url = getenv('queue_url')


def handler(event, context):
  sqs.send_message(QueueUrl=queue_url, MessageBody='oh boy')

  if 'name' in event:
    return 'Hello {}'.format(event['name'])
  else:
    return 'Hello whoever you are! :)'
