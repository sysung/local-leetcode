from __future__ import annotations


def latest_consent(events: list[tuple[str, str, int, bool]], as_of: int) -> list[tuple[str, str, int, bool]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('u1', 'ads', 4, True), ('u1', 'ads', 9, False), ('u1', 'email', 5, True)], 10)
    expected = [('u1', 'ads', 9, False), ('u1', 'email', 5, True)]
    actual = latest_consent(*args)
    print(actual == expected, actual)
