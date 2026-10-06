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

Given a list of log-code strings and an ordered list of required codes, return inclusive `(start_index, end_index)` indices of the shortest contiguous log slice containing the required codes as a subsequence. Required codes must appear in order, but unrelated codes may lie between them. Each required occurrence needs a distinct log occurrence, including when required codes repeat. Minimize the number of log entries in the slice, breaking ties by earliest start. Return `None` if requirements are empty or no matching slice exists. Unlike a set-coverage problem, matching the right codes in the wrong order is insufficient.

## Function signature

```python
def shortest_ordered_match(codes: list[str], required: list[str]) -> tuple[int, int] | None:
    ...
```

## Example 1

Input (positional arguments):

```python
(['A', 'X', 'B', 'C', 'A', 'B', 'C'], ['A', 'B', 'C'])
```

Output:

```python
(4, 6)
```

**Explanation:** The later match has no intervening X, so its slice is shorter.

## Example 2

Input (positional arguments):

```python
(['A', 'B', 'A', 'B'], ['A', 'A', 'B'])
```

Output:

```python
(0, 3)
```

**Explanation:** Two distinct A occurrences are required.

## Constraints

At most 10,000 log codes and 100 required codes; strings are nonempty and at most 30 characters. Target O(n*m) time and O(m) auxiliary space, where n and m are list lengths; account for string comparison cost when discussing complexity.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
