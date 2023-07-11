from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000058")
def sylvester() -> "Iterable[int]":
    """Sylvester's sequence."""
    prev: int = 2  # sylvester(0)
    while True:
        yield prev
        prev = (prev * (prev - 1)) + 1
