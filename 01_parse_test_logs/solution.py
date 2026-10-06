"""Reference solution.

Split and validate each string once, appending only valid records to the result array.

Time: O(L), where L is total input text length. Auxiliary space: O(m) for the longest line, excluding the output.
"""

from __future__ import annotations


def parse_logs(lines: list[str]) -> list[dict[str, int | str]]:
    records = []
    for line in lines:
        fields = [field.strip() for field in line.split(",")]
        if len(fields) != 3:
            continue
        timestamp_text, device_id, status = fields
        digits = timestamp_text[1:] if timestamp_text.startswith(("+", "-")) else timestamp_text
        if not digits or any(char not in "0123456789" for char in digits):
            continue
        timestamp = int(timestamp_text)
        if timestamp < 0 or not device_id or status not in {"PASS", "FAIL"}:
            continue
        records.append({"timestamp": timestamp, "device_id": device_id, "status": status})
    return records
