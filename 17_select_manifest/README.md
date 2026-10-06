---
type: coding-practice
difficulty: easy
created: 2026-10-05
updated: 2026-10-05
---
# Choose the Preferred Manifest

**Difficulty:** Easy  
**DSA skills:** Tuple ordering, linear scanning, path components

## Problem

You are given a list of relative file paths, `paths`.

Return the preferred path, choosing filenames in this priority order: `manifest.json`, `summary.txt`, then `output.txt`.

- Filename priority comes before location.
- For the same filename, choose the path with the fewest directory components.
- If still tied, choose the lexicographically smallest full path using Python string ordering.
- Match filenames exactly and case-sensitively; ignore other filenames.
- Return `None` if no recognized file exists. Use only the supplied path strings.

## Example 1

Input (positional arguments):

```python
(['summary.txt', 'z/deep/manifest.json', 'a/manifest.json'],)
```

Output:

```python
'a/manifest.json'
```

**Explanation:** A manifest outranks a summary, then the shallower manifest wins.

## Example 2

Input (positional arguments):

```python
(['z/summary.txt', 'a/summary.txt', 'README.txt'],)
```

Output:

```python
'a/summary.txt'
```

**Explanation:** Equal priority and depth are resolved by the full path.

## Constraints

At most 100,000 unique paths, each at most 200 characters. Paths use `/`, have nonempty components, and contain no leading/trailing slash, `.` component, or `..` component. Every entry is a file.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
