---
type: coding-practice
difficulty: hard
created: 2026-09-30
updated: 2026-09-30
---
# Reconstruct a Pipeline Execution Trace

**Difficulty:** Hard  
**DSA skills:** Directed multigraphs, Eulerian paths, iterative Hierholzer traversal

## Problem

Each `(source, destination)` tuple records one directed transition between pipeline stages. Starting at `start`, reconstruct a node sequence that uses every transition exactly once. Duplicate transitions are separate edges. If several complete traces exist, return the lexicographically smallest node sequence using normal Python string ordering. Return `[start]` for no transitions. Raise `ValueError` when no complete trace exists from the given start.

This is a simplified trace-reconstruction model: assume all supplied transitions belong to one execution whose ordering was lost. Real traces may require additional correlation information.

## Function signature

```python
def reconstruct_trace(transitions: list[tuple[str, str]], start: str) -> list[str]:
    ...
```

## Example 1

Input (positional arguments):

```python
([('extract', 'validate'), ('validate', 'publish')], 'extract')
```

Output:

```python
['extract', 'validate', 'publish']
```

**Explanation:** Both transitions form one ordered path.

## Example 2

Input (positional arguments):

```python
([('A', 'C'), ('A', 'B'), ('B', 'A'), ('C', 'A')], 'A')
```

Output:

```python
['A', 'B', 'A', 'C', 'A']
```

**Explanation:** Both cycles can be traversed; the trace visiting B first is lexicographically smaller.

## Constraints

At most 100,000 transitions. Stage names and start are nonempty strings.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
