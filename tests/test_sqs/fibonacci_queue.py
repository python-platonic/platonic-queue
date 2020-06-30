from platonic_queue.sqs import SQSInputOutputQueue


class FibonacciQueue(SQSInputOutputQueue[int]):
    """Queue to store Fibonacci numbers."""

    serialize = str     # type: ignore
    deserialize = int   # type: ignore
