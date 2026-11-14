from __future__ import annotations

from collections import Counter


def shortest_event_window(events: list[str], required: list[str]) -> tuple[int, int] | None:
    """Return the shortest qualifying window using counts and two boundaries."""
    if not required:
        return (0, 0)
    # Positive counts mean we need more; negative counts mean we have extras.
    needed = Counter(required)
    missing = len(required)  # Missing occurrences, including repeated requirements.

    left = 0
    right = 0
    best = None
    # The window is events[left:right], with right just past its last event.
    # Even at the end of input, finish shrinking a valid window.
    while right < len(events) or missing == 0:
        # Expand until all required occurrences are present or input runs out.
        while right < len(events) and missing > 0:
            event = events[right]
            if event in needed:
                if needed[event] > 0:
                    missing -= 1
                needed[event] -= 1
            right += 1

        # Shrink valid windows. Noise can be skipped even in an invalid window.
        while left < right and (missing == 0 or events[left] not in needed):
            if missing == 0:
                # Record before removing anything. Equal lengths keep the earlier start.
                candidate = (left, right)
                if best is None or candidate[1] - candidate[0] < best[1] - best[0]:
                    best = candidate
            outgoing = events[left]
            left += 1
            if outgoing in needed:
                needed[outgoing] += 1
                # Removing an extra occurrence is safe; removing a needed one is not.
                if needed[outgoing] > 0:
                    missing += 1
    return best


if __name__ == "__main__":
    args = (['view', 'noise', 'buy', 'view', 'buy'], ['view', 'buy', 'view'])
    expected = (0, 4)
    actual = shortest_event_window(*args)
    print(actual == expected, actual)
