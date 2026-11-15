"""Reference solution using list indices and a min-heap.

Keep the next event's position for each nonempty list in the heap.
Stream index breaks timestamp ties; event position preserves internal order.
Time: O(s + n log(s + 1)) for n events across s streams.
Space: O(s) heap storage plus O(n) returned output, O(s + n) total extra.
"""

from __future__ import annotations
import heapq


def merge_streams(streams: list[list[tuple[int, str]]]) -> list[tuple[int, str]]:
    heap = [(stream[0][0], index, 0) for index, stream in enumerate(streams) if stream]
    heapq.heapify(heap)
    result: list[tuple[int, str]] = []
    while heap:
        _, stream_index, event_index = heapq.heappop(heap)
        result.append(streams[stream_index][event_index])
        following = event_index + 1
        if following < len(streams[stream_index]):
            timestamp = streams[stream_index][following][0]
            heapq.heappush(heap, (timestamp, stream_index, following))
    return result

if __name__ == "__main__":
    args = ([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
    expected = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    actual = merge_streams(*args)
    print(expected == actual, actual)
