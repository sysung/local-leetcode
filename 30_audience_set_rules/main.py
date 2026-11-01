from __future__ import annotations


def build_audience(universe: list[str], required_groups: list[list[str]], excluded: list[str]) -> list[str]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = (['a', 'b', 'c', 'd'], [['a', 'b', 'c'], ['b', 'c', 'd']], ['c'])
    expected = ['b']
    actual = build_audience(*args)
    print(actual == expected, actual)
