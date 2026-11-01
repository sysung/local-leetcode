from __future__ import annotations


def latest_consent(events: list[tuple[str, str, int, bool]], as_of: int) -> list[tuple[str, str, int, bool]]:
    """Implement the problem described in README.md."""
    '''
    SELECT 
        user_id,
        purpose,
        ts,
        granted
    FROM consent
    WHERE ts < as_of
    GROUP BY user_id
    HAVING ts = MAX(ts) -- or use window function
    '''
    id_purpose = {}
    for e in events:
        e_key = (e[0], e[1])
        if (
            (e_key not in id_purpose and e[2] <= as_of) or 
            (e_key in id_purpose and e[2] >= id_purpose[e_key][2] and e[2] <= as_of)
        ):
            id_purpose[e_key] = e

    return sorted(id_purpose.values(), key=lambda x: (x[0], x[1]))


if __name__ == "__main__":
    args = ([('u1', 'ads', 4, True), ('u1', 'ads', 9, False), ('u1', 'email', 5, True)], 10)
    expected = [('u1', 'ads', 9, False), ('u1', 'email', 5, True)]
    actual = latest_consent(*args)
    print(actual == expected, actual)
