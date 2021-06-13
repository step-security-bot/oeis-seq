# coding=utf-8
# flake8: noqa
from typing import Callable, Iterable

from oeis.registry import OEISRegistry


def test_register() -> None:
    registry: OEISRegistry[Callable[[], Iterable[int]]] = OEISRegistry[
        Callable[[], Iterable[int]]
    ]()

    @registry.register(identifier="A000012")
    def one() -> Iterable[int]:
        yield 1

    expected = one
    actual = registry["A000012"]
    assert expected is actual
