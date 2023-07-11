from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000142")
def factorial() -> "Iterable[int]":
    """Factorial numbers."""
    curr: int = 1
    for n in count(start=1):  # pragma: no branch
        yield curr
        curr *= n
