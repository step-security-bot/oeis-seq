# flake8: noqa


from hypothesis import given
from hypothesis.strategies import integers

from oeis.utils import divisors, is_prime


@given(integers(min_value=2, max_value=1000000))
def test_prime_property(n: int) -> None:
    if is_prime(n):
        d: list[int] = divisors(n)
        assert len(d) == 2
        assert d[0] == 1
        assert d[1] == n
