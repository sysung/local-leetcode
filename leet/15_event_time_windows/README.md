---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-09-30
---
# Aggregate Out-of-Order Event-Time Windows

**Difficulty:** Hard  
**DSA skills:** Hash maps, min-heaps, incremental aggregation, watermark-based eviction

## Problem

Process arrival-ordered `(timestamp, device_id, status)` events. Aggregate each accepted event by device into fixed windows `[j * window_size, (j + 1) * window_size)`. Return `(summaries, rejected_indices)`, where summaries contain `(window_start, device_id, total, failures)` tuples ordered by window start, then device ID. Rejected indices use zero-based input positions in arrival order. Do not output empty windows.

The watermark starts at negative infinity. Before handling an event, reject it if its timestamp is strictly below the existing watermark; equality is accepted. After accepting an event, advance the watermark to maximum observed timestamp minus `allowed_lateness`. Finalize windows whose end is at or below that watermark. Flush remaining windows at end of input. A rejected event contributes no counts.

This models event-time aggregation when test-station telemetry arrives out of order. Retain aggregation state only for open windows. `window_size` must be positive, `allowed_lateness` nonnegative, and timestamps nonnegative; otherwise raise `ValueError`.

## Function signature

```python
def aggregate_event_time(events: Iterable[tuple[int, str, str]], window_size: int, allowed_lateness: int) -> tuple[list[tuple[int, str, int, int]], list[int]]:
    ...
```

`Iterable` and any `Iterator` annotation are imported from `collections.abc`.

## Example 1

Input (positional arguments):

```python
([(7, 'a', 'PASS'), (3, 'a', 'FAIL'), (16, 'a', 'PASS'), (4, 'a', 'FAIL')], 10, 5)
```

Output:

```python
([(0, 'a', 2, 1), (10, 'a', 1, 0)], [3])
```

**Explanation:** Timestamp 3 is accepted against watermark 2. Timestamp 16 advances it to 11, so the final timestamp 4 is rejected.

## Example 2

Input (positional arguments):

```python
([(10, 'b', 'PASS'), (5, 'a', 'FAIL'), (4, 'a', 'PASS')], 5, 5)
```

Output:

```python
([(5, 'a', 1, 1), (10, 'b', 1, 0)], [2])
```

**Explanation:** Timestamp 5 equals the watermark and is accepted; timestamp 4 is too old.

## Constraints

At most 100,000 valid events apart from the explicitly checked numeric constraints. Timestamps, window size, and lateness are integers; device IDs are nonempty strings and status is PASS or FAIL.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
