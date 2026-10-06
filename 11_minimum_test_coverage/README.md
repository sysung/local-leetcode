---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-10-05
---
# Find the Smallest Complete Diagnostic Sequence

**Difficulty:** Hard  
**DSA skills:** Variable sliding windows, hash maps, two pointers

## Problem

You are given a list of diagnostic codes, `codes`, and a set of required codes, `required`.

Return the inclusive `(start, end)` indices of the shortest contiguous slice containing every required code at least once. The codes may appear in any order.

- Minimize the number of entries in the slice, not elapsed time.
- If slices have the same length, choose the earliest start.
- Return `None` if `required` is empty or no matching slice exists.
- Target O(n + r) time, where n is the number of codes and r is the number of required codes.

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
