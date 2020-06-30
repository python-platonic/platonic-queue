from platonic_queue.sqs import SQSQueue


class FibonacciQueue(SQSQueue[int]):
    """Queue to store Fibonacci numbers."""

    serialize = str     # type: ignore
    deserialize = int   # type: ignore
