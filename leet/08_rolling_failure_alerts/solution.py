"""Reference solution.

Keep failures in a global timestamp-ordered deque and maintain per-device counts in a hash map. Each failure is inserted and evicted once.

Time: O(n). Auxiliary space: O(w), excluding output, where w is the maximum number of unexpired failures.
"""

from __future__ import annotations
from collections import deque


def failure_alerts(events: list[tuple[int, str, str]], window: int, threshold: int) -> list[tuple[int, str, int]]:
    if window <= 0 or threshold <= 0:
        raise ValueError("window and threshold must be positive")
    recent = deque()
    counts = {}
    alerts = []
    for timestamp, device, status in events:
        while recent and recent[0][0] <= timestamp - window:
            _, expired_device = recent.popleft()
            counts[expired_device] -= 1
            if counts[expired_device] == 0:
                del counts[expired_device]
        if status == "FAIL":
            recent.append((timestamp, device))
            counts[device] = counts.get(device, 0) + 1
        count = counts.get(device, 0)
        if count >= threshold:
            alerts.append((timestamp, device, count))
    return alerts
