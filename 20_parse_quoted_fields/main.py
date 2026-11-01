from __future__ import annotations
import re

def parse_fields(line: str) -> dict[str, str] | None:
    split_line = re.split(r'[\" "\t]', line.strip())
    print(split_line)

    fields = {}
    quote_key = ""
    for curr_line in split_line:
        print(curr_line, "\t", fields)
        # Key and value are in the same block
        if "=" in curr_line:
            equal_idx = curr_line.find("=")
            # If the first "=" is not the last, then treat as a normal key-value pair
            if equal_idx != len(curr_line) - 1:
                key = curr_line[0:equal_idx]
                value = curr_line[equal_idx+1:]
                fields[key] = value
            # If first "=" is the last, then treat as separated key-value pair
            elif equal_idx == len(curr_line) - 1:
                quote_key = curr_line[:-1]
                fields[quote_key] = ""
                print(quote_key)
        # All of these values should append to the current quote_key
        else:
            if fields[quote_key] == "":
                fields[quote_key] = curr_line
            else:
                fields[quote_key] += f" {curr_line}"
        
            
    return fields

if __name__ == "__main__":
    args = (' \tid=a\tmsg="  x  "  ',)
    expected = {'id': 'a', 'msg': '  x  '}
    actual = parse_fields(*args)
    print(expected == actual, actual)
