"""Reference solution.

Accumulate +1 at starts and -1 at ends, then scan sorted timestamps. Applying each timestamp's net change handles half-open endpoints and zero-length jobs.
Time: O(n log(n + 1)). Auxiliary space: O(n).
"""

from __future__ import annotations

def peak_concurrency(intervals: list[tuple[int, int]]) -> int:
    changes = {}
    for start, end in intervals:
        changes[start] = changes.get(start, 0) + 1
        changes[end] = changes.get(end, 0) - 1
    active = 0
    peak = 0
    for timestamp in sorted(changes):
        active += changes[timestamp]
        peak = max(peak, active)
    return peak
