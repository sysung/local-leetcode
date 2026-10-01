---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-09-30
---
# Detect Repeated Device Failures

**Difficulty:** Medium  
**DSA skills:** Sliding windows, deques, hash maps

## Problem

Process timestamp-sorted `(timestamp, device_id, status)` events. After each event, count failures for that event's device in `(timestamp - window, timestamp]`. If the count is at least `threshold`, append `(timestamp, device_id, count)` to the result. A PASS event can also trigger an alert if prior failures are still in its window. Emit an alert for every qualifying event, not just when crossing the threshold. Process simultaneous events in input order.

This models real-time hardware failure monitoring. Window and threshold must be positive; otherwise raise `ValueError`.

## Function signature

```python
def failure_alerts(events: list[tuple[int, str, str]], window: int, threshold: int) -> list[tuple[int, str, int]]:
    ...
```

## Example 1

Input (positional arguments):

```python
([(1, 'a', 'FAIL'), (2, 'a', 'FAIL'), (3, 'a', 'PASS')], 5, 2)
```

Output:

```python
[(2, 'a', 2), (3, 'a', 2)]
```

**Explanation:** The second failure meets the threshold; the following PASS still has two recent failures.

## Example 2

Input (positional arguments):

```python
([(0, 'a', 'FAIL'), (5, 'a', 'FAIL')], 5, 2)
```

Output:

```python
[]
```

**Explanation:** At timestamp 5, timestamp 0 is excluded from the open-left window.

## Constraints

At most 100,000 valid events sorted by timestamp. Timestamps are nonnegative integers; status is PASS or FAIL. Window and threshold are integers.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
