---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-09-30
---
# Calculate Device Test Yield

**Difficulty:** Easy  
**DSA skills:** Hash maps, counting, single-pass aggregation

## Problem

Given test dictionaries with `device_id` and `status`, return a dictionary keyed by device ID. Each value contains integer `total`, integer `failures`, and floating-point `pass_rate`. Pass rate is successful tests divided by total tests, between zero and one. Include only devices present in the input; status is either `PASS` or `FAIL`.

This models a transformation feeding hardware-quality reporting and analytics.

## Function signature

```python
def summarize_tests(records: list[dict[str, str]]) -> dict[str, dict[str, int | float]]:
    ...
```

## Example 1

Input (positional arguments):

```python
([{'device_id': 'gpu', 'status': 'PASS'}, {'device_id': 'gpu', 'status': 'FAIL'}],)
```

Output:

```python
{'gpu': {'failures': 1, 'pass_rate': 0.5, 'total': 2}}
```

**Explanation:** One of two tests passes, so the pass rate is 0.5.

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

**Explanation:** Each device is counted independently.

## Constraints

At most 100,000 records. Required fields exist; device IDs are nonempty strings and statuses are valid.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
