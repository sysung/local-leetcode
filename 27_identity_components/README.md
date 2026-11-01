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

Given a list of links between IDs, return the lexicographically smallest ID connected to each ID, directly or through other IDs.

Implement `resolve_identities(links)`.

- `links` is a list of `(left_id, right_id)` pairs. Each ID is a nonempty string.
- Links work in both directions. If `a` links to `b` and `b` links to `c`, all three belong to the same group.
- For each distinct ID appearing in `links`, return `(id, smallest_id_in_its_group)`.
- Sort the returned tuples by ID. Use Python string ordering for both the smallest ID and the output order.
- Represent an ID with no connections to other IDs using a self-link, such as `('orphan', 'orphan')`.
- Repeated or reversed links do not change the result. An empty list returns `[]`.

## Example 1

Input:

```python
[('email:a', 'cookie:b'), ('customer:c', 'email:a'), ('orphan', 'orphan')]
```

Output:

```python
[('cookie:b', 'cookie:b'), ('customer:c', 'cookie:b'), ('email:a', 'cookie:b'), ('orphan', 'orphan')]
```

**Explanation:** The links form these groups:

```text
cookie:b --- email:a --- customer:c

orphan  (self-link)
```

The first three IDs are connected. Their smallest ID is `cookie:b`, so all three map to it. `orphan` only links to itself, so it maps to itself.

## Example 2

Input:

```python
[('z', 'y'), ('b', 'b'), ('a', 'a')]
```

Output:

```python
[('a', 'a'), ('b', 'b'), ('y', 'y'), ('z', 'y')]
```

**Explanation:** `z` and `y` are connected, so both map to `y`. The self-links put `a` and `b` in separate groups.

## Constraints

At most 100,000 links. String comparisons and hashing use the usual unit-cost assumption.

Do not modify the input list. Assume valid inputs. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
python3 main.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. The sample harness also raises until you implement the function. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
