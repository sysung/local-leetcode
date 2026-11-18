from __future__ import annotations

from collections import defaultdict


def materialize_profiles(changes: list[tuple[str, int, str, str | None]]) -> list[tuple[str, int, str]]:
    """Implement the problem described in README.md."""
    profiles = {}
    # O(n)
    for c in changes:
        # New profile
        if c[0] not in profiles:  # noqa: SIM114
            profiles[c[0]] = c[1:]
        # New event overwrites
        elif c[1] > profiles[c[0]][0]:
            profiles[c[0]] = c[1:]
        # Tiebreaker timestamp 
        elif c[1] == profiles[c[0]][0]:
            # Current event is a deelete
            if profiles[c[0]][1] == 'delete':
                continue
            # New event is a delete
            elif c[2] == 'delete':  # noqa: SIM114
                profiles[c[0]] = c[1:]
            # New event is lexographically larger
            elif c[3] >= str(profiles[c[0]][2]): # type: ignore
                profiles[c[0]] = c[1:]

    # O(n)
    profile_state = []
    for id, state in profiles.items():
        if state[1] != 'delete':
            profile_state.append((id, state[0], state[2]))
            
    # O(nlogn)
    return sorted(profile_state)


if __name__ == "__main__":
    args = ([('a', 1, 'delete', None), ('a', 1, 'upsert', 'zz')],)
    expected = []
    actual = materialize_profiles(*args)
    print(actual == expected, actual)
