# coding=utf-8
from typing import Generator


def padovan(n: int) -> Generator[int, None, None]:
    yield 1  # padovan(0)
    yield 1  # padovan(1)
    yield 1  # padovan(2)
    p = [1, 1, 1]
    for i in range(3, n):
        p.append(p[i - 2] + p[i - 3])
        yield p[-1]
