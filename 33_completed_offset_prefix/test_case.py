"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import advance_offsets
else:
    from main import advance_offsets


class TestCases(unittest.TestCase):

    def test_gap_blocks_later_completion(self):
        args = ({'p0': 5}, [('p0', 7), ('p0', 5), ('p0', 8)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p0': 6})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_independent_partitions(self):
        args = ({'b': 10, 'a': 0}, [('a', 1), ('b', 10), ('a', 0), ('b', 12)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'a': 2, 'b': 11})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_empty(self):
        args = ({}, [])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_no_completions(self):
        args = ({'b': 4, 'a': 2}, [])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'a': 2, 'b': 4})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_duplicates(self):
        args = ({'p': 0}, [('p', 0), ('p', 0), ('p', 1)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 2})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_old_completions(self):
        args = ({'p': 5}, [('p', 1), ('p', 4)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 5})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_missing_start(self):
        args = ({'p': 3}, [('p', 4), ('p', 5)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 3})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_unsorted_contiguous(self):
        args = ({'p': 2}, [('p', 4), ('p', 2), ('p', 3)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 5})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_large_gap(self):
        args = ({'p': 0}, [('p', 1000000000000)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 0})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])

    def test_large_start(self):
        args = ({'p': 1000000000000}, [('p', 1000000000000), ('p', 1000000000001)])
        before = deepcopy(args)
        self.assertEqual(advance_offsets(*args), {'p': 1000000000002})
        self.assertEqual(args, before)
        result = advance_offsets(*args)
        self.assertEqual(list(result), sorted(args[0]))
        self.assertIsNot(result, args[0])


if __name__ == "__main__":
    unittest.main()
