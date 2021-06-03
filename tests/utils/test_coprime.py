# coding=utf-8
from hypothesis import given
from hypothesis.strategies import integers

from oeis.utils import coprime
from math import lcm


@given(a=integers(min_value=2, max_value=100), b=integers(min_value=2, max_value=100))
def test_lcm_property(a: int, b: int) -> None:
    if coprime(a, b):
        assert lcm(a, b) == a * b
