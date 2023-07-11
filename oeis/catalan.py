from itertools import count
from math import comb
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000108")
def catalan() -> "Iterable[int]":
    """Catalan numbers."""
    yield 1  # catalan(0)
    for n in count(start=1):  # pragma: no branch
        yield comb(2 * n, n) - comb(2 * n, n - 1)
