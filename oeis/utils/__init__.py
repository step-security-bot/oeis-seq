# coding=utf-8
"""Various utility functions."""
from functools import lru_cache
from math import gcd, isqrt
from random import randrange
from typing import List, Set

__all__ = [
    "aliquot_sum",
    "coprime",
    "divisors",
    "proper_divisors",
    "sigma",
]


def aliquot_sum(n: int) -> int:
    """Return the aliquot sum of n - s(n)."""
    return sum(proper_divisors(n))


def coprime(a: int, b: int) -> bool:
    """Determine whether a and b are coprime."""
    return gcd(a, b) == 1


@lru_cache
def divisors(n: int) -> List[int]:
    """Return the divisors of n."""
    ret: Set[int] = set()
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    return sorted(ret)


def _is_composite(a: int, d: int, n: int, s: int) -> bool:
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


def is_prime(n: int, k: int = 8) -> bool:
    """
    Miller-Rabin primality test.

    Args:
            n: Number to test.
            k: Optional number of rounds, default 8.
    """
    if n in [0, 1, 4, 6, 8, 9]:
        return False
    if n in [2, 3, 5, 7]:
        return True
    s: int = 0
    d: int = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = randrange(2, n)
        if _is_composite(a, d, n, s):
            return False

    return True


@lru_cache
def proper_divisors(n: int) -> List[int]:
    """Return the proper divisors of n."""
    return divisors(n)[:-1]


def sigma(n: int) -> int:
    """Return the sum of the positive divisors of n, including 1 and n itself."""
    return sum(divisors(n))
