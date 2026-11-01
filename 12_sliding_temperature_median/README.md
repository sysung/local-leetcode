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

**Explanation:** Move a three-reading window one position at a time. Sort each window to identify its middle value:

| Window | Sorted readings | Median |
| --- | --- | --- |
| `[1, 3, -1]` | `[-1, 1, 3]` | `1.0` |
| `[3, -1, -3]` | `[-3, -1, 3]` | `-1.0` |
| `[-1, -3, 5]` | `[-3, -1, 5]` | `-1.0` |
| `[-3, 5, 3]` | `[-3, 3, 5]` | `3.0` |
| `[5, 3, 6]` | `[3, 5, 6]` | `5.0` |
| `[3, 6, 7]` | `[3, 6, 7]` | `6.0` |

Return these medians in window order. Sorting here illustrates the median definition, not a required implementation.

## Example 2

Input (positional arguments):

```python
([10, 20, 30, 40], 2)
```

Output:

```python
[15.0, 25.0, 35.0]
```

**Explanation:** The windows are `[10, 20]`, `[20, 30]`, and `[30, 40]`. Each has two readings, so average them: `(10 + 20) / 2 = 15.0`, `(20 + 30) / 2 = 25.0`, and `(30 + 40) / 2 = 35.0`.

## Constraints

At most 100,000 readings. Readings are integers in [-10^9, 10^9]; k is an integer.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
