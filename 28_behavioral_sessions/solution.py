"""Reference solution.

Sort by user, timestamp, and event ID. Extend the most recent session or append a new
one when its inactivity gap is too large. For n events, time is O(n log(n + 1)) and
auxiliary space is O(n) for sorting, excluding the output.
"""

from __future__ import annotations


def sessionize(events: list[tuple[str, int, str]], timeout: int) -> list[tuple[str, int, int, int, int]]:
    sessions = []
    for user, timestamp, _ in sorted(events):
        if not sessions or sessions[-1][0] != user:
            sessions.append((user, 1, timestamp, timestamp, 1))
            continue
        _, number, start, end, count = sessions[-1]
        if timestamp - end > timeout:
            sessions.append((user, number + 1, timestamp, timestamp, 1))
        else:
            sessions[-1] = (user, number, start, timestamp, count + 1)
    return sessions
