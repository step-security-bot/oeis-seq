# flake8: noqa
from itertools import islice
from typing import List

from hypothesis import given
from hypothesis.strategies import integers

from oeis import recaman


@given(integers(min_value=2, max_value=100))
def test_recaman_greater_than_zero(n: int) -> None:
    r: List[int] = list(islice(recaman(), n))
    assert r[n - 1] >= 0


@given(integers(min_value=2, max_value=100))
def test_recaman_property(n: int) -> None:
    r: List[int] = list(islice(recaman(), n))
    assert abs(r[n - 1] - r[n - 2]) == n - 1
