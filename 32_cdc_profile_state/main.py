from __future__ import annotations


def materialize_profiles(changes: list[tuple[str, int, str, str | None]]) -> list[tuple[str, int, str]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('a', 2, 'upsert', 'new'), ('a', 1, 'upsert', 'old'), ('b', 4, 'delete', None), ('b', 3, 'upsert', 'stale')],)
    expected = [('a', 2, 'new')]
    actual = materialize_profiles(*args)
    print(actual == expected, actual)
