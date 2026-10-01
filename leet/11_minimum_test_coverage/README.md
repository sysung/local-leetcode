---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-09-30
---
# Find the Smallest Complete Diagnostic Sequence

**Difficulty:** Hard  
**DSA skills:** Variable sliding windows, hash maps, two pointers

## Problem

Given diagnostic-code strings and a set of required codes, return inclusive `(start_index, end_index)` indices of the shortest contiguous sequence containing every required code at least once. Minimize the number of events, not elapsed time. Ties favor the earliest starting index. Return `None` when requirements are empty or no sequence covers them all.

A hardware engineer wants the smallest slice of a diagnostic trace that contains all relevant failure categories. Target O(n + r) time for n events and r required codes.

## Function signature

```python
def minimum_test_coverage(codes: list[str], required: set[str]) -> tuple[int, int] | None:
    ...
```

## Example 1

Input (positional arguments):

```python
(['A', 'X', 'B', 'A', 'C', 'B'], {'C', 'B', 'A'})
```

Output:

```python
(2, 4)
```

**Explanation:** Indices 2 through 4 contain B, A, C. The equal-length later candidate loses the earliest-start tie.

## Example 2

Input (positional arguments):

```python
(['A', 'A', 'B'], {'B', 'A'})
```

Output:

```python
(1, 2)
```

**Explanation:** Only one A is needed, so the redundant first A is removed.

## Constraints

At most 100,000 codes and 10,000 required codes. Codes are nonempty strings; required is a set.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
