"""Reference solution.

For each canonical field, inspect its aliases in priority order using key membership.
Time: O(n). Auxiliary space: O(1) excluding O(n) output dictionaries.
"""

from __future__ import annotations

def normalize_records(records: list[dict[str, object]]) -> list[dict[str, object]]:
    aliases = {"item_id": ("item_id", "id"),
               "timestamp": ("timestamp", "time"),
               "status": ("status", "result")}
    output = []
    for record in records:
        normalized = {}
        for field, names in aliases.items():
            normalized[field] = next((record[name] for name in names if name in record), None)
        output.append(normalized)
    return output
