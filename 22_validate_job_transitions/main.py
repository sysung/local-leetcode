from __future__ import annotations


def validate_job_history(events: list[tuple[str, str]]) -> tuple[dict[str, str], list[int]]:
    """Implement the problem described in README.md."""
    states = {}
    rejected_indices = []
    TRANSITIONS = {
        "QUEUED": ["RUNNING", "CANCELLED"],
        "RUNNING": ["SUCCEEDED", "FAILED", "CANCELLED"],
        "SUCCEEDED": "",
        "FAILED": "",
        "CANCELLED": ""
    }

    for idx, e in enumerate(events):
        
        cur_job_id = e[0]
        cur_state = e[1]
        # print(states)
        # if cur_job_id in states:
        #     print(TRANSITIONS[states[cur_job_id]])
        #     print(cur_state)

        # Start of a new event
        if (cur_job_id not in states and cur_state == "QUEUED") or (cur_job_id in states and cur_state in TRANSITIONS[states[cur_job_id]]):
            states[e[0]] = e[1]
        else:
            rejected_indices.append(idx)

    return (states, rejected_indices)


if __name__ == "__main__":
    args = ([('a', 'RUNNING'), ('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'FAILED'), ('a', 'QUEUED')],)
    expected = ({'a': 'FAILED'}, [0, 4])
    actual = validate_job_history(*args)
    print(expected == actual, actual)
