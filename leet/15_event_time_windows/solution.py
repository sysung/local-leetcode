"""Reference solution.

Use a hash map for each open (window, device) bucket and a min-heap ordered by window end and device. Advance the watermark after accepted events, evict finalized buckets, then flush the heap at end of input. The heap makes output ordering deterministic without retaining finalized aggregation state.

Time: O(n log(b + 1)), where b is the maximum number of open device-window buckets. Auxiliary space: O(b), excluding returned summaries and rejected indices.
"""

from __future__ import annotations
from collections.abc import Iterable
import heapq


def aggregate_event_time(events: Iterable[tuple[int, str, str]], window_size: int, allowed_lateness: int) -> tuple[list[tuple[int, str, int, int]], list[int]]:
    if window_size <= 0 or allowed_lateness < 0:
        raise ValueError("window size must be positive and lateness nonnegative")
    maximum = 0
    watermark = float("-inf")
    open_windows = {}
    endings = []
    summaries = []
    rejected = []

    def finalize(up_to):
        while endings and endings[0][0] <= up_to:
            _, start, device = heapq.heappop(endings)
            total, failures = open_windows.pop((start, device))
            summaries.append((start, device, total, failures))

    for index, (timestamp, device, status) in enumerate(events):
        if timestamp < 0:
            raise ValueError("timestamps must be nonnegative")
        if timestamp < watermark:
            rejected.append(index)
            continue
        start = timestamp // window_size * window_size
        key = (start, device)
        if key not in open_windows:
            open_windows[key] = [0, 0]
            heapq.heappush(endings, (start + window_size, start, device))
        counts = open_windows[key]
        counts[0] += 1
        counts[1] += status == "FAIL"
        maximum = max(maximum, timestamp)
        watermark = maximum - allowed_lateness
        finalize(watermark)
    finalize(float("inf"))
    return summaries, rejected
