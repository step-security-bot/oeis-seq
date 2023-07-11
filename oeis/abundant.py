from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_abundant

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A005101")
def abundant() -> "Iterable[int]":
    """Abundant numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_abundant(n):
            yield n
