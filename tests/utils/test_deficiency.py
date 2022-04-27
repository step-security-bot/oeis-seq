# flake8: noqa

from oeis.utils import is_deficient


def test_is_not_deficient() -> None:
    expected: bool = False
    for n in [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78]:
        actual: bool = is_deficient(n)
        assert actual is expected


def test_is_deficient() -> None:
    expected: bool = True
    for n in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23]:
        actual: bool = is_deficient(n)
        assert actual is expected
