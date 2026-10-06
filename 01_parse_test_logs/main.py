from __future__ import annotations


def parse_logs(lines: list[str]) -> list[dict[str, int | str]]:
    """Implement the problem described in README.md."""
    output = []
    for l in lines:
        # Strips leading and preceding whitespace
        records = [i.strip() for i in l.split(",")]
        # Checks if input has exactly 3 inputs
        if len(records) != 3:
            continue
        # Only accounts PASS or FAIL
        if records[2] not in ("PASS", "FAIL"):
            continue
        # Timestamp must be nonnegative ASCII digits, with an optional sign.
        digits = records[0][1:] if records[0].startswith(("+", "-")) else records[0]
        if not digits.isascii() or not digits.isdigit() or int(records[0]) < 0:
            continue
        # Device must be a non-empty string
        if not records[1].isascii() or str(records[1]) == "":
            continue

        timestamp = int(records[0])
        device_id = records[1]
        status = records[2]
        output.append({
            "device_id": device_id,
            "status": status,
            "timestamp": timestamp
        })
    return output

if __name__ == "__main__":
    logs = ['-1,gpu,PASS', '1,,PASS', '1,gpu,pass', '1.5,gpu,FAIL']
    expected = []

    actual = parse_logs(logs)

    print()
    print(actual == expected)
    print(actual)
