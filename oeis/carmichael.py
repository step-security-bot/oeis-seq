# coding=utf-8
from typing import Iterable

from oeis.registry import registry

from .composite import composite


@registry.register(identifier="A002997")
def carmichael() -> Iterable[int]:
    """Carmichael numbers."""
    for n in composite():
        for a in range(2, n):
            if pow(a, n, n) != a:
                break
        else:
            yield n
