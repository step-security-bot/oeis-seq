from collections.abc import Iterable
from itertools import count

from oeis.registry import registry


@registry.register("A006564")
def icosahedral() -> Iterable[int]:
    """Icoseahedral numbers."""
    for n in count(start=1):  # pragma: no branch
        yield (n * (5 * (n**2) - (5 * n) + 2)) // 2
