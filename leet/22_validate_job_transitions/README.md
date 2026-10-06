---
type: coding-practice
difficulty: medium
created: 2026-10-05
updated: 2026-10-05
---
# Validate a Job State History

**Difficulty:** Medium  
**DSA skills:** State machines, hash maps, event replay

## Problem

Replay arrival-ordered `(job_id, state)` events. A new job must first enter `QUEUED`. Allowed transitions are `QUEUED -> RUNNING`, `QUEUED -> CANCELLED`, and `RUNNING -> SUCCEEDED`, `RUNNING -> FAILED`, or `RUNNING -> CANCELLED`. The last three states are terminal. Reject any other event, including unknown states, repeated states, or restarting a terminal job. Rejection leaves the accepted state unchanged and does not prevent later valid events from being processed. Return `(states, rejected_indices)`, where `states` maps each job with at least one accepted event to its latest accepted state and rejected indices are zero-based, in arrival order. Jobs with only rejected events are absent.

## Function signature

```python
def validate_job_history(events: list[tuple[str, str]]) -> tuple[dict[str, str], list[int]]:
    ...
```

## Example 1

Input (positional arguments):

```python
([('a', 'RUNNING'), ('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'FAILED'), ('a', 'QUEUED')],)
```

Output:

```python
({'a': 'FAILED'}, [0, 4])
```

**Explanation:** An invalid initial state is rejected; the later queue event starts the job.

## Example 2

Input (positional arguments):

```python
([('a', 'QUEUED'), ('b', 'QUEUED'), ('a', 'CANCELLED'), ('b', 'RUNNING')],)
```

Output:

```python
({'a': 'CANCELLED', 'b': 'RUNNING'}, [])
```

**Explanation:** Each job has its own independent state.

## Constraints

At most 100,000 events. Job IDs are nonempty strings. States may be any strings; unknown ones must be rejected.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
