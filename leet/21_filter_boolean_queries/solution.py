"""Reference solution.

Convert the query to postfix with an operator stack and an operand-expected flag. Evaluate the postfix expression with a boolean stack for each record. Unary NOT stays on the operator stack when another NOT arrives.
Time: O(C + nT), where C is query length, T its token count, and n record count. Auxiliary space: O(T), excluding output.
"""

from __future__ import annotations

import re


def filter_records(records: list[set[str]], query: str) -> list[int]:
    precedence = {"|": 1, "&": 2, "!": 3}
    label_pattern = re.compile(r"[a-z][a-z0-9_]*")
    postfix = []
    operators = []
    expect_operand = True
    index = 0
    while index < len(query):
        char = query[index]
        if char.isspace():
            index += 1
            continue
        label = label_pattern.match(query, index)
        if label is not None:
            if not expect_operand:
                raise ValueError("Missing operator")
            postfix.append(label.group())
            index = label.end()
            expect_operand = False
            continue
        if char in ("!", "("):
            if not expect_operand:
                raise ValueError("Missing operator")
            operators.append(char)
        elif char == ")":
            if expect_operand:
                raise ValueError("Missing operand")
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())
            if not operators:
                raise ValueError("Unmatched parenthesis")
            operators.pop()
        elif char in ("&", "|"):
            if expect_operand:
                raise ValueError("Missing operand")
            while operators and operators[-1] != "(" and precedence[operators[-1]] >= precedence[char]:
                postfix.append(operators.pop())
            operators.append(char)
            expect_operand = True
        else:
            raise ValueError("Illegal character")
        index += 1
    if expect_operand:
        raise ValueError("Missing operand")
    while operators:
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Unmatched parenthesis")
        postfix.append(operator)
    output = []
    for index, record in enumerate(records):
        values = []
        for token in postfix:
            if token == "!":
                values.append(not values.pop())
            elif token in ("&", "|"):
                right = values.pop()
                left = values.pop()
                values.append(left and right if token == "&" else left or right)
            else:
                values.append(token in record)
        if values[0]:
            output.append(index)
    return output
