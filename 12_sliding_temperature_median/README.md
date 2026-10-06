---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-10-05
---
# Track Sliding Temperature Medians

**Difficulty:** Hard  
**DSA skills:** Two heaps, lazy deletion, heap rebalancing

## Problem

You are given integer temperature readings, `values`, and a window size `k`.

Return a list containing the median of each consecutive window of `k` readings, as a float.

- For even `k`, average the two middle values.
- Repeated readings count as separate entries.
- Raise `ValueError` unless `1 <= k <= len(values)`.
- Target O(n log(k + 1)) time and O(k) auxiliary space. If you use heaps, compact them so expired entries do not accumulate indefinitely.

## Example 1

Input (positional arguments):

```python
([1, 3, -1, -3, 5, 3, 6, 7], 3)
```

Output:

```python
[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
```

**Explanation:** Each group of three contributes its middle reading.

## Example 2

Input (positional arguments):

```python
([10, 20, 30, 40], 2)
```

Output:

```python
[15.0, 25.0, 35.0]
```

**Explanation:** Each window has two readings; average them.

## Constraints

At most 100,000 readings. Readings are integers in [-10^9, 10^9]; k is an integer.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
