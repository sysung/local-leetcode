---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-09-30
---
# Merge Sorted Hardware Event Streams

**Difficulty:** Medium  
**DSA skills:** Min-heaps, k-way merging, iterators

## Problem

Given a list of individually timestamp-sorted iterables of `(timestamp, event_id)` tuples, yield a single timestamp-sorted stream. Equal timestamps favor the lower input-stream index; preserve each stream's internal order. The IDs do not participate in ordering.

Independent hardware test stations produce sorted streams that a data platform must combine. Consume inputs incrementally, keeping at most one buffered event per stream. Return an iterator, not a list. Consuming iterators is expected; do not edit caller-owned collections.

## Function signature

```python
def merge_streams(streams: list[Iterable[tuple[int, str]]]) -> Iterator[tuple[int, str]]:
    ...
```

`Iterable` and any `Iterator` annotation are imported from `collections.abc`.

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
