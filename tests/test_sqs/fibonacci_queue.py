from platonic_queue.sqs import SQSBaseQueue


class FibonacciQueue(SQSBaseQueue[int]):
    """Queue to store Fibonacci numbers."""

    serialize = str     # type: ignore
    deserialize = int   # type: ignore
