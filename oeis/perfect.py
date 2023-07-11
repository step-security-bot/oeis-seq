from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_perfect

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000396")
def perfect() -> "Iterable[int]":
    """Perfect numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_perfect(n):
            yield n
