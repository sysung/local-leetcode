---
type: coding-practice
difficulty: medium
created: 2026-11-14
updated: 2026-11-14
---
# Design historical keyed lookup

**Difficulty:** Medium (local)

## Problem

Implement `TimeMap()` with `set(key: str, value: str, timestamp: int) -> None` and `get(key: str, timestamp: int) -> str | None`.

Return the value at the greatest stored timestamp less than or equal to the query timestamp. Return `None` if no eligible version exists. Empty-string values are valid and differ from missing values. Keys are nonempty strings; timestamps are nonnegative integers. Writes for each individual key are strictly increasing; writes across different keys may interleave. Reject an equal or decreasing timestamp for the same key with `ValueError`, leaving state unchanged. Assume all other inputs are valid. At most 100,000 operations.

Example: set `('consent', 'yes', 3)`, then `('consent', 'no', 8)`. Queries at 2, 3, 7, and 8 return `None`, `'yes'`, `'yes'`, and `'no'`.

Target amortized O(1) valid writes, O(log m) lookup for a key with m versions, and O(total writes) space. An invalid write must also take O(1) time. This is an online API, unlike the batch attribution exercise. Discuss late-write insertion and retention after solving the defined contract.

## Practice

Implement `main.py`, then run from this folder:

```bash
python3 -m unittest -v test_case.py
```

The tests import your learner file; it intentionally raises until implemented. Compare with `solution.py` after your attempt. Output tests establish correctness on their cases, not the required asymptotic bound; justify that bound separately.
