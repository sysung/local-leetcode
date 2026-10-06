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

Parse a single log line containing whitespace-separated `key=value` fields into a dictionary. Keys match `[a-z][a-z0-9_]*`. A value is either a nonempty unquoted sequence containing no whitespace or double quotes, or a double-quoted sequence that may contain spaces and may be empty. An equals sign is allowed inside either form of value. Quoted values must be entirely enclosed: text immediately before or after the quotes is invalid. Whitespace may appear between fields and at either end, but not between a key and its equals sign or between the equals sign and its value. Repeated keys use the last value. Remove enclosing quotes and preserve all other value characters exactly. Return `{}` for an empty or whitespace-only line, and `None` if any field is invalid; do not return a partial record. No escaping syntax is supported.

## Function signature

```python
def parse_fields(line: str) -> dict[str, str] | None:
    ...
```

## Example 1

Input (positional arguments):

```python
('id=a message="sensor too hot" code=X=7',)
```

Output:

```python
{'id': 'a', 'message': 'sensor too hot', 'code': 'X=7'}
```

**Explanation:** Quoted whitespace stays inside a value; equals signs need no special treatment.

## Example 2

Input (positional arguments):

```python
('id=a id=b note=""',)
```

Output:

```python
{'id': 'b', 'note': ''}
```

**Explanation:** The last duplicate wins and quoted empty values are valid.

## Constraints

Line length is at most 100,000 characters. Input contains no carriage returns, newlines, or backslashes. Whitespace means a character for which `str.isspace()` is True.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
