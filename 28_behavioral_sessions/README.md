---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Sessionize behavioral events

**Difficulty:** Medium  
**DSA skills:** Sorting, grouped scans, boundary conditions

## Problem

Implement `sessionize(events, timeout)` to group each user's page and product events into sessions based on the gaps between events.

- **Process each user's events in timestamp order. If two events have the same timestamp, sort them by `event_id`. Start a new session when the gap since that user's previous event is greater than `timeout`. If the gap equals `timeout`, keep the event in the same session.**
- `events` is a list of `(user_id, timestamp, event_id)` tuples. Both IDs are nonempty strings. `timestamp` and `timeout` are nonnegative integers measured in the same unit.
- Number each user's sessions starting at 1. Use the first and last event timestamps as the inclusive start and end of the session. Count every event row, including exact duplicates.
- Return a list of `(user_id, session_number, start_timestamp, end_timestamp, event_count)` tuples sorted by `user_id`, then by `session_number`. If `events` is empty, return `[]`.

## Example 1

Input (positional arguments):

```python
([('u', 0, 'a'), ('u', 5, 'b'), ('u', 11, 'c')], 5)
```

Output:

```python
[('u', 1, 0, 5, 2), ('u', 2, 11, 11, 1)]
```

**Explanation:** The gap from timestamp `0` to `5` is exactly timeout `5`, so both events stay in session `1`. Its start is `0`, its end is `5`, and it contains two events. The next gap is `11 - 5 = 6`, greater than the timeout, so timestamp `11` starts session `2` with one event.

## Example 2

Input (positional arguments):

```python
([('b', 4, 'b1'), ('a', 9, 'a2'), ('a', 1, 'a1')], 10)
```

Output:

```python
[('a', 1, 1, 9, 2), ('b', 1, 4, 4, 1)]
```

**Explanation:** For user `a`, process timestamps `1` and `9` in that order even though the input lists them in reverse. Their gap is `8`, within timeout `10`, so they form one session with two events. User `b` has one event at `4` and gets a separate session numbered `1`. Sort the result by user, placing `a` before `b`.

## Constraints

At most 100,000 total input rows or IDs across all input collections. String comparisons and hashing use the usual unit-cost assumption. Integer timestamps, versions, and offsets are at most `10**12`.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
python3 main.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. The sample harness also raises until you implement the function. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
