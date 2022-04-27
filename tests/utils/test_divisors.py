# flake8: noqa

from typing import List

from oeis.utils import divisors


def test_divisors() -> None:
    expected: List[int] = [1, 2, 251, 502]
    actual: List[int] = divisors(502)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_divisors_of_prime() -> None:
    expected: List[int] = [1, 337]
    actual: List[int] = divisors(337)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
