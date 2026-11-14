---
type: coding-practice
difficulty: medium
created: 2026-09-30
updated: 2026-10-05
---
# Rank the Most Frequent Failure Codes

**Difficulty:** Medium
**DSA skills:** Frequency maps, custom sorting

## Problem

You are given a list of failure codes, `codes`, and an integer `k`.

Return up to `k` `(code, count)` pairs, ordered from most frequent to least frequent.

- Break frequency ties alphabetically by code.
- If fewer than `k` distinct codes exist, return them all.
- Return `[]` if `k <= 0`.

## Complexity requirement

Let n be the number of input codes, u the number of distinct codes, and h = min(max(k, 0), u). Use expected O(n + u log(h + 1) + h log(h + 1)) time and O(u + h) space. Select with a bounded heap; do not sort all u distinct codes when k is small. Include deterministic ordering of the selected output in your analysis.

## Example 1

Input (positional arguments):

```python
(['ECC', 'TEMP', 'ECC', 'POWER'], 2)
```

Output:

```python
[('ECC', 2), ('POWER', 1)]
```

**Explanation:** The counts are `ECC: 2`, `TEMP: 1`, and `POWER: 1`. `ECC` ranks first because it occurs twice. `POWER` and `TEMP` tie, so `POWER` comes first alphabetically. With `k = 2`, return only `ECC` and `POWER`.

## Example 2

Input (positional arguments):

```python
(['Z', 'A', 'B'], 5)
```

Output:

```python
[('A', 1), ('B', 1), ('Z', 1)]
```

**Explanation:** Each code occurs once, so order all three alphabetically as `A`, `B`, `Z`. Although `k = 5`, only three distinct codes exist. Return those three with count `1` each.

## Constraints

At most 100,000 codes. Codes are nonempty strings; k is an integer.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Python hash-map operations use their expected average-case complexity.

## Practice

Fill in `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests exercise `main.py` only. The starter intentionally raises `NotImplementedError`. Check `solution.py` after your attempt for the complete algorithm and complexity analysis.

## Interview follow-ups

- Audience membership uses sets: intersect required groups with a universe, then subtract exclusions. No required groups means the universe; an empty required group means no audience. Duplicate IDs do not matter.
- Campaign reconciliation uses multisets: compare counts per `(campaign_id, event_id)` across source and destination and report differing counts, including missing keys as zero. Set comparison would hide duplicate delivery.
- Neither follow-up is part of `top_failure_codes`; explain the different semantics rather than adding unrelated functions to this exercise.
