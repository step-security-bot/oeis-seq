from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A093069")
def kynea() -> "Iterable[int]":
    """Kynea numbers."""
    for n in count(start=1):  # pragma: no branch
        yield pow(pow(2, n) + 1, 2) - 2
