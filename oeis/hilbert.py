from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A016813")
def hilbert() -> "Iterable[int]":
    """Hilbert numbers."""
    for n in count(start=0):  # pragma: no branch
        yield 4 * n + 1
