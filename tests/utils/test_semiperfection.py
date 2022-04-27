# flake8: noqa

from oeis.utils import is_semiperfect


def test_is_semiperfect() -> None:
    expected: bool = True
    for n in [6, 12, 18, 20, 24, 28, 30, 36, 40, 42, 48, 54, 56, 60, 66, 72, 78, 80]:
        actual: bool = is_semiperfect(n)
        assert actual is expected


def test_is_not_semiperfect() -> None:
    expected: bool = False
    for n in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23]:
        actual: bool = is_semiperfect(n)
        assert actual is expected
