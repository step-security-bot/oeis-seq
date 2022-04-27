# flake8: noqa

from oeis.utils import sigma


def test_sigma() -> None:
    expected: int = 12
    actual: int = sigma(6)
    assert actual == expected
