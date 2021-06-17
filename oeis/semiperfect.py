# coding=utf-8
from itertools import combinations, count
from typing import Iterable, List, Set

from oeis.registry import registry
from oeis.utils import proper_divisors


@registry.register("A005835")
def semiperfect() -> Iterable[int]:
    """Semiperfect numbers."""
    found: Set[int] = set()
    for n in count(start=1):
        pd: List[int] = proper_divisors(n)
        l: int = len(pd)
        for i in range(l + 1):
            comb = combinations(pd, i)
            for c in comb:
                if sum(c) == n and n not in found:
                    yield n
                    found.add(n)
