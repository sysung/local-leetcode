---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-10-05
---
# Aggregate Out-of-Order Event-Time Windows

**Difficulty:** Hard  
**DSA skills:** Hash maps, min-heaps, incremental aggregation, watermark-based eviction

## Problem

You are given arrival-ordered `events`, a `window_size`, and `allowed_lateness`. Each event is `(timestamp, device_id, status)`.

Group accepted events by device into time windows of length `window_size` starting at multiples of `window_size`. Each window includes its start and excludes its end.

Return `(summaries, rejected_indices)`. Each summary is `(window_start, device_id, total, failures)`; sort summaries by window start, then device ID.

- The watermark starts at negative infinity. Reject an event if its timestamp is below the current watermark; equality is accepted.
- After accepting an event, set the watermark to the greatest accepted timestamp minus `allowed_lateness`.
- Finalize windows whose end is at or below the watermark. Keep counts only for open windows, and flush them at the end.
- Rejected events add no counts. Return their zero-based input indices in arrival order, and omit empty windows.
- Raise `ValueError` if `window_size <= 0`, `allowed_lateness < 0`, or any timestamp is negative.

## Example 1

Input (positional arguments):

```python
([(7, 'a', 'PASS'), (3, 'a', 'FAIL'), (16, 'a', 'PASS'), (4, 'a', 'FAIL')], 10, 5)
```

Output:

```python
([(0, 'a', 2, 1), (10, 'a', 1, 0)], [3])
```

**Explanation:** Process the events in arrival order with allowed lateness `5`:

| Input index | Timestamp | Watermark before event | Decision | Watermark after event |
| --- | --- | --- | --- | --- |
| 0 | 7 | Negative infinity | Accept | 2 |
| 1 | 3 | 2 | Accept | 2 |
| 2 | 16 | 2 | Accept | 11 |
| 3 | 4 | 11 | Reject | 11 |

Timestamps `7` and `3` fall in window `[0, 10)`, giving two events and one failure for device `a`. Timestamp `16` falls in `[10, 20)`, giving one event and no failures. Reject input index `3` because timestamp `4` is below watermark `11`.

## Example 2

Input (positional arguments):

```python
([(10, 'b', 'PASS'), (5, 'a', 'FAIL'), (4, 'a', 'PASS')], 5, 5)
```

Output:

```python
([(5, 'a', 1, 1), (10, 'b', 1, 0)], [2])
```

**Explanation:** Timestamp `10` is accepted and sets the watermark to `10 - 5 = 5`. Timestamp `5` equals the watermark, so it is accepted. Timestamp `4` is below the watermark, so reject input index `2`. Device `a` has one failure in `[5, 10)`, and device `b` has one passing event in `[10, 15)`. List the summaries by window start.

## Constraints

At most 100,000 valid events apart from the explicitly checked numeric constraints. Timestamps, window size, and lateness are integers; device IDs are nonempty strings and status is PASS or FAIL.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
