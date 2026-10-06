"""Reference solution.

Keep the lower half in a max-heap and upper half in a min-heap. Index readings so duplicates can expire independently. Logical heap sizes exclude expired entries; prune stale roots and rebalance so the lower half has at most one extra reading. Filter and heapify a heap whenever its physical size exceeds 2k, bounding retained stale data.

Time: O(n log(k + 1)) amortized. Auxiliary space: O(k), excluding the returned medians. Heap rebuilding adds O(n) amortized work.
"""

from __future__ import annotations
import heapq


def sliding_medians(values: list[int], k: int) -> list[float]:
    if not 1 <= k <= len(values):
        raise ValueError("k must be between 1 and the number of readings")
    lower = []  # Max-heap encoded as (-value, index).
    upper = []  # Min-heap encoded as (value, index).
    sides = {}  # Active index -> True for lower, False for upper.
    lower_size = upper_size = 0
    medians = []

    def prune(heap, is_lower):
        while heap and sides.get(heap[0][1]) != is_lower:
            heapq.heappop(heap)

    for index, value in enumerate(values):
        prune(lower, True)
        if not lower or value <= -lower[0][0]:
            heapq.heappush(lower, (-value, index))
            sides[index] = True
            lower_size += 1
        else:
            heapq.heappush(upper, (value, index))
            sides[index] = False
            upper_size += 1

        if index >= k:
            expired_side = sides.pop(index - k)
            if expired_side:
                lower_size -= 1
            else:
                upper_size -= 1
        prune(lower, True)
        prune(upper, False)

        while lower_size > upper_size + 1:
            negative, moved = heapq.heappop(lower)
            sides[moved] = False
            heapq.heappush(upper, (-negative, moved))
            lower_size -= 1
            upper_size += 1
            prune(lower, True)
        while lower_size < upper_size:
            positive, moved = heapq.heappop(upper)
            sides[moved] = True
            heapq.heappush(lower, (-positive, moved))
            upper_size -= 1
            lower_size += 1
            prune(upper, False)

        # Rebuild only after at least k stale entries can have accumulated.
        # Each heap remains O(k); each rebuild costs O(k) amortized.
        if len(lower) > 2 * k:
            lower = [entry for entry in lower if sides.get(entry[1]) is True]
            heapq.heapify(lower)
        if len(upper) > 2 * k:
            upper = [entry for entry in upper if sides.get(entry[1]) is False]
            heapq.heapify(upper)

        if index >= k - 1:
            if k % 2:
                medians.append(float(-lower[0][0]))
            else:
                medians.append((-lower[0][0] + upper[0][0]) / 2.0)
    return medians
