# coding=utf-8
from typing import Generator
from math import floor, log2


def polite(n: int) -> Generator[int, None, None]:
    for i in range(2, n):
        yield i + floor(log2(i + log2(i)))
