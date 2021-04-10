# coding=utf-8
from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0:
        yield 1  # special case
    a: int = 0  # initially set to fib(0)
    b: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        a, b = b, a + b
        yield b  # main generation step
