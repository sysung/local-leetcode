---
type: coding-practice
difficulty: hard
created: 2026-10-05
updated: 2026-10-05
---
# Find the Shortest Ordered Log Match

**Difficulty:** Hard  
**DSA skills:** Dynamic programming, subsequences, reverse updates

## Problem

You are given two lists of strings, `codes` and `required`.

Return the inclusive `(start, end)` indices of the shortest contiguous slice of `codes` that contains the required codes in order. Other codes may appear between matches.

- Repeated required codes must match separate log entries.
- If multiple slices have the same length, choose the earliest start.
- Return `None` if `required` is empty or no match exists.

## Example 1

Input (positional arguments):

```python
(['A', 'X', 'B', 'C', 'A', 'B', 'C'], ['A', 'B', 'C'])
```

Output:

```python
(4, 6)
```

**Explanation:** Multiple slices can match, but return the shortest one:

- `(0, 3)` contains `["A", "X", "B", "C"]`: valid, length 4.
- `(4, 6)` contains `["A", "B", "C"]`: valid, length 3.
- `(3, 5)` contains `["C", "A", "B"]`: invalid, because the required codes do not appear in order.

Return `(4, 6)` because it is the shortest valid slice.

## Example 2

Input (positional arguments):

```python
(['A', 'B', 'A', 'B'], ['A', 'A', 'B'])
```

Output:

```python
(0, 3)
```

**Explanation:** Match `A` at indices 0 and 2, then `B` at index 3. The `B` at index 1 is skipped, so the required codes still appear in order within the slice `(0, 3)`.

## Example 3

Input (positional arguments):

```python
(['B', 'A'], ['A', 'B'])
```

Output:

```python
None
```

**Explanation:** Both codes exist, but `B` never appears after `A`, so the required order cannot be matched.

## Constraints

At most 10,000 log codes and 100 required codes; strings are nonempty and at most 30 characters. Target O(n*m) time and O(m) auxiliary space, where n and m are list lengths; account for string comparison cost when discussing complexity.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
