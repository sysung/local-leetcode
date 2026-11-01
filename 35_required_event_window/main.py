from __future__ import annotations


def shortest_event_window(events: list[str], required: list[str]) -> tuple[int, int] | None:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = (['view', 'noise', 'buy', 'view', 'buy'], ['view', 'buy'])
    expected = (2, 4)
    actual = shortest_event_window(*args)
    print(actual == expected, actual)
