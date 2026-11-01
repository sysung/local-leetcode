---
type: coding-practice
difficulty: medium
created: 2026-10-05
updated: 2026-10-05
---
# Find Peak Concurrent Jobs

**Difficulty:** Medium  
**DSA skills:** Sweep lines, sorting, interval boundaries

## Problem

You are given job intervals, `intervals`. Each `(start, end)` describes a job that runs from `start` up to, but not including, `end`.

Return the maximum number of jobs running at the same time.

- A job ending at a time does not overlap with a job starting at that same time.
- Zero-duration jobs do not count.
- Intervals may be unsorted, and duplicate intervals represent separate jobs.
- Return `0` for an empty list. Return only the count, not the jobs or time.

## Example 1

Input (positional arguments):

```python
([(0, 4), (2, 5), (4, 7)],)
```

Output:

```python
2
```

**Explanation:** The number of running jobs changes as follows:

```text
Time range     Running jobs             Count
[0, 2)         (0, 4)                      1
[2, 4)         (0, 4), (2, 5)              2
[4, 5)         (2, 5), (4, 7)              2
[5, 7)         (4, 7)                      1
```

At time `4`, the first job has ended when the third starts. They do not overlap, so the maximum count is `2`, not `3`.

## Example 2

Input (positional arguments):

```python
([(1, 3), (1, 3), (2, 2)],)
```

Output:

```python
2
```

**Explanation:** The two `(1, 3)` entries represent separate jobs, so both run during `[1, 3)`. The job `(2, 2)` has zero duration and never counts as running. The maximum is therefore `2`.

## Constraints

At most 100,000 intervals. Endpoints are integers between 0 and 10**12 with start <= end.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
