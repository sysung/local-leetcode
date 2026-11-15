from __future__ import annotations


def merge_streams(streams: list[list[tuple[int, str]]]) -> list[tuple[int, str]]:
    """Implement the problem described in README.md."""
    flattened_stream = []
    idx = 0
    for s in streams:
        for e in s:
            flattened_stream += [list(e) + [idx]]
            idx += 1
    sorted_stream = sorted(flattened_stream, key=lambda x: (x[0], x[2]))
    return [tuple(e[:2]) for e in sorted_stream]

if __name__ == "__main__":
    args = ([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
    expected = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    actual = merge_streams(*args)
    print(expected == actual, actual)
