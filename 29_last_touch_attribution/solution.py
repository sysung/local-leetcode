"""Reference solution.

Keep the smallest campaign for each user and touch timestamp. Binary search the sorted
timestamps for each conversion. For t touches and c conversions, time is O(t log(t + 1)
+ c log(t + 1) + c log(c + 1)) and auxiliary space is O(t + c), excluding the output.
"""

from __future__ import annotations

from bisect import bisect_right


def attribute_last_touch(touches: list[tuple[str, int, str]], conversions: list[tuple[str, str, int]], lookback: int) -> list[tuple[str, str | None]]:
    by_user = {}
    for user, timestamp, campaign in touches:
        at_time = by_user.setdefault(user, {})
        if timestamp not in at_time or campaign < at_time[timestamp]:
            at_time[timestamp] = campaign
    timelines = {user: sorted(at_time) for user, at_time in by_user.items()}
    result = []
    for conversion, user, timestamp in conversions:
        times = timelines.get(user, [])
        index = bisect_right(times, timestamp) - 1
        campaign = None
        if index >= 0 and times[index] >= timestamp - lookback:
            campaign = by_user[user][times[index]]
        result.append((conversion, campaign))
    result.sort()
    return result
