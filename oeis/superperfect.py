from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry
from oeis.utils import is_superperfect

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A019279")
def superperfect() -> "Iterable[int]":
    """Perfect numbers."""
    for n in count(start=1):  # pragma: no branch
        if is_superperfect(n):
            yield n
