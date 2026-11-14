from __future__ import annotations

from collections import Counter


def count_target_ranges(values: list[int], target: int) -> int:
    """Expected O(n) time and O(n) space; include the empty prefix once."""
    frequencies = Counter({0: 1})
    prefix = result = 0
    for value in values:
        prefix += value
        result += frequencies[prefix - target]
        frequencies[prefix] += 1
    return result
