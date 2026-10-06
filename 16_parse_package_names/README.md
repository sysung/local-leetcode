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

A package name follows `group_item_revision_result_timestamp.zip`. The group and item each contain one or more ASCII letters, digits, or hyphens. Revision and timestamp each contain one or more ASCII digits and represent nonnegative integers. Result is exactly `PASS` or `FAIL`; the extension is exactly lowercase `.zip`. Return a dictionary with keys `group`, `item`, `revision`, `result`, and `timestamp`, converting the two numeric fields to integers. Return `None` if any part is invalid. Validate the whole input: surrounding whitespace, extra fields, directory prefixes, and trailing text are invalid. Leading zeroes in numeric fields are valid. Treat timestamp as an integer, with no calendar interpretation.

## Function signature

```python
def parse_package_name(name: str) -> dict[str, str | int] | None:
    ...
```

## Example 1

Input (positional arguments):

```python
('team-A_unit7_003_PASS_0012.zip',)
```

Output:

```python
{'group': 'team-A', 'item': 'unit7', 'revision': 3, 'result': 'PASS', 'timestamp': 12}
```

**Explanation:** Leading zeroes are accepted and removed by integer conversion.

## Example 2

Input (positional arguments):

```python
('team_unit_2_pass_12.zip',)
```

Output:

```python
None
```

**Explanation:** Result matching is case-sensitive.

## Constraints

Name length is at most 200 characters, including the extension. Numeric fields have at most 18 digits in otherwise valid names.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
