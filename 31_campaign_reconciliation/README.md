---
type: coding-practice
difficulty: easy
created: 2026-11-01
updated: 2026-11-01
---
# Reconcile campaign event counts

**Difficulty:** Easy  
**DSA skills:** Hash maps, multisets, reconciliation

## Problem

A campaign ingestion audit compares raw source rows with destination rows without hiding duplicate delivery.

Implement `reconcile_campaign_events(source, destination)`.

- Both arguments are lists of `(campaign_id, event_id)` tuples of nonempty strings. Each tuple is an event key. One event ID can occur in different campaigns.
- Treat each list as a multiset. Every duplicate row contributes one count.
- Return `(campaign_id, event_id, source_count, destination_count)` tuples only for keys whose counts differ, sorted by `(campaign_id, event_id)`.
- A key missing on one side has count 0 on that side. Equal counts produce no discrepancy, even if both exceed 1.

## Example 1

Input (positional arguments):

```python
([('c', 'e1'), ('c', 'e1'), ('c', 'e2')], [('c', 'e1'), ('c', 'e3')])
```

Output:

```python
[('c', 'e1', 2, 1), ('c', 'e2', 1, 0), ('c', 'e3', 0, 1)]
```

**Explanation:** Count each event key on both sides, including repeated rows:

| Event key | Source count | Destination count |
| --- | --- | --- |
| `('c', 'e1')` | 2 | 1 |
| `('c', 'e2')` | 1 | 0 |
| `('c', 'e3')` | 0 | 1 |

All three keys have different counts, so report all three in event-key order.

## Example 2

Input (positional arguments):

```python
([('c', 'e'), ('c', 'e')], [('c', 'e'), ('c', 'e')])
```

Output:

```python
[]
```

**Explanation:** The key `('c', 'e')` appears twice in the source and twice in the destination. Duplicate rows count, but the counts agree at `2`. There is no discrepancy to report, so return `[]`.

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
