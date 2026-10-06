---
type: coding-practice
difficulty: easy
created: 2026-10-05
updated: 2026-10-05
---
# Normalize Evolving Record Fields

**Difficulty:** Easy  
**DSA skills:** Hash maps, schema mapping, presence checks

## Problem

You are given a list of dictionaries, `records`, whose field names may differ.

Return one new dictionary per record, in input order, containing exactly `item_id`, `timestamp`, and `status`.

- For `item_id`, prefer `item_id`, then `id`.
- For `timestamp`, prefer `timestamp`, then `time`.
- For `status`, prefer `status`, then `result`.
- Use the first key that exists, even if its value is `None`, `0`, `False`, or `""`. If neither key exists, use `None`.
- Keep selected values unchanged and discard unrelated fields.

## Example 1

Input (positional arguments):

```python
([{'id': 'a', 'time': 0, 'result': 'PASS', 'extra': 9}],)
```

Output:

```python
[{'item_id': 'a', 'timestamp': 0, 'status': 'PASS'}]
```

**Explanation:** Legacy names map to the canonical fields.

## Example 2

Input (positional arguments):

```python
([{'item_id': None, 'id': 'fallback', 'status': '', 'result': 'PASS'}],)
```

Output:

```python
[{'item_id': None, 'timestamp': None, 'status': ''}]
```

**Explanation:** Presence takes precedence over truthiness.

## Constraints

At most 100,000 records. Record keys are strings and values are scalars: strings, integers, floats, booleans, or None.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
