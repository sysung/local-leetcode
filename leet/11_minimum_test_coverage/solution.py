"""Reference solution.

Expand the right boundary until every required category is present. Shrink the left boundary while coverage remains complete. Only strictly shorter candidates replace the answer, preserving the earliest tie.

Time: O(n + r). Auxiliary space: O(r), for r required codes.
"""

from __future__ import annotations


def minimum_test_coverage(codes: list[str], required: set[str]) -> tuple[int, int] | None:
    if not required:
        return None
    counts = {}
    covered = 0
    left = 0
    best = None
    for right, code in enumerate(codes):
        if code in required:
            counts[code] = counts.get(code, 0) + 1
            if counts[code] == 1:
                covered += 1
        while covered == len(required):
            if best is None or right - left < best[1] - best[0]:
                best = (left, right)
            outgoing = codes[left]
            if outgoing in required:
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    covered -= 1
            left += 1
    return best
