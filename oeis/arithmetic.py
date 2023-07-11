from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import divisors, sigma

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A003601")
def arithmetic() -> "Iterable[int]":
    """Arithmetic numbers."""
    for n in count(start=1):  # pragma: no branch
        div: list[int] = divisors(n)
        s: int = sigma(n)
        if not s % len(div):
            yield n
