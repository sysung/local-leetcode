---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-10-05
---
# Parse Hardware Test Logs

**Difficulty:** Easy  
**DSA skills:** Strings, arrays, linear scanning

## Problem

You are given a list of strings, `lines`. Each valid line has the format `timestamp,device_id,status`.

Return a list of dictionaries containing `timestamp`, `device_id`, and `status` for each valid line.

- Trim whitespace around each field and preserve input order.
- Skip lines with missing or extra fields, an empty device ID, an invalid timestamp, or an invalid status.
- Timestamps must be nonnegative integers written with ASCII digits and an optional leading `+` or `-`.
- Status must be exactly `PASS` or `FAIL`.

## Example 1

Input (positional arguments):

```python
(['10,gpu-1,PASS', 'broken', '12,gpu-2,FAIL'],)
```

Output:

```python
[{'device_id': 'gpu-1', 'status': 'PASS', 'timestamp': 10},
 {'device_id': 'gpu-2', 'status': 'FAIL', 'timestamp': 12}]
```

**Explanation:** The malformed middle line is skipped; valid test results retain their order.

## Example 2

Input (positional arguments):

```python
([' 0 , board-1 , FAIL '],)
```

Output:

```python
[{'device_id': 'board-1', 'status': 'FAIL', 'timestamp': 0}]
```

**Explanation:** Whitespace is removed and timestamp zero is valid.

## Constraints

At most 100,000 lines; each line is at most 1,000 characters. Inputs are strings; numeric values fit normal Python integer conversion limits.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
