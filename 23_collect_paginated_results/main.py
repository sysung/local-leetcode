from __future__ import annotations


def collect_pages(pages: dict[str, tuple[list[tuple[str, int]], str | None]], start_cursor: str | None) -> list[tuple[str, int]]:
    """Collect items until the cursor chain ends, goes missing, or repeats."""
    visited: set[str] = set()
    items_by_id: dict[str, int] = {}
    cursor = start_cursor

    while cursor is not None and cursor in pages and cursor not in visited:
        visited.add(cursor)
        items, next_cursor = pages[cursor]
        for item_id, value in items:
            # Updating a value preserves the ID's first-seen position.
            items_by_id[item_id] = value
        cursor = next_cursor

    return list(items_by_id.items())


if __name__ == "__main__":
    Pages = dict[str, tuple[list[tuple[str, int]], str | None]]

    args: tuple[Pages, str | None] = ({'p': ([('x', 1)], 'missing')}, 'p')
    expected = [('x', 1)]
    actual = collect_pages(*args)
    print(expected == actual, actual)
