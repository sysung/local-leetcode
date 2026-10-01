---
type: coding-practice
difficulty: easy
created: 2026-09-30
updated: 2026-09-30
---
# Rank the Most Frequent Failure Codes

**Difficulty:** Easy  
**DSA skills:** Frequency maps, custom sorting

## Problem

Given a list of failure-code strings and integer `k`, return up to `k` `(code, count)` pairs. Rank higher counts first; break ties alphabetically by code. Return an empty list if `k <= 0`. If fewer than `k` distinct codes exist, return them all.

This models prioritizing the most common chip or board test failures for analysis.

## Function signature

```python
def top_failure_codes(codes: list[str], k: int) -> list[tuple[str, int]]:
    ...
```

## Example 1

Input (positional arguments):

```python
(['ECC', 'TEMP', 'ECC', 'POWER'], 2)
```

Output:

```python
[('ECC', 2), ('POWER', 1)]
```

**Explanation:** ECC is most frequent; POWER precedes TEMP alphabetically for the tie.

## Example 2

Input (positional arguments):

```python
(['Z', 'A', 'B'], 5)
```

Output:

```python
[('A', 1), ('B', 1), ('Z', 1)]
```

**Explanation:** All counts tie, and requesting more than the distinct count returns every code.

## Constraints

At most 100,000 codes. Codes are nonempty strings; k is an integer.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.
