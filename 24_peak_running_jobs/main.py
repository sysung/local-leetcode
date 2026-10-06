from __future__ import annotations


def peak_concurrency(intervals: list[tuple[int, int]]) -> int:
    """Implement the problem described in README.md."""
    changes = {}
    for start, end in intervals:
        changes[start] = changes.get(start, 0) + 1
        changes[end] = changes.get(end, 0) - 1
    print(changes)

    active = 0
    peak = 0
    for ts in sorted(changes):
        active += changes[ts]
        peak = max(peak, active)
    return peak
    
if __name__ == "__main__":
    args = ([(0, 10), (2, 8), (3, 4)],)
    expected = 3
    actual = peak_concurrency(*args)

    print(actual == expected, actual)
