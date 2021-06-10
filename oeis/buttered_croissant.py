# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register(identifier="A100702")
def buttered_croissant() -> Iterable[int]:
    yield 1  # special case
    for n in count(start=1):
        yield 1 + 2 * pow(3, n - 1)
