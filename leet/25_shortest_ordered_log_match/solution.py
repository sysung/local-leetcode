"""Reference solution.

Track the latest start index for a matched prefix ending at or before the current position. Update prefixes backwards so one event cannot satisfy two required positions. When the final code matches, compare the resulting window with the best. Keeping the latest start minimizes a window for any future ending index.
Time: O(n*m*s), for maximum string length s (O(n*m) with bounded-length codes). Auxiliary space: O(m).
"""

from __future__ import annotations

def shortest_ordered_match(codes: list[str], required: list[str]) -> tuple[int, int] | None:
    if not required:
        return None
    starts = [-1] * len(required)
    best = None
    for end, code in enumerate(codes):
        for index in range(len(required) - 1, -1, -1):
            if code == required[index]:
                if index == 0:
                    starts[index] = end
                elif starts[index - 1] != -1:
                    starts[index] = starts[index - 1]
        if code == required[-1] and starts[-1] != -1:
            start = starts[-1]
            if best is None or (end - start, start) < (best[1] - best[0], best[0]):
                best = (start, end)
    return best
