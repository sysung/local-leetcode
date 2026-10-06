---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Merge Sorted Hardware Event Streams

**Difficulty:** Medium  
**DSA skills:** Min-heaps, k-way merging, iterators

## Problem

You are given a list of streams, `streams`. Each stream contains `(timestamp, event_id)` tuples sorted by timestamp.

Return an iterator that yields all events in timestamp order.

- For equal timestamps, choose the event from the lower-indexed input stream first.
- Preserve each stream's internal order; event IDs do not affect sorting.
- Read streams incrementally, buffering at most one event per stream.
- Consuming input iterators is allowed, but do not modify input collections.

## Example 1

Input (positional arguments):

```python
([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
```

Output:

```python
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

**Explanation:** Choose the next smallest timestamp across stream heads.

## Example 2

Input (positional arguments):

```python
([[(1, 'z'), (1, 'y')], [(1, 'a')]],)
```

Output:

```python
[(1, 'z'), (1, 'y'), (1, 'a')]
```

**Explanation:** Stream zero wins both timestamp ties, even though its IDs sort later.

## Constraints

At most 1,000 streams and 100,000 total events. Each input stream is sorted by timestamp; each event is a valid tuple.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
