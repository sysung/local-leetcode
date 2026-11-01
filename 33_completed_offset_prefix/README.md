---
type: coding-practice
difficulty: medium
created: 2026-11-01
updated: 2026-11-01
---
# Advance completed partition offsets

**Difficulty:** Medium  
**DSA skills:** Sets, contiguous prefixes, stream checkpoints

## Problem

A consumer processes records out of order. It may commit only the completed contiguous prefix for each partition.

Implement `advance_offsets(next_offsets, completed)`.

- `next_offsets` is a dictionary mapping nonempty partition ID strings to nonnegative integer offsets. Each value is the first offset not yet committed, not the last committed offset.
- `completed` is a list of `(partition_id, offset)` tuples. Each partition ID must occur in `next_offsets`. Offsets are nonnegative integers.
- For each partition, start at its supplied next offset and advance while that offset appears in `completed` for that partition. Stop at the first gap.
- Return a new dictionary with every original partition and its new next offset. Insert keys in lexicographic order.
- Duplicate completions have no additional effect. Completions below the starting offset are already committed and have no effect. Higher completions beyond a gap cannot advance the checkpoint.
- Do not modify the input dictionary or completion list.

## Example 1

Input (positional arguments):

```python
({'p0': 5}, [('p0', 7), ('p0', 5), ('p0', 8)])
```

Output:

```python
{'p0': 6}
```

**Explanation:** Partition `p0` starts at next offset `5`, meaning offsets below `5` are already committed. Offset `5` is completed, so advance to `6`. Offset `6` is missing, so stop there. Completed offsets `7` and `8` cannot bridge that gap.

```text
Offset:     5          6          7          8
Status:  completed   missing   completed   completed
                     ^ new next offset
```

## Example 2

Input (positional arguments):

```python
({'b': 10, 'a': 0}, [('a', 1), ('b', 10), ('a', 0), ('b', 12)])
```

Output:

```python
{'a': 2, 'b': 11}
```

**Explanation:** Partition `a` starts at `0`. Both `0` and `1` are completed, so advance to `2`, the first gap. Partition `b` starts at `10`. Offset `10` is completed, but `11` is missing, so stop at `11` despite completion `12`. Insert the result keys in alphabetical order, `a` before `b`.

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
