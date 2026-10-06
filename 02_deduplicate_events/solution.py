"""Reference solution.

Index the newest record by event ID. Using >= makes a later occurrence win a timestamp tie. Sort only the distinct IDs.

Time: O(n + u log u). Auxiliary space: O(u), excluding output, for n records and u distinct IDs.
"""

from __future__ import annotations
from typing import Any


def deduplicate_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest = {}
    for event in events:
        event_id = event["event_id"]
        if event_id not in latest or event["timestamp"] >= latest[event_id]["timestamp"]:
            latest[event_id] = event
    return [latest[event_id].copy() for event_id in sorted(latest)]
