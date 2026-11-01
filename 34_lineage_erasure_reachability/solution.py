"""Reference solution.

Build an adjacency map that preserves edge direction, then traverse downstream with a
visited set. For e edges and r root rows, with v distinct reachable datasets, expected
time is O(e + r + v log(v + 1)) and auxiliary space is O(e + r + v), excluding the
output.
"""

from __future__ import annotations


def erasure_scope(edges: list[tuple[str, str]], roots: list[str]) -> list[str]:
    downstream = {}
    for upstream, child in edges:
        downstream.setdefault(upstream, set()).add(child)
    reached = set(roots)
    pending = list(reached)
    while pending:
        dataset = pending.pop()
        for child in downstream.get(dataset, ()):
            if child not in reached:
                reached.add(child)
                pending.append(child)
    return sorted(reached)
