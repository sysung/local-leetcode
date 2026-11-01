---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Build the latest consent snapshot

**Difficulty:** Medium  
**DSA skills:** Hash maps, composite ordering, event reduction

## Problem

A marketing activation job needs one consent state per user and purpose before it can export an audience.

Implement `latest_consent(events, as_of)`.

- `events` is a list of `(user_id, purpose, timestamp, granted)` tuples. IDs and purposes are nonempty strings, timestamps are nonnegative integers, and `granted` is a boolean.
- `as_of` is a nonnegative integer. Ignore events with `timestamp > as_of`.
- For each `(user_id, purpose)`, select the event with the greatest eligible timestamp. If events at that timestamp disagree, revocation (`False`) wins, regardless of input order.
- Return a list of `(user_id, purpose, timestamp, granted)` tuples, sorted by `(user_id, purpose)`. Include revoked states. Omit pairs with no eligible event.
- Exact duplicate events have no additional effect.

## Example 1

Input (positional arguments):

```python
([('u1', 'ads', 4, True), ('u1', 'ads', 9, False), ('u1', 'email', 5, True)], 10)
```

Output:

```python
[('u1', 'ads', 9, False), ('u1', 'email', 5, True)]
```

**Explanation:** All three events occur at or before `as_of = 10`. For purpose `ads`, timestamp `9` is later than `4`, so keep the revoked state `False` at `9`. Purpose `email` has one eligible event, so keep its granted state `True` at `5`. Return `ads` before `email` in the sorted result.

## Example 2

Input (positional arguments):

```python
([('u1', 'ads', 7, False), ('u1', 'ads', 7, True)], 7)
```

Output:

```python
[('u1', 'ads', 7, False)]
```

**Explanation:** Both events refer to the same user and purpose at timestamp `7`, which is eligible at `as_of = 7`. Their timestamps tie but their consent values disagree. Revocation wins regardless of input order, so keep the event with `False`.

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
