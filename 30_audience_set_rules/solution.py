"""Reference solution.

Intersect a fresh universe set with each required group, subtract excluded IDs, and
sort. For n total input IDs, g required groups, and k surviving IDs, expected time is
O(n + g + k log(k + 1)). Auxiliary space is O(n), excluding the output, because set
intersection may construct a temporary group set.
"""

from __future__ import annotations


def build_audience(universe: list[str], required_groups: list[list[str]], excluded: list[str]) -> list[str]:
    eligible = set(universe)
    for group in required_groups:
        eligible.intersection_update(group)
    eligible.difference_update(excluded)
    return sorted(eligible)
