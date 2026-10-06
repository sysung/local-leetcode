---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-10-05
---
# Balance Ordered ETL Workloads

**Difficulty:** Hard  
**DSA skills:** Binary search on the answer, greedy feasibility checking

## Problem

You are given a list of processing costs, `loads`, and an integer `batch_count`.

Split `loads` into exactly `batch_count` nonempty contiguous batches. Return the smallest possible value of the largest batch sum.

- Preserve the order of the loads.
- Return only the minimum largest sum, not the batches.
- Raise `ValueError` if the input is empty, a load is negative, or `batch_count` is outside `1..len(loads)`.

## Example 1

Input (positional arguments):

```python
([7, 2, 5, 10, 8], 2)
```

Output:

```python
18
```

**Explanation:** Splitting into [7, 2, 5] and [10, 8] gives sums 14 and 18; a smaller maximum is impossible.

## Example 2

Input (positional arguments):

```python
([1, 2, 3, 4, 5], 3)
```

Output:

```python
6
```

**Explanation:** [1, 2, 3], [4], [5] achieve a maximum of 6.

## Constraints

At most 100,000 loads, each an integer with magnitude at most 10^9. batch_count is an integer.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
