from __future__ import annotations

from bisect import bisect_right


class TimeMap:
    """Parallel per-key arrays: amortized O(1) append, O(log m) lookup."""

    def __init__(self) -> None:
        self._history: dict[str, tuple[list[int], list[str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        times, values = self._history.setdefault(key, ([], []))
        if times and timestamp <= times[-1]:
            raise ValueError("timestamps must increase per key")
        times.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str | None:
        if key not in self._history:
            return None
        times, values = self._history[key]
        index = bisect_right(times, timestamp) - 1
        return values[index] if index >= 0 else None
