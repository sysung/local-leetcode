"""Reference solution.

Build a completion set per partition, then walk each prefix from its starting offset. A
prefix step consumes a distinct completed offset, so the total number of steps is at
most the number of completions. For n completions and p partitions, expected time is O(n
+ p log(p + 1)) and auxiliary space is O(n + p), excluding the output.
"""

from __future__ import annotations


def advance_offsets(next_offsets: dict[str, int], completed: list[tuple[str, int]]) -> dict[str, int]:
    done = {partition: set() for partition in next_offsets}
    for partition, offset in completed:
        done[partition].add(offset)
    result = {}
    for partition in sorted(next_offsets):
        offset = next_offsets[partition]
        while offset in done[partition]:
            offset += 1
        result[partition] = offset
    return result
