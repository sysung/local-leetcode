"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import collect_pages
else:
    from main import collect_pages


Pages = dict[str, tuple[list[tuple[str, int]], str | None]]


class TestCases(unittest.TestCase):

    def test_none(self):
        args: tuple[Pages, str | None] = ({}, None)
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [])
        self.assertEqual(args, before)

    def test_deduplicate(self):
        args: tuple[Pages, str | None] = ({'p1': ([('b', 1), ('a', 2)], 'p2'), 'p2': ([('b', 9), ('c', 3)], None)}, 'p1')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('b', 9), ('a', 2), ('c', 3)])
        self.assertEqual(args, before)

    def test_empty_page(self):
        args: tuple[Pages, str | None] = ({'p1': ([], 'p2'), 'p2': ([('x', 1)], None)}, 'p1')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('x', 1)])
        self.assertEqual(args, before)

    def test_empty_cursor(self):
        args: tuple[Pages, str | None] = ({'': ([('x', 0)], None)}, '')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('x', 0)])
        self.assertEqual(args, before)

    def test_same_page_duplicate(self):
        args: tuple[Pages, str | None] = ({'p': ([('x', 1), ('x', 2)], None)}, 'p')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('x', 2)])
        self.assertEqual(args, before)

    def test_unreachable_cycle(self):
        args: tuple[Pages, str | None] = ({'p': ([], None), 'bad': ([], 'bad')}, 'p')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [])
        self.assertEqual(args, before)

    def test_missing_start(self):
        args: tuple[Pages, str | None] = ({}, 'missing')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [])
        self.assertEqual(args, before)

    def test_missing_next(self):
        args: tuple[Pages, str | None] = ({'p': ([('x', 1)], 'missing')}, 'p')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('x', 1)])
        self.assertEqual(args, before)

    def test_self_cycle(self):
        args: tuple[Pages, str | None] = ({'p': ([('x', 1)], 'p')}, 'p')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('x', 1)])
        self.assertEqual(args, before)

    def test_multi_page_cycle(self):
        args: tuple[Pages, str | None] = ({'p': ([('b', 1), ('a', 2)], 'q'), 'q': ([('b', 9), ('c', 3)], 'p')}, 'p')
        before = deepcopy(args)
        self.assertEqual(collect_pages(*args), [('b', 9), ('a', 2), ('c', 3)])
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
