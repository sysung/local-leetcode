"""Reference solution.

Traverse the document depth first using a stack of dictionary iterators. Extend the path at each edge and emit only scalar leaves.

Time: O(N + P), where N is the number of dictionary entries and P is the sum of constructed path lengths. Auxiliary space: O(h + A), excluding output, for depth h and total ancestor-path characters A retained by stack frames.
"""

from __future__ import annotations
from typing import Any


def flatten_telemetry(record: dict[str, Any]) -> dict[str, Any]:
    flattened = {}
    # Iterator frames keep traversal state proportional to nesting depth.
    stack = [("", iter(record.items()))]
    while stack:
        prefix, children = stack[-1]
        try:
            key, value = next(children)
        except StopIteration:
            stack.pop()
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            stack.append((path, iter(value.items())))
        else:
            flattened[path] = value
    return flattened
