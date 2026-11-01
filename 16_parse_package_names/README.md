---
type: coding-practice
difficulty: easy
created: 2026-10-05
updated: 2026-10-05
---
# Validate and Parse Package Names

**Difficulty:** Easy  
**DSA skills:** Strings, validation, regular expressions

## Problem

You are given a package filename, `name`, with the format `group_item_revision_result_timestamp.zip`.

Return a dictionary containing `group`, `item`, `revision`, `result`, and `timestamp`. Convert `revision` and `timestamp` to integers. Return `None` if the filename is invalid.

- `group` and `item` contain one or more ASCII letters, digits, or hyphens.
- `revision` and `timestamp` contain one or more ASCII digits; leading zeroes are allowed.
- `result` is exactly `PASS` or `FAIL`, and the extension is lowercase `.zip`.
- Reject surrounding whitespace, extra fields, directory prefixes, and trailing text.
- Treat the timestamp as an integer, not a calendar date.

## Example 1

Input (positional arguments):

```python
('team-A_unit7_003_PASS_0012.zip',)
```

Output:

```python
{'group': 'team-A', 'item': 'unit7', 'revision': 3, 'result': 'PASS', 'timestamp': 12}
```

**Explanation:** The five fields are group `team-A`, item `unit7`, revision `003`, result `PASS`, and timestamp `0012`. The filename has the required lowercase `.zip` extension. Convert revision `003` to integer `3` and timestamp `0012` to integer `12`. Keep the other fields as strings.

## Example 2

Input (positional arguments):

```python
('team_unit_2_pass_12.zip',)
```

Output:

```python
None
```

**Explanation:** The result field is `pass`, but only uppercase `PASS` or `FAIL` is valid. This makes the entire filename invalid, so return `None` rather than a partial dictionary.

## Constraints

Name length is at most 200 characters, including the extension. Numeric fields have at most 18 digits in otherwise valid names.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
