"""Reference solution.

Build adjacency lists and indegrees, then run Kahn's topological sort. A min-heap selects the smallest available task. Unprocessed tasks indicate a cycle.

Time: O(P + V log V), where P includes all listed prerequisites and V is the number of tasks. Auxiliary space: O(V + E) for distinct dependency edges E.
"""

from __future__ import annotations
import heapq


def order_tasks(dependencies: dict[str, list[str]]) -> list[str]:
    tasks = set(dependencies)
    for prerequisites in dependencies.values():
        tasks.update(prerequisites)
    outgoing = {task: [] for task in tasks}
    indegree = {task: 0 for task in tasks}
    for task, prerequisites in dependencies.items():
        for prerequisite in set(prerequisites):
            outgoing[prerequisite].append(task)
            indegree[task] += 1
    available = [task for task in tasks if indegree[task] == 0]
    heapq.heapify(available)
    ordered = []
    while available:
        task = heapq.heappop(available)
        ordered.append(task)
        for dependent in outgoing[task]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(available, dependent)
    if len(ordered) != len(tasks):
        raise ValueError("dependency cycle")
    return ordered
