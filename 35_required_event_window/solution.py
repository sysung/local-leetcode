"""Reference solution.

Track deficits for required event types and the total number of missing occurrences.
Extend the right edge and shrink the left edge while the window qualifies. Each index
enters and leaves once. Update the best only for a shorter window to keep the earliest
tie. For n events and m required rows, expected time is O(n + m) and auxiliary space is
O(k) for k distinct required types.
"""

from __future__ import annotations

from collections import Counter


def shortest_event_window(events: list[str], required: list[str]) -> tuple[int, int] | None:
    if not required:
        return (0, 0)
    needed = Counter(required)
    missing = len(required)
    left = 0
    best = None
    for right, event in enumerate(events):
        if event in needed:
            if needed[event] > 0:
                missing -= 1
            needed[event] -= 1
        while missing == 0:
            candidate = (left, right + 1)
            if best is None or candidate[1] - candidate[0] < best[1] - best[0]:
                best = candidate
            outgoing = events[left]
            left += 1
            if outgoing in needed:
                needed[outgoing] += 1
                if needed[outgoing] > 0:
                    missing += 1
    return best
