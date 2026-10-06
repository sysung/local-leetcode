"""Reference solution.

Use a transition table and one current-state entry per accepted job. Check membership before changing state.
Time: O(n). Auxiliary space: O(j), excluding rejected-index output, where j is accepted job count.
"""

from __future__ import annotations

def validate_job_history(events: list[tuple[str, str]]) -> tuple[dict[str, str], list[int]]:
    allowed = {None: {"QUEUED"}, "QUEUED": {"RUNNING", "CANCELLED"},
               "RUNNING": {"SUCCEEDED", "FAILED", "CANCELLED"}}
    states = {}
    rejected = []
    for index, (job, state) in enumerate(events):
        if state in allowed.get(states.get(job), set()):
            states[job] = state
        else:
            rejected.append(index)
    return states, rejected
