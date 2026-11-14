"""Count, select a bounded best-k set, then order the selected output.

Expected time: O(n + u log(h+1) + h log(h+1)); space: O(u+h).
h = min(max(k, 0), u). String comparisons use the unit-cost assumption.
"""
from __future__ import annotations
from collections import Counter
from heapq import nsmallest


def top_failure_codes(codes: list[str], k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    counts = Counter(codes)
    return nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))
