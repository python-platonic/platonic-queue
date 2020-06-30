from typing import TypeVar, Generic

T = TypeVar('T')  # noqa: WPS111


class Queue(Generic[T]):
    """Acknowledgement Queue."""

