---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Materialize profile state from CDC

**Difficulty:** Medium  
**DSA skills:** Hash maps, version ordering, tombstones

## Problem

- **Implement `materialize_profiles(changes)` to determine which customer profiles are still live after all changes and return their final values.**

### Input

- `changes` is a list of `(profile_id, version, operation, value)` tuples. Profile IDs are nonempty strings and versions are nonnegative integers.
- `operation` is either `"upsert"` or `"delete"`. An upsert's `value` is a string, including the empty string. A delete's `value` is `None`.

### Rules

- For each profile, the highest version wins. At the same version, delete wins over upsert. Among conflicting upserts at the same version, the lexicographically greatest value wins.
- Exact duplicate changes have no additional effect. Changes can arrive out of version order, and input order never changes the result. An upsert with a higher version can recreate a deleted profile.
- Return `(profile_id, version, value)` tuples for live profiles only, sorted by profile ID. Preserve a delete's winning version internally so that older upserts cannot resurrect it.

## Example 1

Input (positional arguments):

```python
([('a', 2, 'upsert', 'new'), ('a', 1, 'upsert', 'old'), ('b', 4, 'delete', None), ('b', 3, 'upsert', 'stale')],)
```

Output:

```python
[('a', 2, 'new')]
```

**Explanation:** Profile `a` has upserts at versions `2` and `1`. Version `2` wins, keeping value `new` even though the older update arrives afterward. Profile `b` has a delete at version `4`, which overrides the upsert at version `3`. Omit deleted profile `b`, leaving only `('a', 2, 'new')`.

## Example 2

Input (positional arguments):

```python
([('a', 1, 'upsert', 'A'), ('a', 1, 'upsert', 'Z'), ('b', 2, 'upsert', 'x'), ('b', 2, 'delete', None)],)
```

Output:

```python
[('a', 1, 'Z')]
```

**Explanation:** Profile `a` has two upserts at version `1`. Choose value `Z` because it is lexicographically greater than `A`. Profile `b` has an upsert and a delete at version `2`. The delete wins the version tie, so omit `b` from the live output.

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

## Interview follow-ups: one reduction, different policies

These are discussion variants, not changes to `materialize_profiles` or its tests.

1. **Latest event per ID:** select greatest timestamp, keep the last input occurrence on a tie, preserve its payload, and sort by ID. This policy depends on arrival order; CDC tie resolution does not.
2. **Consent as of activation:** for each `(user, purpose)`, ignore events later than `as_of`; select the greatest eligible timestamp, with revocation winning equal-time disagreement. Include revoked states and sort by key. This filters by event time; it does not model tombstone resurrection.
3. Explain which comparator/state changes for each variant. Timestamp eligibility, arrival-order ties, and deletion precedence are different requirements even though all use keyed reduction.
