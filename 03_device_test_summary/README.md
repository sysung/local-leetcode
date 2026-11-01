---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-10-05
---
# Calculate Device Test Yield

**Difficulty:** Easy  
**DSA skills:** Hash maps, counting, single-pass aggregation

## Problem

You are given a list of test records, `records`. Each record has a `device_id` and a status of `PASS` or `FAIL`.

Return a dictionary keyed by device ID. For each device, include:

- `total`: the number of tests.
- `failures`: the number of failed tests.
- `pass_rate`: the number of passed tests divided by `total`, as a float.

Include only devices that appear in the input.

## Example 1

Input (positional arguments):

```python
([{'device_id': 'gpu', 'status': 'PASS'}, {'device_id': 'gpu', 'status': 'FAIL'}],)
```

Output:

```python
{'gpu': {'failures': 1, 'pass_rate': 0.5, 'total': 2}}
```

**Explanation:** Device `gpu` has two tests, one `PASS` and one `FAIL`. Its total is `2`, its failure count is `1`, and its pass rate is `1 / 2 = 0.5`.

## Example 2

Input (positional arguments):

```python
([{'device_id': 'a', 'status': 'FAIL'}, {'device_id': 'b', 'status': 'PASS'}],)
```

Output:

```python
{'a': {'failures': 1, 'pass_rate': 0.0, 'total': 1},
 'b': {'failures': 0, 'pass_rate': 1.0, 'total': 1}}
```

**Explanation:** Device `a` has one failed test, giving total `1`, failures `1`, and pass rate `0 / 1 = 0.0`. Device `b` has one passed test, giving total `1`, failures `0`, and pass rate `1 / 1 = 1.0`. Count each device separately.

## Constraints

At most 100,000 records. Required fields exist; device IDs are nonempty strings and statuses are valid.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
