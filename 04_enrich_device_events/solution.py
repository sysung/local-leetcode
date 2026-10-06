"""Reference solution.

Build a hash index over metadata once, then look up each event in expected constant time. Construct new event dictionaries.

Time: O(m + n) for fixed-width records. Auxiliary space: O(u), excluding output, for u distinct metadata IDs.
"""

from __future__ import annotations
from typing import Any


def enrich_events(events: list[dict[str, Any]], devices: list[dict[str, str]]) -> list[dict[str, Any]]:
    metadata = {device["device_id"]: device for device in devices}
    enriched = []
    for event in events:
        device = metadata.get(event["device_id"])
        enriched.append({**event, "model": device["model"] if device else None,
                         "site": device["site"] if device else None})
    return enriched
