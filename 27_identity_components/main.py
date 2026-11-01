from __future__ import annotations


def resolve_identities(identifiers: list[str], links: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Implement the problem described in README.md."""
    raise NotImplementedError


if __name__ == "__main__":
    args = (['orphan'], [('email:a', 'cookie:b'), ('customer:c', 'email:a')])
    expected = [('cookie:b', 'cookie:b'), ('customer:c', 'cookie:b'), ('email:a', 'cookie:b'), ('orphan', 'orphan')]
    actual = resolve_identities(*args)
    print(actual == expected, actual)
