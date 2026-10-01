"""Reference solution.

Count occurrences using a hash map, then sort distinct codes by negative count and code.

Time: O(n + u log u). Auxiliary space: O(u), for u distinct codes.
"""

from __future__ import annotations
from collections import Counter


def top_failure_codes(codes: list[str], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    counts = Counter(codes)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
