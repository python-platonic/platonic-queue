import boto3
from boto3_type_annotations.sqs import Client as SQSClient
from moto import mock_sqs

from tests.test_sqs.fibonacci_queue import FibonacciQueue


@mock_sqs
def test_moto_put():
    client: SQSClient = boto3.client('sqs')
    sqs_queue = client.create_queue(QueueName='mock')

    url = sqs_queue['QueueUrl']

    queue = FibonacciQueue(url=url)
    queue.put_many([1, 1, 2, 3, 5, 8, 13, 21])

    response = client.receive_message(
        QueueUrl=url,
    )

    assert response['Messages'][0]['Body'] == '1'
