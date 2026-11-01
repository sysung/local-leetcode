from __future__ import annotations


def reconcile_campaign_events(source: list[tuple[str, str]], destination: list[tuple[str, str]]) -> list[tuple[str, str, int, int]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('c', 'e1'), ('c', 'e1'), ('c', 'e2')], [('c', 'e1'), ('c', 'e3')])
    expected = [('c', 'e1', 2, 1), ('c', 'e2', 1, 0), ('c', 'e3', 0, 1)]
    actual = reconcile_campaign_events(*args)
    print(actual == expected, actual)
