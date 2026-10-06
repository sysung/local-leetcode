"""Reference solution.

Use fullmatch with explicit ASCII character classes, then convert captured numeric fields.
Time: O(L). Auxiliary space: O(L), where L is name length.
"""

from __future__ import annotations

import re


def parse_package_name(name: str) -> dict[str, str | int] | None:
    match = re.fullmatch(
        r"([A-Za-z0-9-]+)_([A-Za-z0-9-]+)_([0-9]+)_(PASS|FAIL)_([0-9]+)\.zip",
        name,
    )
    if match is None:
        return None
    group, item, revision, result, timestamp = match.groups()
    return {"group": group, "item": item, "revision": int(revision),
            "result": result, "timestamp": int(timestamp)}
