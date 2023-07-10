# flake8: noqa


from hypothesis import given
from hypothesis.strategies import integers

from oeis.utils import is_prime, prime_factors


def test_prime_factors() -> None:
    expected: list[int] = [3, 3, 5, 7]
    actual: list[int] = prime_factors(315)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


@given(integers(min_value=2, max_value=100000))
def test_all_factors_are_prime(n: int) -> None:
    factors: list[int] = prime_factors(n)
    assert all([is_prime(a) for a in factors])
