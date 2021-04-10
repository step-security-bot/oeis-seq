# coding=utf-8
from typing import Generator


def lucas(n: int) -> Generator[int, None, None]:
    yield 2  # special case
    if n > 0:
        yield 1  # special case
    a: int = 2  # initially set to lucas(0)
    b: int = 1  # initially set to lucas(1)
    for _ in range(1, n):
        a, b = b, a + b
        yield b  # main generation step
