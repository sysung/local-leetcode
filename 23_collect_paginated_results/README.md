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

**Explanation:** Start at `p1`, collecting `b = 1` and `a = 2` in that order. Follow its cursor to `p2`, where `b` changes to `9` and new ID `c` is appended with value `3`. Updating `b` preserves its first-seen position. The next cursor is `None`, so stop with ID order `b`, `a`, `c`.

## Example 2

Input (positional arguments):

```python
({'p1': ([], 'p2'), 'p2': ([('x', 1)], None)}, 'p1')
```

Output:

```python
[('x', 1)]
```

**Explanation:** Start at `p1`, which contains no items but points to `p2`. Continue to `p2` and collect `('x', 1)`. Its next cursor is `None`, so stop. An empty page alone does not end the cursor chain.

## Example 3

Input (positional arguments):

```python
({}, 'missing')
```

Output:

```python
[]
```

**Explanation:** The start cursor does not exist, so no items are collected.

## Example 4

Input (positional arguments):

```python
({'p1': ([('x', 1)], 'missing')}, 'p1')
```

Output:

```python
[('x', 1)]
```

**Explanation:** Collect the items from `p1`, then stop because the next cursor is missing. Return the collected items without raising an error.

## Example 5

Input (positional arguments):

```python
({'p1': ([('b', 1), ('a', 2)], 'p2'), 'p2': ([('b', 9), ('c', 3)], 'p1')}, 'p1')
```

Output:

```python
[('b', 9), ('a', 2), ('c', 3)]
```

**Explanation:** Visit `p1` and `p2` once, then stop before revisiting `p1`. The later value of `b` is kept, and the collected items are returned without raising an error.

## Constraints

At most 100,000 pages and 200,000 items across all pages. Cursors and item IDs are strings. Values are integers. Page tuples and item tuples have the stated structure.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
