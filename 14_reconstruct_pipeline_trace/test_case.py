"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import reconstruct_trace
else:
    from main import reconstruct_trace


class TestCases(unittest.TestCase):
    def test_simple_trace(self):
        args = ([('extract', 'validate'), ('validate', 'publish')], 'extract')
        before = deepcopy(args)
        expected = ['extract', 'validate', 'publish']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_lexicographic(self):
        args = ([('A', 'C'), ('A', 'B'), ('B', 'A'), ('C', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'B', 'A', 'C', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([], 'start')
        before = deepcopy(args)
        expected = ['start']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_edges(self):
        args = ([('A', 'B'), ('A', 'B'), ('B', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'B', 'A', 'B']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_self_loop(self):
        args = ([('A', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_dead_end_requires_postorder(self):
        args = ([('J', 'K'), ('J', 'N'), ('N', 'J')], 'J')
        before = deepcopy(args)
        expected = ['J', 'N', 'J', 'K']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_disconnected(self):
        args = ([('A', 'B'), ('C', 'D')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_wrong_start(self):
        args = ([('A', 'B')], 'B')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_invalid_branch(self):
        args = ([('A', 'B'), ('A', 'C')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_impossible_degrees(self):
        args = ([('A', 'B'), ('B', 'A'), ('A', 'C'), ('B', 'C')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_long_chain(self):
        edges = [(str(i), str(i + 1)) for i in range(2000)]
        self.assertEqual(reconstruct_trace(edges, "0"), [str(i) for i in range(2001)])


    def test_multiple_self_loops(self):
        args = ([('A', 'A'), ('A', 'A'), ('A', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'A', 'A', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_unreachable_cycle(self):
        args = ([('A', 'B'), ('C', 'C')], 'A')
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            reconstruct_trace(*args)
        self.assertEqual(args, before)

    def test_nested_cycles_before_terminal_edge(self):
        args = ([('A', 'B'), ('B', 'C'), ('C', 'B'), ('B', 'A'), ('A', 'D')], 'A')
        before = deepcopy(args)
        expected = ['A', 'B', 'C', 'B', 'A', 'D']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_lexicographic_destinations(self):
        args = ([('A', 'Ω'), ('Ω', 'A'), ('A', 'é'), ('é', 'A')], 'A')
        before = deepcopy(args)
        expected = ['A', 'é', 'A', 'Ω', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_smallest_destination_must_be_last(self):
        args = ([('S', 'A'), ('S', 'B'), ('B', 'S')], 'S')
        before = deepcopy(args)
        expected = ['S', 'B', 'S', 'A']
        self.assertEqual(reconstruct_trace(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_duplicate_edge_multiset(self):
        edges = [("A", "B")] * 50000 + [("B", "A")] * 50000
        self.assertEqual(reconstruct_trace(edges, "A"), ["A", "B"] * 50000 + ["A"])
        self.assertEqual(len(edges), 100000)

    def test_large_lexicographic_fan_out_cycles(self):
        edges = [("hub", f"node-{i:05d}") for i in range(9999, -1, -1)] + [(f"node-{i:05d}", "hub") for i in range(10000)]
        expected = ["hub"]
        for i in range(10000):
            expected.extend([f"node-{i:05d}", "hub"])
        self.assertEqual(reconstruct_trace(edges, "hub"), expected)
        self.assertEqual(edges[0], ("hub", "node-09999"))

    def test_exhaustive_small_multigraph_oracle(self):
        import itertools
        possible_edges = [("A", "A"), ("A", "B"), ("B", "A"), ("B", "B")]
        for count in range(5):
            for sequence in itertools.product(possible_edges, repeat=count):
                candidates = []
                for ordered_edges in set(itertools.permutations(sequence)):
                    nodes = ["A"]
                    for source, destination in ordered_edges:
                        if source != nodes[-1]:
                            break
                        nodes.append(destination)
                    else:
                        candidates.append(nodes)
                with self.subTest(edges=sequence):
                    if candidates:
                        self.assertEqual(reconstruct_trace(list(sequence), "A"), min(candidates))
                    else:
                        with self.assertRaises(ValueError):
                            reconstruct_trace(list(sequence), "A")

    def test_maximum_depth_trace(self):
        edges = [(str(i), str(i + 1)) for i in range(100000)]
        self.assertEqual(reconstruct_trace(edges, "0"), [str(i) for i in range(100001)])
        self.assertEqual(edges[0], ("0", "1"))


if __name__ == "__main__":
    unittest.main()
