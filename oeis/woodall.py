from itertools import count
from typing import TYPE_CHECKING

from .registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A003261")
def woodall() -> "Iterable[int]":
    """Woodall (or Riesel) numbers."""
    for n in count(start=1):  # pragma: no branch
        yield n * (2**n) - 1
