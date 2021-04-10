from oeis.leonardo import leonardo
from typing import List

from oeis import (
    __version__,
    fib,
    jacobsthal,
    lazy_caterer,
    leonardo,
    lucas,
    padovan,
    polite,
    sylvester,
)


def test_fibonacci() -> None:
    expected: List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    actual: List[int] = [i for i in fib(9)]
    assert actual == expected


def test_jacobsthal() -> None:
    expected: List[int] = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]
    actual: List[int] = [i for i in jacobsthal(9)]
    assert actual == expected


def test_lazy_caterer() -> None:
    expected: List[int] = [1, 2, 4, 7, 11, 16, 22, 29, 37]
    actual: List[int] = [i for i in lazy_caterer(9)]
    assert actual == expected


def test_leonardo() -> None:
    expected: List[int] = [1, 1, 3, 5, 9, 15, 25, 41, 67]
    actual: List[int] = [i for i in leonardo(9)]
    assert actual == expected


def test_lucas() -> None:
    expected: List[int] = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
    actual: List[int] = [i for i in lucas(9)]
    assert actual == expected


def test_padovan() -> None:
    expected: List[int] = [1, 1, 1, 2, 2, 3, 4, 5, 7]
    actual: List[int] = [i for i in padovan(9)]
    assert actual == expected


def test_polite() -> None:
    expected: List[int] = [3, 5, 6, 7, 9, 10, 11, 12]
    actual: List[int] = [i for i in polite(9)]
    assert actual == expected


def test_sylvester() -> None:
    expected: List[int] = [
        2,
        3,
        7,
        43,
        1807,
        3263443,
        10650056950807,
        113423713055421844361000443,
        12864938683278671740537145998360961546653259485195807,
    ]
    actual: List[int] = [i for i in sylvester(9)]
    assert actual == expected
