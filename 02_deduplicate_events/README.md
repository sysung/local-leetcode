---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-10-05
---
# Keep the Newest Event

**Difficulty:** Easy  
**DSA skills:** Hash maps, sorting

## Problem

You are given a list of event dictionaries, `events`. Each event has an `event_id`, a `timestamp`, and a `payload`.

Return one event per ID, keeping the event with the greatest timestamp.

- If timestamps tie, keep the last occurrence in the input.
- Sort the result alphabetically by event ID.
- Keep all fields from each selected event.

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

**Explanation:** ID `b` appears at timestamps `1` and `2`. Keep its timestamp-`2` record, including payload `new`. ID `a` appears once, so keep that record too. Sort the selected records by ID, placing `a` before `b`.

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

**Explanation:** Both records have ID `a` and timestamp `4`. The timestamps tie, so keep the later input record with payload `last`. Only one record is returned for that ID.

## Constraints

At most 100,000 events. Event IDs are nonempty strings. Required fields exist and timestamps are nonnegative integers.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
