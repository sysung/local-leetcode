from __future__ import annotations


def erasure_scope(edges: list[tuple[str, str]], roots: list[str]) -> list[str]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = ([('raw', 'profiles'), ('profiles', 'audience'), ('raw', 'audit')], ['raw'])
    expected = ['audience', 'audit', 'profiles', 'raw']
    actual = erasure_scope(*args)
    print(actual == expected, actual)
