# coding=utf-8
from typing import Generator


def lazy_caterer(n: int) -> Generator[int, None, None]:
    yield 1  # special case
    if n > 0:
        yield 2  # special case
    for i in range(2, n):
        yield ((i * i) + i + 2) // 2
