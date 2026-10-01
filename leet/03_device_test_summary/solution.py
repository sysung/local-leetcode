"""Reference solution.

Use a hash map for per-device counters, then derive each pass rate from its totals.

Time: O(n). Auxiliary space: O(d) including output, for d distinct devices.
"""

from __future__ import annotations


def summarize_tests(records: list[dict[str, str]]) -> dict[str, dict[str, int | float]]:
    summary = {}
    for record in records:
        device = record["device_id"]
        counts = summary.setdefault(device, {"total": 0, "failures": 0})
        counts["total"] += 1
        counts["failures"] += record["status"] == "FAIL"
    for counts in summary.values():
        counts["pass_rate"] = (counts["total"] - counts["failures"]) / counts["total"]
    return summary
