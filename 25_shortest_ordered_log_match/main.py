from __future__ import annotations


def shortest_ordered_match(codes: list[str], required: list[str]) -> tuple[int, int] | None:
    """Implement the problem described in README.md."""
    # Initialize required frequency
    required_map = {}
    for rdx, r in enumerate(required):
        if r not in required_map:
            required_map[r] = [rdx]
        else:
            required_map[r].append(rdx)

    # Brute force
    slices = []
    for idx, i in enumerate(codes):
        if i in required_map:
            for s in slices:
                for rdx in required_map[i][::-1]:
                    if len(s) == rdx:
                        s.append(idx)
            if 0 in required_map[i]:
                slices.append([idx])

    print(slices)
    shortest_slice = None
    for s in slices:
        if len(s) == len(required) and (shortest_slice is None or s[-1] - s[0] < shortest_slice[-1] - shortest_slice[0]):
            shortest_slice = s

    return (shortest_slice[0], shortest_slice[-1]) if shortest_slice is not None else None
                

if __name__ == "__main__":
    args = (['A', 'A', 'A', 'A'], ['A', 'A', 'A'])
    expected = (0,2)
    actual = shortest_ordered_match(*args)
    print(expected == actual)
    print(expected)
    print(actual)