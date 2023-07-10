# flake8: noqa


from oeis.utils import divisors


def test_divisors() -> None:
    expected: list[int] = [1, 2, 251, 502]
    actual: list[int] = divisors(502)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_divisors_of_prime() -> None:
    expected: list[int] = [1, 337]
    actual: list[int] = divisors(337)
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])
