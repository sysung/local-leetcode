from __future__ import annotations
from collections.abc import Iterable


def aggregate_event_time(events: Iterable[tuple[int, str, str]], window_size: int, allowed_lateness: int) -> tuple[list[tuple[int, str, int, int]], list[int]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError("Complete this practice problem")
