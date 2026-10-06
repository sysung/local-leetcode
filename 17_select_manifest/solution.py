"""Reference solution.

Track the minimum tuple (filename priority, directory depth, full path).
Time: O(L), where L is total path length. Auxiliary space: O(m), where m is maximum path length.
"""

from __future__ import annotations

def select_manifest(paths: list[str]) -> str | None:
    priorities = {"manifest.json": 0, "summary.txt": 1, "output.txt": 2}
    best = None
    for path in paths:
        basename = path.rsplit("/", 1)[-1]
        if basename in priorities:
            candidate = (priorities[basename], path.count("/"), path)
            if best is None or candidate < best:
                best = candidate
    return None if best is None else best[2]
