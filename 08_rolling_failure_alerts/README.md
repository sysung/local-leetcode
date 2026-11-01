---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Detect Repeated Device Failures

**Difficulty:** Medium  
**DSA skills:** Sliding windows, deques, hash maps

## Problem

You are given timestamp-sorted `events`, a window length `window`, and a failure `threshold`. Each event is `(timestamp, device_id, status)`.

After each event, count that device's failures at times greater than `timestamp - window` and at most `timestamp`. If the count is at least `threshold`, append `(timestamp, device_id, count)` to the result.

- A `PASS` event can trigger an alert if enough earlier failures remain in its window.
- Emit an alert for every qualifying event, not only when the count first reaches the threshold.
- Process events with equal timestamps in input order.
- Raise `ValueError` if `window` or `threshold` is not positive.

## Example 1

Input (positional arguments):

```python
([(1, 'a', 'FAIL'), (2, 'a', 'FAIL'), (3, 'a', 'PASS')], 5, 2)
```

Output:

```python
[(2, 'a', 2), (3, 'a', 2)]
```

**Explanation:** With window `5` and threshold `2`, the failure counts after each event are:

| Timestamp | Event | Failures in the window | Alert? |
| --- | --- | --- | --- |
| 1 | `FAIL` | 1 | No |
| 2 | `FAIL` | 2 | Yes |
| 3 | `PASS` | 2 | Yes |

The `PASS` does not add a failure, but both earlier failures are still in its window. Return alerts at timestamps `2` and `3`.

## Example 2

Input (positional arguments):

```python
([(0, 'a', 'FAIL'), (5, 'a', 'FAIL')], 5, 2)
```

Output:

```python
[]
```

**Explanation:** At timestamp `0`, there is only one failure. At timestamp `5`, the window includes times greater than `0` and at most `5`, so the failure at `0` has expired. The count is again `1`, below threshold `2`. No event produces an alert.

## Constraints

At most 100,000 valid events sorted by timestamp. Timestamps are nonnegative integers; status is PASS or FAIL. Window and threshold are integers.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
