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

Given relative file paths from an archive, return the preferred manifest path or `None` if none exists. Recognize exact basenames `manifest.json`, `summary.txt`, and `output.txt`, in that order of priority. Filename priority takes precedence over location. Within the same filename, prefer the path with the fewest directory components; if still tied, choose the lexicographically smallest full path using Python string ordering. Ignore every other basename. Paths are case-sensitive. Operate on the supplied strings; do not open an archive or access the filesystem.

## Function signature

```python
def select_manifest(paths: list[str]) -> str | None:
    ...
```

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
