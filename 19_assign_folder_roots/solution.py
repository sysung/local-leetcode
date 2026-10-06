"""Reference solution.

Build a trie of manifest directory components. While walking a measurement's directory components, remember the deepest marked root. Empty-string roots are distinct from None.
Time: O(L). Auxiliary space: O(L), where L is total path length, excluding output.
"""

from __future__ import annotations

def assign_roots(manifest_paths: list[str], measurement_paths: list[str]) -> dict[str, str | None]:
    trie = {}
    marker = object()
    for path in manifest_paths:
        parts = path.split("/")[:-1]
        node = trie
        for part in parts:
            node = node.setdefault(part, {})
        node[marker] = "/".join(parts)
    output = {}
    for path in measurement_paths:
        node = trie
        owner = node.get(marker)
        for part in path.split("/")[:-1]:
            if part not in node:
                break
            node = node[part]
            if marker in node:
                owner = node[marker]
        output[path] = owner
    return output
