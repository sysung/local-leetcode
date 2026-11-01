"""Reference solution.

Build an undirected adjacency map, traverse each component once, and assign its smallest
ID to every member. Iteration avoids recursion limits on long chains. For v distinct IDs
and e links, time is O(e + v log(v + 1)) and auxiliary
space is O(v + e), excluding the output.
"""

from __future__ import annotations


def resolve_identities(links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    neighbors = {}
    for left, right in links:
        neighbors.setdefault(left, set()).add(right)
        neighbors.setdefault(right, set()).add(left)
    canonical = {}
    for start in neighbors:
        if start in canonical:
            continue
        component = []
        pending = [start]
        canonical[start] = start
        while pending:
            current = pending.pop()
            component.append(current)
            for neighbor in neighbors[current]:
                if neighbor not in canonical:
                    canonical[neighbor] = start
                    pending.append(neighbor)
        root = min(component)
        for identifier in component:
            canonical[identifier] = root
    return sorted(canonical.items())
