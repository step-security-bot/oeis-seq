from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A001595")
def leonardo() -> "Iterable[int]":
    """Leonardo numbers."""
    yield 1  # leonardo(0)
    yield 1  # leonardo(1)
    prev: int = 1
    curr: int = 1
    while True:
        prev, curr = curr, curr + prev + 1
        yield curr
