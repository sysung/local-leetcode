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

You are given arrival-ordered job events, `events`. Each event is `(job_id, state)`.

Process each job independently. A new job must start in `QUEUED`, with these allowed transitions:

- `QUEUED` → `RUNNING` or `CANCELLED`.
- `RUNNING` → `SUCCEEDED`, `FAILED`, or `CANCELLED`.
- `SUCCEEDED`, `FAILED`, and `CANCELLED` are terminal: no further transitions are allowed.

Return `(states, rejected_indices)`. `states` maps each job to its latest accepted state; `rejected_indices` lists rejected events' zero-based indices in arrival order.

- Reject unknown states, repeated states, and all other invalid transitions.
- A rejected event does not change the job's state; continue processing later events.
- Omit jobs that have no accepted events.

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
