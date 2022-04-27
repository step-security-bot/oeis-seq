# flake8: noqa

from oeis.utils import is_perfect


def test_is_perfect() -> None:
    expected: bool = True
    for n in [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]:
        actual: bool = is_perfect(n)
        assert actual is expected


def test_is_not_perfect() -> None:
    expected: bool = False
    for n in [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23]:
        actual: bool = is_perfect(n)
        assert actual is expected
