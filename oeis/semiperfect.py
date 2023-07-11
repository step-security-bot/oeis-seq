from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_semiperfect

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A005835")
def semiperfect() -> "Iterable[int]":
    """Semiperfect numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_semiperfect(n):
            yield n
