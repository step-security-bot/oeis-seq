# coding=utf-8
from math import gcd

from hypothesis import given
from hypothesis.strategies import integers
from oeis.utils import coprime


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


@given(a=integers(), b=integers())
def test_lcm_property(a: int, b: int) -> None:
    if coprime(a, b):
        assert lcm(a, b) == a * b
