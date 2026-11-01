---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Attribute conversions to the last touch

**Difficulty:** Medium  
**DSA skills:** Grouped sorting, binary search, deterministic ties

## Problem

A campaign report credits each conversion to its most recent eligible marketing touch for the same user.

Implement `attribute_last_touch(touches, conversions, lookback)`.

- `touches` is a list of `(user_id, touch_timestamp, campaign_id)` tuples. `conversions` is a list of `(conversion_id, user_id, conversion_timestamp)` tuples.
- All IDs are nonempty strings. Conversion IDs are unique. Timestamps and `lookback` are nonnegative integers in the same time unit. Touches may repeat.
- A touch is eligible when it belongs to the conversion's user and lies in the inclusive interval `[conversion_timestamp - lookback, conversion_timestamp]`.
- Select the eligible touch with the greatest timestamp. At that timestamp, choose the lexicographically smallest campaign ID. Input order does not break ties.
- Return `(conversion_id, campaign_id_or_none)` tuples sorted by conversion ID. Use `None` when no eligible touch exists. The same touch can receive credit for multiple conversions.

## Example 1

Input (positional arguments):

```python
([('u', 1, 'old'), ('u', 8, 'new'), ('u', 12, 'future')], [('c1', 'u', 10)], 5)
```

Output:

```python
[('c1', 'new')]
```

**Explanation:** Conversion `c1` occurs at timestamp `10`, so lookback `5` gives the inclusive eligible interval `[5, 10]`. Campaign `old` at `1` is too early, and campaign `future` at `12` is after the conversion. Campaign `new` at `8` is the only eligible touch, so it receives credit.

## Example 2

Input (positional arguments):

```python
([('u', 7, 'z'), ('u', 7, 'a')], [('c2', 'missing', 10), ('c1', 'u', 10)], 3)
```

Output:

```python
[('c1', 'a'), ('c2', None)]
```

**Explanation:** For conversion `c1`, both touches belong to user `u` and occur at `7`, the included lower boundary of `[7, 10]`. Their timestamps tie, so choose campaign `a` before `z` lexicographically. Conversion `c2` belongs to user `missing`, who has no touches, so it maps to `None`. Sort the output by conversion ID.

## Constraints

At most 100,000 total input rows or IDs across all input collections. String comparisons and hashing use the usual unit-cost assumption. Integer timestamps, versions, and offsets are at most `10**12`.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
python3 main.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. The sample harness also raises until you implement the function. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
