from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_deficient

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A005100")
def deficient() -> "Iterable[int]":
    """Deficient numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_deficient(n):
            yield n
