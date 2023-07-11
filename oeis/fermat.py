from itertools import count
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register(identifier="A000215")
def fermat() -> "Iterable[int]":
    """Fermaat numbers."""
    for n in count(start=0):  # pragma: no branch
        yield pow(2, pow(2, n)) + 1
