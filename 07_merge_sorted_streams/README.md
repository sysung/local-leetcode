---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-11-15
---
# Merge Sorted Hardware Event Streams

**Difficulty:** Medium
**DSA skills:** Min-heaps, k-way merging, list indices

## Problem

You are given `streams`, a list of lists. Each inner list contains `(timestamp, event_id)` tuples sorted by timestamp.

Return a new list containing all events in timestamp order.

```python
def merge_streams(streams: list[list[tuple[int, str]]]) -> list[tuple[int, str]]:
    ...
```

- For equal timestamps, choose the event from the lower-indexed input stream first.
- Preserve each stream's internal order; event IDs do not affect sorting.
- Inputs and output are ordinary lists; no generators or iterator behavior is required.
- Do not modify the input lists. Empty input, or only empty inner lists, returns `[]`.
- Use a heap to merge the already sorted lists, keeping at most one candidate per nonempty list.
- Target O(s + n log(s + 1)) time for s lists and n total events. Heap storage is O(s); the returned list adds O(n), so total extra space is O(s + n).

## Example 1

Input (positional arguments):

```python
([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
```

Output:

```python
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

**Explanation:** The first stream contains timestamps `1, 4`, and the second contains `2, 3`. In combined timestamp order, the events are `a` at `1`, `b` at `2`, `c` at `3`, and `d` at `4`. Return these events together in a list.

## Example 2

Input (positional arguments):

```python
([[(1, 'z'), (1, 'y')], [(1, 'a')]],)
```

Output:

```python
[(1, 'z'), (1, 'y'), (1, 'a')]
```

**Explanation:** All events have timestamp `1`, so the stream index breaks the tie. Both events from stream `0` come before the event from stream `1`. Preserve stream `0`'s internal order: `z`, then `y`, then `a`. Event IDs do not determine the order.

## Constraints

At most 1,000 streams and 100,000 total events. Each input stream is sorted by timestamp; each event is a valid tuple.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. An unfinished implementation may fail until you complete it. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
