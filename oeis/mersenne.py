from typing import TYPE_CHECKING

from oeis.registry import registry

from .eratosthenes import eratosthenes

if TYPE_CHECKING:
    from collections.abc import Iterable


@registry.register(identifier="A001348")
def mersenne() -> "Iterable[int]":
    """Mersenne numbers."""
    for n in eratosthenes():  # pragma: no branch
        yield pow(2, n) - 1
