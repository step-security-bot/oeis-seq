from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A006564")
def icosahedral() -> "Iterable[int]":
    """Icoseahedral numbers."""
    for n in count(start=1):  # pragma: no branch
        yield (n * (5 * (n**2) - (5 * n) + 2)) // 2
