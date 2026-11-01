from __future__ import annotations


def advance_offsets(next_offsets: dict[str, int], completed: list[tuple[str, int]]) -> dict[str, int]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ({'p0': 5}, [('p0', 7), ('p0', 5), ('p0', 8)])
    expected = {'p0': 6}
    actual = advance_offsets(*args)
    print(actual == expected, actual)
