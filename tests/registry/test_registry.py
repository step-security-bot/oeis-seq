# flake8: noqa
from collections.abc import Iterable
from typing import Callable

import pytest

from oeis.registry import OEISRegistry


def test_register() -> None:
    registry: OEISRegistry[Callable[[], Iterable[int]]] = OEISRegistry[
        Callable[[], Iterable[int]]
    ]()

    @registry.register(identifier="A000012")
    def one() -> "Iterable[int]":
        yield 1

    expected = one
    actual = registry["A000012"]
    assert expected is actual


def test_duplicate_entries_throw_KeyError() -> None:
    registry: OEISRegistry[Callable[[], Iterable[int]]] = OEISRegistry[
        Callable[[], Iterable[int]]
    ]()

    @registry.register(identifier="A000012")
    def one() -> "Iterable[int]":
        yield 1

    with pytest.raises(KeyError):

        @registry.register(identifier="A000012")
        def two() -> "Iterable[int]":
            yield 1
