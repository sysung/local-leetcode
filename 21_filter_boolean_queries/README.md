---
type: coding-practice
difficulty: hard
created: 2026-10-05
updated: 2026-10-05
---
# Filter Records with a Boolean Query

**Difficulty:** Hard  
**DSA skills:** Stacks, expression parsing, operator precedence, sets

## Problem

You are given label sets, `records`, and a Boolean expression, `query`.

Return the zero-based indices of records that satisfy the query, in input order. A label is true if it is present in that record.

- Labels match `[a-z][a-z0-9_]*`.
- Operators are `!` (NOT), `&` (AND), and `|` (OR), from highest to lowest precedence. AND and OR associate left-to-right.
- Parentheses override precedence, and repeated NOT operators are allowed.
- Ignore whitespace between tokens, but do not allow it inside a label. Operators must be explicit: `a b` and `a(b)` are invalid.
- Raise `ValueError` for an empty query, illegal characters, missing operands or operators, or unmatched parentheses, even if `records` is empty.
- Do not use `eval`. Support nesting deeper than Python's recursion limit.

## Example 1

Input (positional arguments):

```python
([{'ready', 'failed'}, {'ready'}, {'urgent'}, set()], 'ready & !failed | urgent')
```

Output:

```python
[1, 2]
```

**Explanation:** AND binds more tightly than OR.

## Example 2

Input (positional arguments):

```python
([{'a'}, {'b'}, set()], '!(a | b)')
```

Output:

```python
[2]
```

**Explanation:** The parentheses make NOT apply to the entire disjunction.

## Constraints

At most 10,000 records, 100 labels per record, and 10,000 query characters. Record labels follow the same label syntax. Whitespace means `str.isspace()`.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
