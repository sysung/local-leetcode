---
type: coding-practice
difficulty: medium
created: 2026-10-05
updated: 2026-10-05
---
# Parse Quoted Key-Value Fields

**Difficulty:** Medium  
**DSA skills:** Tokenization, strings, hash maps

## Problem

You are given a log string, `line`, containing whitespace-separated `key=value` fields.

Return a dictionary of keys and string values. Return `None` if any field is invalid, or `{}` if the line is empty or contains only whitespace.

- Keys match `[a-z][a-z0-9_]*`.
- Unquoted values are nonempty and contain no whitespace or double quotes.
- Double-quoted values may contain whitespace or be empty. Remove only the enclosing quotes; no escaping is supported.
- Values may contain `=`. Quoted values cannot have text immediately before or after the quotes.
- Allow whitespace between fields and at either end, but not around a field's `=` separator.
- Repeated keys keep the last value. Preserve all other value characters and never return a partial record.

## Example 1

Input (positional arguments):

```python
('id=a message="sensor too hot" code=X=7',)
```

Output:

```python
{'id': 'a', 'message': 'sensor too hot', 'code': 'X=7'}
```

**Explanation:** The line contains three fields. `id=a` gives value `a`. The quotes in `message="sensor too hot"` keep the spaces inside one value, then the enclosing quotes are removed. In `code=X=7`, the first `=` separates the key from the value, so the value is `X=7`.

## Example 2

Input (positional arguments):

```python
('id=a id=b note=""',)
```

Output:

```python
{'id': 'b', 'note': ''}
```

**Explanation:** The first field sets `id` to `a`, and the second replaces it with `b` because the last duplicate wins. The field `note=""` is valid and gives an empty string. Return both keys with those final values.

## Constraints

Line length is at most 100,000 characters. Input contains no carriage returns, newlines, or backslashes. Whitespace means a character for which `str.isspace()` is True.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
