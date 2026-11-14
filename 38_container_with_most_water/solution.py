from __future__ import annotations

def max_area(heights: list[int]) -> int:
    """O(n) time, O(1) space; discard the shorter endpoint."""
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(heights[left], heights[right]))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best
