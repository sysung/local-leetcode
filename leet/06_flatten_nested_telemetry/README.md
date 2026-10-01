---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-09-30
---
# Flatten Nested Telemetry

**Difficulty:** Medium  
**DSA skills:** Trees, depth-first traversal, explicit stacks

## Problem

Flatten a nested telemetry dictionary into a dictionary whose keys are dotted paths. Dictionary nodes can contain more dictionaries or scalar leaves (strings, integers, floats, booleans, or `None`). Preserve leaf values exactly. Empty dictionaries produce no output entries. Keys are nonempty strings with no dots, so paths cannot collide. Dictionary output order is not significant.

Telemetry schema evolution can introduce nested hardware measurements. This exercise treats the document as a tree and prepares leaves for tabular analysis. Use iterative traversal to support nesting deeper than Python's recursion limit.

## Function signature

```python
def flatten_telemetry(record: dict[str, Any]) -> dict[str, Any]:
    ...
```

`Any` is imported from `typing`.

## Example 1

Input (positional arguments):

```python
({'gpu': {'fan': {'rpm': 1200}, 'temperature': 80}, 'site': 'lab'},)
```

Output:

```python
{'gpu.fan.rpm': 1200, 'gpu.temperature': 80, 'site': 'lab'}
```

**Explanation:** Each dictionary edge contributes one path component.

## Example 2

Input (positional arguments):

```python
({'gpu': {}, 'healthy': True, 'reading': None},)
```

Output:

```python
{'healthy': True, 'reading': None}
```

**Explanation:** Empty dictionaries contribute no leaves; booleans and None are preserved.

## Constraints

At most 10,000 dictionary entries, including deeply nested chains of 2,000 or more levels. Inputs are acyclic; shared dictionaries may occur at different paths.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
