import pytest

from tests.test_sqs.fibonacci_queue import FibonacciQueue


def test_get_not_implemented():
    with pytest.raises(NotImplementedError, match=''):
        FibonacciQueue(url='boo').get()
