---
type: coding-practice
difficulty: easy
created: 2026-11-01
updated: 2026-11-01
---
# Apply audience inclusion and exclusion rules

**Difficulty:** Easy  
**DSA skills:** Sets, intersection, difference

## Problem

An activation job combines required audience memberships, then removes suppression-list members.

Implement `build_audience(universe, required_groups, excluded)`.

- `universe` and `excluded` are lists of nonempty user ID strings. `required_groups` is a list of lists of nonempty user ID strings.
- A user qualifies only if the user is in `universe`, appears in every required group, and does not appear in `excluded`.
- With no required groups, every universe member qualifies before exclusions. An empty required group makes the result empty.
- Ignore duplicate IDs and IDs outside the universe. Return distinct qualifying IDs in lexicographic order.

## Example 1

Input (positional arguments):

```python
(['a', 'b', 'c', 'd'], [['a', 'b', 'c'], ['b', 'c', 'd']], ['c'])
```

Output:

```python
['b']
```

**Explanation:** Users `b` and `c` appear in both required groups and in the universe. User `a` is missing from the second group, and `d` is missing from the first. Exclude `c` because it is on the suppression list. Only `b` remains.

## Example 2

Input (positional arguments):

```python
(['b', 'a', 'b'], [], ['b'])
```

Output:

```python
['a']
```

**Explanation:** There are no required groups, so both distinct universe members, `a` and `b`, initially qualify. Duplicate `b` does not create another member. Excluding `b` leaves only `a`.

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
