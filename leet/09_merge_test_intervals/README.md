---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-09-30
---
# Combine Hardware Test Sessions

**Difficulty:** Medium  
**DSA skills:** Sorting, interval algorithms, linear scanning

## Problem

Given integer `(start, end)` test-session intervals with `start <= end`, return their sorted union. Merge overlapping intervals and intervals that touch at an endpoint. Preserve the original input list. Zero-length intervals are valid.

This models consolidating hardware test activity before calculating equipment utilization.

## Function signature

```python
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ...
```

## Example 1

Input (positional arguments):

```python
([(5, 8), (1, 4), (3, 6)],)
```

Output:

```python
[(1, 8)]
```

**Explanation:** The overlapping intervals form one connected session.

## Example 2

Input (positional arguments):

```python
([(1, 2), (2, 3), (5, 7)],)
```

Output:

```python
[(1, 3), (5, 7)]
```

**Explanation:** The first two intervals touch; the gap before 5 remains.

## Constraints

At most 100,000 intervals. Endpoints are integers and each interval is valid.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
