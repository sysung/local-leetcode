"""Reference solution.

Reduce each profile to the greatest `(version, is_delete, value)` rank. The delete flag
outranks any upsert value at the same version. For n changes and k profiles, time is O(n
+ k log(k + 1)) and auxiliary space is O(k), excluding the output.
"""

from __future__ import annotations


def materialize_profiles(changes: list[tuple[str, int, str, str | None]]) -> list[tuple[str, int, str]]:
    winners = {}
    for profile, version, operation, value in changes:
        rank = (version, operation == "delete", "" if value is None else value)
        if profile not in winners or rank > winners[profile]:
            winners[profile] = rank
    return [(profile, version, value)
            for profile, (version, deleted, value) in sorted(winners.items())
            if not deleted]
