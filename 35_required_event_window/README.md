---
type: coding-practice
difficulty: hard
created: 2026-11-01
updated: 2026-11-01
---
# Find the shortest qualifying event window

**Difficulty:** Hard  
**DSA skills:** Sliding windows, frequency counts, multisets

## Problem

A funnel investigation needs the shortest contiguous stretch of a user's ordered event stream that contains all required event occurrences.

Implement `shortest_event_window(events, required)`.

- `events` and `required` are lists of nonempty event-type strings. `events` already has the desired stream order. Do not sort it.
- Return a half-open index pair `(start, end)` such that `events[start:end]` contains every required event type at least as many times as it occurs in `required`.
- Duplicate requirements matter. For example, `["view", "view", "buy"]` requires two views and one buy. Their relative order inside the window does not matter.
- Minimize the number of event rows, `end - start`. On a tie, choose the smaller start index.
- Return `None` when no qualifying window exists. An empty `required` returns `(0, 0)`, including when `events` is empty. Irrelevant events count toward window length.

## Example 1

Input (positional arguments):

```python
(['view', 'noise', 'buy', 'view', 'buy'], ['view', 'buy'])
```

Output:

```python
(2, 4)
```

## Example 2

Input (positional arguments):

```python
(['view', 'buy', 'view', 'noise', 'view'], ['view', 'view', 'buy'])
```

Output:

```python
(0, 3)
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
