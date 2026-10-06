"""Reference solution.

Maintain one heap entry per nonempty stream. Yield the smallest head, then replace it with the next event from the same iterator. Stream index supplies the tie-break.

Time: O(s + n log(s + 1)) for n events across s streams. Auxiliary space: O(s).
"""

from __future__ import annotations
from collections.abc import Iterable, Iterator
import heapq


def merge_streams(streams: list[Iterable[tuple[int, str]]]) -> Iterator[tuple[int, str]]:
    iterators = [iter(stream) for stream in streams]
    heap = []
    for index, stream in enumerate(iterators):
        event = next(stream, None)
        if event is not None:
            heap.append((event[0], index, event))
    heapq.heapify(heap)
    while heap:
        _, index, event = heapq.heappop(heap)
        yield event
        following = next(iterators[index], None)
        if following is not None:
            heapq.heappush(heap, (following[0], index, following))
