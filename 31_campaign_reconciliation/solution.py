"""Reference solution.

Count each event key independently on both sides, then compare the union of keys. For n
total rows and k distinct keys, expected time is O(n + k log(k + 1)) and auxiliary space
is O(k), excluding the output.
"""

from __future__ import annotations

from collections import Counter


def reconcile_campaign_events(source: list[tuple[str, str]], destination: list[tuple[str, str]]) -> list[tuple[str, str, int, int]]:
    source_counts = Counter(source)
    destination_counts = Counter(destination)
    return [(campaign, event, source_counts[(campaign, event)], destination_counts[(campaign, event)])
            for campaign, event in sorted(source_counts.keys() | destination_counts.keys())
            if source_counts[(campaign, event)] != destination_counts[(campaign, event)]]
