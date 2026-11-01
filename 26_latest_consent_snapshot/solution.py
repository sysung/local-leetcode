"""Reference solution.

Keep the greatest `(timestamp, revoked)` rank per user and purpose. Boolean ordering
makes a revocation win a timestamp tie. If n is the number of events and k is the number
of eligible pairs, time is O(n + k log(k + 1)) and auxiliary space is O(k), excluding
the output.
"""

from __future__ import annotations


def latest_consent(events: list[tuple[str, str, int, bool]], as_of: int) -> list[tuple[str, str, int, bool]]:
    latest = {}
    for user, purpose, timestamp, granted in events:
        if timestamp > as_of:
            continue
        key = (user, purpose)
        rank = (timestamp, not granted)
        if key not in latest or rank > latest[key]:
            latest[key] = rank
    return [(user, purpose, timestamp, not revoked)
            for (user, purpose), (timestamp, revoked) in sorted(latest.items())]
