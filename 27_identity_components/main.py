from __future__ import annotations


def resolve_identities(links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Implement the problem described in README.md."""
    seen = {} # Keys = ID, Value = graph_id
    max_graphs = 0
    graph_lowest_id = {} # Keys = graph_id, Value = id
    for l in links:
        left = l[0]
        right = l[1]

        if left not in seen:
            # Left not seen, right seen
            if right in seen:
                seen[left] = seen[right]
                graph_lowest_id[seen[right]] = min(graph_lowest_id[seen[right]], left)
            # Both not seen
            else:
                seen[left] = max_graphs
                seen[right] = max_graphs
                max_graphs += 1
                graph_lowest_id[seen[left]] = min(left, right)
        else:
            # Left seen, right not seen
            if left in seen:
                seen[right] = seen[left]
                graph_lowest_id[seen[left]] = min(graph_lowest_id[seen[left]], right)

    retval = [(id, graph_lowest_id[seen[id]]) for id in seen]

    return sorted(retval, key=lambda x: x[0])

if __name__ == "__main__":
    args = ([('email:a', 'cookie:b'), ('customer:c', 'email:a'), ('orphan', 'orphan')],)
    expected = [('cookie:b', 'cookie:b'), ('customer:c', 'cookie:b'), ('email:a', 'cookie:b'), ('orphan', 'orphan')]
    actual = resolve_identities(*args)
    print(actual == expected, actual)
