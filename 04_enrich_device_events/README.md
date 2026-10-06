---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-10-05
---
# Join Events with Device Metadata

**Difficulty:** Easy  
**DSA skills:** Hash maps, indexed lookup, hash joins

## Problem

You are given event dictionaries, `events`, and device metadata, `devices`. Both contain a `device_id`; metadata also contains `model` and `site`.

Return copies of the events with `model` and `site` from the matching device.

- For unknown devices, set both fields to `None`.
- If metadata contains the same device ID more than once, use the last record.
- Replace any existing `model` and `site` fields, preserving all other fields and event order.

## Example 1

Input (positional arguments):

```python
([{'device_id': 'a', 'value': 7}, {'device_id': 'x', 'value': 8}],
 [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}])
```

Output:

```python
[{'device_id': 'a', 'model': 'GPU', 'site': 'lab', 'value': 7},
 {'device_id': 'x', 'model': None, 'site': None, 'value': 8}]
```

**Explanation:** The known device receives metadata; the unknown device remains in the output.

## Example 2

Input (positional arguments):

```python
([{'device_id': 'a'}],
 [{'device_id': 'a', 'model': 'old', 'site': 'one'},
  {'device_id': 'a', 'model': 'new', 'site': 'two'}])
```

Output:

```python
[{'device_id': 'a', 'model': 'new', 'site': 'two'}]
```

**Explanation:** The last metadata record wins.

## Constraints

At most 100,000 events and metadata records. Required fields exist and metadata values are strings. Record width is bounded.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
