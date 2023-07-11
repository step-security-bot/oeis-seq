from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000124")
def lazy_caterer() -> "Iterable[int]":
    """Central polygonal numbers (the Lazy Caterer's sequence)."""
    yield 1  # special case
    yield 2  # special case
    for i in count(start=2):  # pragma: no branch
        yield ((i * i) + i + 2) // 2
