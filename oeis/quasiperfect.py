from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_quasiperfect

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A088831")
def quasiperfect() -> "Iterable[int]":
    """Quasiperfect numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_quasiperfect(n):
            yield n
