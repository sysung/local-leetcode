---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-09-30
---
# Track Sliding Temperature Medians

**Difficulty:** Hard  
**DSA skills:** Two heaps, lazy deletion, heap rebalancing

## Problem

Given integer temperature readings and window size k, return one floating-point median for every consecutive window of exactly k readings. For even k, average the two middle values. Repeated readings are distinct occurrences. Raise `ValueError` unless `1 <= k <= len(values)`.

Rolling medians resist occasional sensor spikes in hardware telemetry. Target O(n log(k + 1)) time and O(k) auxiliary space. Expired entries must not accumulate indefinitely in the heaps; periodically compact them.

## Function signature

```python
def sliding_medians(values: list[int], k: int) -> list[float]:
    ...
```

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
