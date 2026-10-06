---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-09-30
---
# Resolve ETL Dependencies

**Difficulty:** Medium  
**DSA skills:** Directed graphs, topological sorting, indegrees, min-heaps

## Problem

A dictionary maps each task name to a list of prerequisites. Return a valid execution order containing every named task, including tasks mentioned only as prerequisites. At each step, choose the alphabetically smallest currently available task. Repeated prerequisite names represent one dependency. Raise `ValueError` if any cycle prevents a complete order, including a self-dependency.

This models orchestration of extraction, validation, transformation, and data-lake publishing stages.

## Function signature

```python
def order_tasks(dependencies: dict[str, list[str]]) -> list[str]:
    ...
```

## Example 1

Input (positional arguments):

```python
({'extract': [], 'publish': ['transform'], 'transform': ['extract']},)
```

Output:

```python
['extract', 'transform', 'publish']
```

**Explanation:** Each prerequisite executes before its dependent stage.

## Example 2

Input (positional arguments):

```python
({'b': ['a'], 'c': [], 'z': []},)
```

Output:

```python
['a', 'b', 'c', 'z']
```

**Explanation:** Prerequisite-only task a is included; b becomes available before c is selected.

## Constraints

At most 10,000 tasks and 100,000 prerequisite entries. Task names are nonempty strings.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
