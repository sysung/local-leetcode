"""Reference solution.

Binary-search the allowed maximum batch sum. Greedily pack each batch until another load would exceed the limit. If at most the requested number of batches suffice, the limit is feasible: nonnegative loads let us subdivide to reach exactly the requested count without increasing the maximum.

Time: O(n log(S + 1)), where S is total load. Auxiliary space: O(1).
"""

from __future__ import annotations


def minimize_max_batch_load(loads: list[int], batch_count: int) -> int:
    if not loads or not 1 <= batch_count <= len(loads) or any(load < 0 for load in loads):
        raise ValueError("loads must be nonnegative and the batch count valid")
    low, high = max(loads), sum(loads)
    while low < high:
        limit = (low + high) // 2
        batches = 1
        current = 0
        for load in loads:
            if current + load > limit:
                batches += 1
                current = 0
            current += load
        if batches <= batch_count:
            high = limit
        else:
            low = limit + 1
    return low
