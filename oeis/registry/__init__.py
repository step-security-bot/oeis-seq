# coding=utf-8
from typing import Callable, Dict, Generic, Iterable, TypeVar

T = TypeVar("T", bound=Callable[[], Iterable[int]])


class OEISRegistry(Generic[T]):
    def __init__(self) -> None:
        self.sequences: Dict[str, T] = {}

    def __getitem__(self, identifier: str) -> T:
        return self.sequences[identifier]

    def register(self, identifier: str) -> Callable[[T], T]:
        def wrapper(func: T) -> T:
            self.sequences[identifier] = func
            return func

        return wrapper


registry: OEISRegistry[Callable[[], Iterable[int]]] = OEISRegistry[
    Callable[[], Iterable[int]]
]()

__all__ = [
    "registry",
    "OEISRegistry",
]
