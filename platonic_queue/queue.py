from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Iterable

T = TypeVar('T')  # noqa: WPS111


class Queue(ABC, Generic[T]):
    """Acknowledgement Queue."""

    @abstractmethod
    def serialize(self, instance: T) -> str:
        """Convert arbitrary value to a string."""

    @abstractmethod
    def deserialize(self, serialized_string: str) -> T:
        """Convert a serialized value received over the wire to an instance."""

    @abstractmethod
    def put(self, instance: T) -> None:
        """Put a message into the queue."""

    def put_many(self, iterable: Iterable[T]) -> None:
        """Put multiple messages into the queue."""
        for instance in iterable:
            self.put(instance)

    @abstractmethod
    def get(self) -> T:
        """Get next instance from queue."""
