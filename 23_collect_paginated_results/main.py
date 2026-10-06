from __future__ import annotations


def collect_pages(pages: dict[str, tuple[list[tuple[str, int]], str | None]], start_cursor: str | None) -> list[tuple[str, int]]:
    """Collect items until the cursor chain ends, goes missing, or repeats."""
    visited = set()
    values = {}

    def visit(cursor):
        if cursor not in pages or cursor in visited:
            return

        visited.add(cursor)
        items, next_cursor = pages[cursor]

        for item_id, value in items:
            values[item_id] = value

        visit(next_cursor)

    visit(start_cursor)
    return list(values.items())


if __name__ == "__main__":
    Pages = dict[str, tuple[list[tuple[str, int]], str | None]]

    args: tuple[Pages, str | None] = ({'p': ([('x', 1)], 'missing')}, 'p')
    expected = [('x', 1)]
    actual = collect_pages(*args)
    print(expected == actual, actual)
