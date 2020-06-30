import uuid
from functools import cached_property
from typing import Generic, Iterable, List, Optional, TypedDict, TypeVar

import boto3
from boto3_type_annotations.sqs import Client as SQSClient

# We only can send 10 messages at once to SQS.
from platonic_queue.queue import Queue

MAX_ENTRIES_PER_BATCH = 10

T = TypeVar('T')  # noqa: WPS111


def chunkify(lst: Iterable[T], chunk_size: int) -> Iterable[List[T]]:
    """Split list into chunks of size not larger than the given number."""
    chunk = []
    for item in lst:  # noqa: WPS110
        chunk.append(item)

        if len(chunk) >= chunk_size:
            yield chunk
            chunk = []

    if chunk:
        yield chunk


class SQSMessage(TypedDict):
    """Representation of SQS message."""

    Id: str   # noqa: WPS115
    MessageBody: str  # noqa: WPS115


class SQSQueue(Queue[T]):
    """SQS Queue wrapper."""

    url: str

    def __init__(self, url: Optional[str] = None):
        if url is not None:
            self.url = url

        if not self.url:
            raise ValueError(f'{self}.url is not specified.')

    @cached_property
    def client(self) -> SQSClient:
        """Create boto3 SQS client."""
        return boto3.client('sqs')

    def serialize(self, value: T) -> str:   # noqa: WPS110
        """Convert arbitrary value to a string."""
        return value  # type: ignore

    def create_message_id(self) -> str:
        """Unique SQS message id."""
        return uuid.uuid4().hex

    def generate_message(self, serialized_object: str) -> SQSMessage:
        """Create an SQS message from a string."""
        return SQSMessage(
            Id=self.create_message_id(),
            MessageBody=serialized_object,
        )

    def put_many(self, objects: Iterable[T]):  # noqa: WPS110
        """Send multiple objects to SQS queue."""
        serialized_objects = map(self.serialize, objects)

        messages = map(self.generate_message, serialized_objects)

        # We only can send MAX_ENTRIES_PER_BATCH messages at once.
        chunks = chunkify(messages, MAX_ENTRIES_PER_BATCH)

        for chunk in chunks:
            self.client.send_message_batch(
                QueueUrl=self.url,
                Entries=chunk,
            )
