# flake8: noqa

from typing import List

from oeis.utils import proper_divisors


def test_divisors() -> None:
    expected: List[int] = [1, 2, 251]
    actual: List[int] = proper_divisors(502)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
