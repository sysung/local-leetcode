---
type: coding-practice
difficulty: medium
created: 2026-11-14
updated: 2026-11-14
---
# Container With Most Water

**Difficulty:** Medium (local)

## Problem

Given nonnegative integer heights at equally spaced positions, choose two positions i < j maximizing `min(heights[i], heights[j]) * (j - i)`. Return that maximum area. Fewer than two heights returns 0. Do not mutate input. At most 100,000 heights, each at most 10**9.

Example: `max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])` returns `49`, using indices 1 and 8.

Target O(n) time and O(1) auxiliary space. Prove why moving the shorter endpoint cannot discard a better candidate involving that endpoint. This deliberately keeps the standard geometry problem: its value is two-pointer elimination reasoning, not a forced business story.

## Practice

Implement `main.py`, then run from this folder:

```bash
python3 -m unittest -v test_case.py
```

The tests import your learner file; it intentionally raises until implemented. Compare with `solution.py` after your attempt. Output tests establish correctness on their cases, not the required asymptotic bound; justify that bound separately.
