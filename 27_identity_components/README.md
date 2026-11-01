---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Resolve identity components

**Difficulty:** Medium  
**DSA skills:** Graphs, connected components, iterative traversal

## Problem

An identity pipeline links browser, email, and customer identifiers. Resolve every identifier to a stable canonical identity.

Implement `resolve_identities(identifiers, links)`.

- `identifiers` is a list of nonempty strings. `links` is a list of `(left_id, right_id)` pairs of nonempty strings.
- Each link is undirected. The universe includes every identifier in `identifiers` and every endpoint in `links`.
- Identifiers connected directly or transitively belong to one component. The canonical ID is the lexicographically smallest identifier in that component, using Python string ordering.
- Return one `(identifier, canonical_id)` tuple for every distinct identifier, sorted by identifier.
- Repeated identifiers, duplicate or reversed links, and self-links have no additional effect. Isolated identifiers map to themselves.

## Example 1

Input (positional arguments):

```python
(['orphan'], [('email:a', 'cookie:b'), ('customer:c', 'email:a')])
```

Output:

```python
[('cookie:b', 'cookie:b'), ('customer:c', 'cookie:b'), ('email:a', 'cookie:b'), ('orphan', 'orphan')]
```

## Example 2

Input (positional arguments):

```python
(['z', 'b', 'a'], [('z', 'y')])
```

Output:

```python
[('a', 'a'), ('b', 'b'), ('y', 'y'), ('z', 'y')]
```

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
