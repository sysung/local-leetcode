---
type: coding-practice
difficulty: medium
created: 2026-11-14
updated: 2026-11-14
---
# Count contiguous adjustments matching a target

**Difficulty:** Medium (local)

## Problem

Given integer adjustments `values` and an integer `target`, return the number of nonempty contiguous ranges whose sum equals `target`. Values and target may be negative or zero. Count overlapping ranges separately. Empty input returns 0; do not mutate input. At most 100,000 values, each between -10**9 and 10**9.

Example: `count_target_ranges([1, -1, 1], 1)` returns `3`: ranges `[0:1]`, `[0:3]`, and `[2:3]`.

Target expected O(n) time and O(n) space. Explain why a monotonic sliding window does not work when values can be negative. Frame this as signed daily campaign or telemetry adjustments; indices define order, not calendar duration.

## Practice

Implement `main.py`, then run from this folder:

```bash
python3 -m unittest -v test_case.py
```

The tests import your learner file; it intentionally raises until implemented. Compare with `solution.py` after your attempt. Output tests establish correctness on their cases, not the required asymptotic bound; justify that bound separately.
