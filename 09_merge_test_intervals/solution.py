"""Reference solution.

Sort by starting endpoint. Compare each interval only with the last merged interval, extending its end when they overlap or touch.

Time: O(n log n). Auxiliary space: O(n) for sorting, excluding output.
"""

from __future__ import annotations


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
