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

You are given a dictionary of `pages` and a `start_cursor`. Each page maps a cursor to `(items, next_cursor)`, where items are `(item_id, value)` tuples.

Follow the cursor chain and return one tuple per item ID. Keep IDs in the order they first appear, but use each ID's last encountered value.

- Stop when the next cursor is `None`. An empty string is a valid cursor, and empty pages may lead to more pages.
- Return `[]` if `start_cursor` is `None` or does not exist in `pages`.
- If a later cursor is missing or already visited, stop before processing it and return the items collected so far.
- Ignore unreachable pages and their links. No network requests are needed.

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
