from collections.abc import Iterable
from itertools import count

from oeis.registry import registry
from oeis.utils import divisors, sigma


@registry.register("A003601")
def arithmetic() -> Iterable[int]:
    """Arithmetic numbers."""
    for n in count(start=1):  # pragma: no branch
        div: list[int] = divisors(n)
        s: int = sigma(n)
        if not s % len(div):
            yield n
