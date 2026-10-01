"""Reference solution.

Sort outgoing edges in reverse order so pop chooses the smallest destination. Perform iterative Hierholzer traversal, adding nodes only after exhausting outgoing edges. Reverse the completed traversal. Validate the resulting edge multiset as well as its length; disconnected or non-Eulerian graphs must not produce a spurious answer.

Time: O(E log(E + 1)). Auxiliary space: O(E + 1), including adjacency lists, traversal stack, and validation counters.
"""

from __future__ import annotations
from collections import Counter, defaultdict


def reconstruct_trace(transitions: list[tuple[str, str]], start: str) -> list[str]:
    outgoing = defaultdict(list)
    for source, destination in transitions:
        outgoing[source].append(destination)
    for destinations in outgoing.values():
        destinations.sort(reverse=True)
    stack = [start]
    reverse_trace = []
    while stack:
        node = stack[-1]
        if outgoing[node]:
            stack.append(outgoing[node].pop())
        else:
            reverse_trace.append(stack.pop())
    trace = reverse_trace[::-1]
    # Length alone cannot reject every impossible directed graph.
    if len(trace) != len(transitions) + 1 or Counter(zip(trace, trace[1:])) != Counter(transitions):
        raise ValueError("no complete trace exists from the given start")
    return trace
