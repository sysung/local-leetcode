from __future__ import annotations


def sessionize(events: list[tuple[str, int, str]], timeout: int) -> list[tuple[str, int, int, int, int]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('u', 0, 'a'), ('u', 5, 'b'), ('u', 11, 'c')], 5)
    expected = [('u', 1, 0, 5, 2), ('u', 2, 11, 11, 1)]
    actual = sessionize(*args)
    print(actual == expected, actual)
