"""Reference solution.

Match one field at the current position, verify that the next character is whitespace or end-of-line, and continue. Full coverage prevents partial acceptance.
Time: O(L). Auxiliary space: O(L), including returned keys and values.
"""

from __future__ import annotations

import re


def parse_fields(line: str) -> dict[str, str] | None:
    field = re.compile(r'([a-z][a-z0-9_]*)=(?:"([^"]*)"|([^\s"]+))')
    output = {}
    index = 0
    while index < len(line):
        if line[index].isspace():
            index += 1
            continue
        match = field.match(line, index)
        if match is None:
            return None
        index = match.end()
        if index < len(line) and not line[index].isspace():
            return None
        key, quoted, bare = match.groups()
        output[key] = quoted if quoted is not None else bare
    return output
