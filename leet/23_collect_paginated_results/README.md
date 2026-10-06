---
type: coding-practice
difficulty: medium
created: 2026-10-05
updated: 2026-10-05
---
# Collect a Paginated Result Chain

**Difficulty:** Medium  
**DSA skills:** Linked traversal, cycle detection, ordered hash maps

## Problem

A dictionary maps each cursor string to `(items, next_cursor)`. Items is a list of `(item_id, value)` tuples; next_cursor is another cursor or `None`, marking the end. Starting from `start_cursor`, follow the chain and return one tuple per distinct item ID. Preserve the order in which IDs are first encountered, but use the last encountered value for each ID. An empty page may still point to another page. Return `[]` when start_cursor is `None`. Raise `ValueError` if a followed cursor is missing or if the chain revisits a cursor. Ignore unreachable pages, including any errors in their links. An empty string is a valid cursor and must not be treated as end-of-chain. No network requests are needed.

## Function signature

```python
def collect_pages(pages: dict[str, tuple[list[tuple[str, int]], str | None]], start_cursor: str | None) -> list[tuple[str, int]]:
    ...
```

## Example 1

Input (positional arguments):

```python
({'p1': ([('b', 1), ('a', 2)], 'p2'), 'p2': ([('b', 9), ('c', 3)], None)}, 'p1')
```

Output:

```python
[('b', 9), ('a', 2), ('c', 3)]
```

**Explanation:** Updating b changes its value but keeps its first-seen position.

## Example 2

Input (positional arguments):

```python
({'p1': ([], 'p2'), 'p2': ([('x', 1)], None)}, 'p1')
```

Output:

```python
[('x', 1)]
```

**Explanation:** An empty page does not terminate traversal.

## Constraints

At most 100,000 pages and 200,000 items across all pages. Cursors and item IDs are strings. Values are integers. Page tuples and item tuples have the stated structure.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
