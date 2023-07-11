from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A001045")
def jacobsthal() -> "Iterable[int]":
    """Jacobsthal sequence (or Jacobsthal numbers)."""
    yield 0  # special case
    yield 1  # special case
    prev: int = 0  # initially set to jacobsthal(0)
    curr: int = 1  # initially set to jacobsthal(1)
    while True:
        prev, curr = curr, curr + 2 * prev
        yield curr
