# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register(identifier="A000215")
def fermat() -> Iterable[int]:
    """Fermaat numbers."""
    for n in count(start=0):
        yield pow(2, pow(2, n)) + 1
