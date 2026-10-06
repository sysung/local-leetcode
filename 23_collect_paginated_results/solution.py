"""Reference solution.

Follow cursor links with a visited set; collect last values in an insertion-ordered dictionary. Updating an existing Python dictionary key preserves its position.
Time: O(p + m), for p followed pages and m encountered items. Auxiliary space: O(p + u), for u distinct encountered IDs.
"""

from __future__ import annotations

def collect_pages(pages: dict[str, tuple[list[tuple[str, int]], str | None]], start_cursor: str | None) -> list[tuple[str, int]]:
    seen = set()
    values = {}
    cursor = start_cursor
    while cursor is not None:
        if cursor in seen or cursor not in pages:
            raise ValueError("Repeated or missing cursor")
        seen.add(cursor)
        items, cursor = pages[cursor]
        for item_id, value in items:
            values[item_id] = value
    return list(values.items())
