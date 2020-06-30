import pytest

from tests.test_sqs.fibonacci_queue import FibonacciQueue


def test_init_no_arg():
    with pytest.raises(ValueError, match='Please specify FibonacciQueue.url'):
        FibonacciQueue()
