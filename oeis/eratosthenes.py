from typing import TYPE_CHECKING

from oeis.registry import registry

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register("A000040")
def eratosthenes() -> "Iterable[int]":
    """Sieve of Eratosthenes."""
    discards: dict[int, list[int]] = {}
    p: int = 2

    while True:
        if p not in discards:
            yield p
            discards[p * p] = [p]
        else:
            for n in discards[p]:
                discards.setdefault(p + n, []).append(n)
            del discards[p]
        p += 1
