# coding=utf-8
from itertools import count
from math import sqrt
from typing import Iterable, List

from oeis.registry import registry

from .utils import prime_factors


@registry.register("A064052")
def unusual() -> Iterable[int]:
    """Unusual numbers, aka sqrt(n)-rough numbers."""
    for n in count(start=2):
        factors: List[int] = prime_factors(n)
        gpf = max(factors)
        if gpf > sqrt(n):
            yield n
