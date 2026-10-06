---
type: coding-practice
difficulty: medium
created: 2026-10-05
updated: 2026-10-05
---
# Assign Files to Their Nearest Manifest

**Difficulty:** Medium  
**DSA skills:** Tries, tree ancestry, path component matching

## Problem

You are given two lists of file paths: `manifest_paths` and `measurement_paths`. Each manifest is named `manifest.json`, and its parent directory defines a root.

Return a dictionary mapping each measurement path to the deepest root that contains it, or `None` if no root contains it.

- Nested roots take priority over their parent roots.
- Match whole directory components: `run` contains `run/log.txt`, but not `runner/log.txt`.
- Represent the archive root as `""`.
- All paths belong to the same archive. Use only the supplied strings.

## Example 1

Input (positional arguments):

```python
(['manifest.json', 'a/manifest.json', 'a/sub/manifest.json'], ['a/sub/x.txt', 'a/y.txt', 'b/z.txt'])
```

Output:

```python
{'a/sub/x.txt': 'a/sub', 'a/y.txt': 'a', 'b/z.txt': ''}
```

**Explanation:** Each measurement uses the deepest enclosing root.

## Example 2

Input (positional arguments):

```python
(['run/manifest.json'], ['run/x.txt', 'runner/x.txt'])
```

Output:

```python
{'run/x.txt': 'run', 'runner/x.txt': None}
```

**Explanation:** A string prefix alone does not establish directory ownership.

## Constraints

At most 100,000 paths across both lists and at most 2,000,000 total characters. Paths use `/`, have nonempty components, and contain no leading/trailing slash, `.` component, or `..` component. Measurement paths are unique; repeated manifest paths are allowed. A measurement path never names a directory containing another supplied file.

Do not modify caller-owned input collections. Assume valid inputs except for validation explicitly required above. Use Python 3.10 or later and only built-ins or standard-library modules.

## Practice

Implement `main.py`, then run from this problem's folder:

```bash
python3 -m unittest -v test_case.py
```

Tests import only `main.py`; the starter intentionally raises `NotImplementedError`. Compare with `solution.py` after your attempt. Explain your algorithm, boundary cases, and time/space complexity aloud.
