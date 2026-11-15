from __future__ import annotations

from collections import Counter


def top_failure_codes(codes: list[str], k: int) -> list[tuple[str, int]]:
    """Implement the problem described in README.md."""
    if k <= 0:
        return []
    codes_freq_map = Counter(codes)     # K = Code, V = Frequency count
    sorted_codes_freq_map = sorted(codes_freq_map.items(), key=lambda x: (-x[1], x[0]))[:k]
    return sorted_codes_freq_map

if __name__ == "__main__":
    args = (['ECC', 'TEMP', 'ECC', 'POWER'], 2)

    expected = [('ECC', 2), ('POWER', 1)]
    actual = top_failure_codes(*args)

    print(actual)
    print(actual == expected)
