from itertools import cycle
from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000035")
def period2() -> "Iterable[int]":
    """Period 2: repeat [0, 1]."""
    return cycle([0, 1])
