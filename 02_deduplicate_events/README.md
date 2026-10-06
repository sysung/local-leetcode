---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-09-30
---
# Keep the Newest Event

**Difficulty:** Easy  
**DSA skills:** Hash maps, sorting

## Problem

Each event dictionary contains a string `event_id`, an integer `timestamp`, and an arbitrary `payload`. Return one record per event ID: the record with the greatest timestamp. If timestamps tie, the last occurrence in the input wins. Sort the returned records alphabetically by event ID and preserve every field on the selected record.

Retrying and replaying an ingestion pipeline can produce duplicate telemetry events; this exercise models deterministic deduplication.

## Function signature

```python
def deduplicate_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ...
```

`Any` is imported from `typing`.

## Example 1

Input (positional arguments):

```python
([{'event_id': 'b', 'payload': 'old', 'timestamp': 1},
  {'event_id': 'a', 'payload': 'a', 'timestamp': 3},
  {'event_id': 'b', 'payload': 'new', 'timestamp': 2}],)
```

Output:

```python
[{'event_id': 'a', 'payload': 'a', 'timestamp': 3},
 {'event_id': 'b', 'payload': 'new', 'timestamp': 2}]
```

**Explanation:** Event b keeps its newest record; a precedes b in the output.

## Example 2

Input (positional arguments):

```python
([{'event_id': 'a', 'payload': 'first', 'timestamp': 4},
  {'event_id': 'a', 'payload': 'last', 'timestamp': 4}],)
```

Output:

```python
[{'event_id': 'a', 'payload': 'last', 'timestamp': 4}]
```

**Explanation:** The last occurrence wins when timestamps are equal.

## Constraints

At most 100,000 events. Event IDs are nonempty strings. Required fields exist and timestamps are nonnegative integers.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
