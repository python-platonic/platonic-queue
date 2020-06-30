from platonic_queue.list import LIFOListQueue


class LIFOFibQueue(LIFOListQueue[int]):
    """Queue for integers."""


def test_put_many():
    queue = LIFOFibQueue()   # type: ignore

    queue.put_many([1, 1, 2, 3])

    assert queue.get() == 3
    assert queue.get() == 2
    assert queue.get() == 1
    assert queue.get() == 1
