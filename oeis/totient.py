from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

from .utils import coprime

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000010")
def totient() -> "Iterable[int]":
    """Euler totient function."""
    yield 1  # totient(0)
    for n in count(start=2):  # pragma: no branch
        totients: list[bool] = [coprime(n, p) for p in range(1, n)]
        yield totients.count(True)
