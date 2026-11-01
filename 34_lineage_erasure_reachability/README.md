---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Find datasets affected by an erasure

**Difficulty:** Medium  
**DSA skills:** Directed graphs, reachability, cycle detection

## Problem

A privacy workflow must identify every downstream dataset that can contain data derived from an erasure source.

Implement `erasure_scope(edges, roots)`.

- `edges` is a list of `(upstream_dataset, downstream_dataset)` tuples of nonempty strings. Each directed edge means the downstream dataset derives data from the upstream dataset.
- `roots` is a list of nonempty dataset ID strings that require erasure. Include each root even if it never appears in an edge.
- Return all distinct roots and all datasets reachable by following zero or more downstream edges, sorted lexicographically.
- Do not follow edges upstream. Cycles, self-edges, duplicate edges, and duplicate roots are valid. Visit each dataset at most once. Empty roots produce `[]`.
- This function computes scope only. It does not delete data.

## Example 1

Input (positional arguments):

```python
([('raw', 'profiles'), ('profiles', 'audience'), ('raw', 'audit')], ['raw'])
```

Output:

```python
['audience', 'audit', 'profiles', 'raw']
```

**Explanation:** Starting at `raw`, follow its downstream edges:

```text
raw -> profiles -> audience
  |
  +--> audit
```

Include `raw` itself, its direct downstream datasets `profiles` and `audit`, and the indirectly reachable `audience`. Return the four distinct names in lexicographic order, rather than traversal order.

## Example 2

Input (positional arguments):

```python
([('a', 'b'), ('b', 'c'), ('c', 'a')], ['b'])
```

Output:

```python
['a', 'b', 'c']
```

**Explanation:** Starting at `b`, follow `b -> c -> a`. The edge `a -> b` returns to a dataset already reached, so it adds no new dataset. Include each of `a`, `b`, and `c` once and return them in sorted order.

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
