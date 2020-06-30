import pytest

from platonic_queue.chunkify import chunkify


@pytest.mark.parametrize(('actual', 'expected'), [
    (chunkify([], 5), []),
    (chunkify([1, 2, 3], 5), [[1, 2, 3]]),
    (chunkify([1, 2, 3], 3), [[1, 2, 3]]),
    (chunkify([1, 2, 3], 2), [[1, 2], [3]]),
])
def test_chunkify(actual, expected):
    assert list(actual) == expected
