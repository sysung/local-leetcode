from __future__ import annotations


def sessionize(events: list[tuple[str, int, str]], timeout: int) -> list[tuple[str, int, int, int, int]]:
    """Implement the problem described in README.md."""

    # Suppose n = len(events)

    # O(nlogn)
    ordered_events = sorted(events, key=lambda x: (x[0], x[1]))

    # Combine the user sessions O(n)
    sessions = {}
    for e in ordered_events:
        e_user_id = e[0]
        e_timestamp = e[1]
        if e_user_id not in sessions:
            # O(1)
            sessions[e_user_id] = [[e_timestamp, e_timestamp, 1]]
        else:
            last_session = sessions[e_user_id][-1]
            # O(1)
            if last_session[0] <= e_timestamp <= last_session[1] + timeout:
                # Set the latest session to be max of either the latest known event timestamp or the new event timestamp
                sessions[e_user_id][-1][1] = max(last_session[1], e_timestamp)
                sessions[e_user_id][-1][2] += 1
            else:
                sessions[e_user_id].append([e_timestamp, e_timestamp, 1])

    # Iterate through the sessions as a list orderd by user_id, then by session_number (O(n))
    sessions_list = []
    for user_id, session in sessions.items():
        for s_id, s in enumerate(session):
            sessions_list.append((user_id, s_id+1, s[0], s[1], s[2]))

    return sessions_list


if __name__ == "__main__":
    # args = ([('u', 0, 'a'), ('u', 5, 'b'), ('u', 11, 'c')], 5)
    # expected = [('u', 1, 0, 5, 2), ('u', 2, 11, 11, 1)]
    # actual = sessionize(*args)
    # print(actual == expected, actual)

    args = ([('b', 4, 'b1'), ('a', 9, 'a2'), ('a', 1, 'a1')], 10)
    expected = [('a', 1, 1, 9, 2), ('b', 1, 4, 4, 1)]
    actual = sessionize(*args)
    print(actual == expected, actual)
