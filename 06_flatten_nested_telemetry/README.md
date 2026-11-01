---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Flatten Nested Telemetry

**Difficulty:** Medium  
**DSA skills:** Trees, depth-first traversal, explicit stacks

## Problem

You are given a nested dictionary, `record`.

Return a flat dictionary whose keys join the nested keys with dots. For example, `{"gpu": {"temp": 80}}` becomes `{"gpu.temp": 80}`.

- Keep scalar values unchanged, including strings, numbers, booleans, and `None`.
- Empty dictionaries add no entries; output order does not matter.
- Keys are nonempty strings without dots, so paths cannot collide.
- Use iterative traversal to handle nesting deeper than Python's recursion limit.

## Example 1

Input (positional arguments):

```python
({'gpu': {'fan': {'rpm': 1200}, 'temperature': 80}, 'site': 'lab'},)
```

Output:

```python
{'gpu.fan.rpm': 1200, 'gpu.temperature': 80, 'site': 'lab'}
```

**Explanation:** Follow the nested keys to each value and join those keys with dots:

```text
gpu -> fan -> rpm       becomes gpu.fan.rpm = 1200
gpu -> temperature      becomes gpu.temperature = 80
site                    stays   site = 'lab'
```

The output contains one entry for each of these three values.

## Example 2

Input (positional arguments):

```python
({'gpu': {}, 'healthy': True, 'reading': None},)
```

Output:

```python
{'healthy': True, 'reading': None}
```

**Explanation:** The empty dictionary under `gpu` contains no values, so it adds no output entry. `healthy` and `reading` already hold values rather than dictionaries. Keep `True` and `None` unchanged under their original keys.

## Constraints

At most 10,000 dictionary entries, including deeply nested chains of 2,000 or more levels. Inputs are acyclic; shared dictionaries may occur at different paths.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
