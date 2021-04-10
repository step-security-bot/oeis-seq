# coding=utf-8
from typing import Generator


def sylvester(n: int) -> Generator[int, None, None]:
    yield 2  # sylvester(0)
    s = [2]
    for i in range(1, n):
        s.append(s[i - 1] * (s[i - 1] - 1) + 1)
        yield s[-1]
