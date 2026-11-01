---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Combine Hardware Test Sessions

**Difficulty:** Medium  
**DSA skills:** Sorting, interval algorithms, linear scanning

## Problem

You are given a list of test-session intervals, `intervals`. Each interval is `(start, end)` with `start <= end`.

Merge overlapping intervals and intervals that touch at an endpoint. Return the merged intervals sorted by start time.

- Zero-length intervals are valid.
- Do not modify the input list.

## Example 1

Input (positional arguments):

```python
([(5, 8), (1, 4), (3, 6)],)
```

Output:

```python
[(1, 8)]
```

**Explanation:** In start-time order, the intervals are `(1, 4)`, `(3, 6)`, and `(5, 8)`. The first two overlap and cover `(1, 6)`. That interval overlaps `(5, 8)`, so all three merge into `(1, 8)`.

## Example 2

Input (positional arguments):

```python
([(1, 2), (2, 3), (5, 7)],)
```

Output:

```python
[(1, 3), (5, 7)]
```

**Explanation:** Intervals `(1, 2)` and `(2, 3)` touch at `2`, so they merge into `(1, 3)`. There is a gap between `3` and `5`, so `(5, 7)` remains a separate interval.

## Constraints

At most 100,000 intervals. Endpoints are integers and each interval is valid.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
