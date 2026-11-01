from __future__ import annotations


def attribute_last_touch(touches: list[tuple[str, int, str]], conversions: list[tuple[str, str, int]], lookback: int) -> list[tuple[str, str | None]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('u', 1, 'old'), ('u', 8, 'new'), ('u', 12, 'future')], [('c1', 'u', 10)], 5)
    expected = [('c1', 'new')]
    actual = attribute_last_touch(*args)
    print(actual == expected, actual)
