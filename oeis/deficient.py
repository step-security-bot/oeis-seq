# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import sigma


@registry.register("A005100")
def deficient() -> Iterable[int]:
    """Deficient numbers."""
    for n in count(start=1):
        s: int = sigma(n)
        if s < 2 * n:
            yield n
