---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Resolve ETL Dependencies

**Difficulty:** Medium  
**DSA skills:** Directed graphs, topological sorting, indegrees, min-heaps

## Problem

You are given a dictionary, `dependencies`, mapping task names to their prerequisites.

Return an execution order in which every prerequisite comes before its task.

- Include all named tasks, even those mentioned only as prerequisites.
- At each step, choose the alphabetically smallest task whose prerequisites are complete.
- Repeated prerequisite names count as one dependency.
- Raise `ValueError` if a cycle prevents a complete order, including a task that depends on itself.

## Example 1

Input (positional arguments):

```python
({'extract': [], 'publish': ['transform'], 'transform': ['extract']},)
```

Output:

```python
['extract', 'transform', 'publish']
```

**Explanation:** `extract` has no prerequisites, so it runs first. `transform` can then run because `extract` is complete. Finally, `publish` can run because `transform` is complete. The dependency chain is `extract -> transform -> publish`.

## Example 2

Input (positional arguments):

```python
({'b': ['a'], 'c': [], 'z': []},)
```

Output:

```python
['a', 'b', 'c', 'z']
```

**Explanation:** Initially, `a`, `c`, and `z` are available. Include `a` even though it appears only as a prerequisite. Choose `a` alphabetically, which makes `b` available. Now choose `b` before `c` and `z`, then finish with `c` and `z`.

## Constraints

At most 10,000 tasks and 100,000 prerequisite entries. Task names are nonempty strings.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
