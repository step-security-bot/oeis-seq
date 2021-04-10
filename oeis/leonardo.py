# coding=utf-8
from typing import Generator


def leonardo(n: int) -> Generator[int, None, None]:
    yield 1  # leonardo(0)
    yield 1  # leonardo(1)
    leo = [1, 1]
    for i in range(2, n):
        leo.append(leo[i - 1] + leo[i - 2] + 1)
        yield leo[-1]
