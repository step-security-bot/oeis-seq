from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_abundant, is_semiperfect

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A006037")
def weird() -> "Iterable[int]":
    """Weird numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_abundant(n) and not is_semiperfect(n):
            yield n
