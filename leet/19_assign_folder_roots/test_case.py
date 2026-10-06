"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import assign_roots


class TestCases(unittest.TestCase):

    def test_empty(self):
        args = ([], [])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {})
        self.assertEqual(args, before)

    def test_no_roots(self):
        args = ([], ['a/x.txt', 'y.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'a/x.txt': None, 'y.txt': None})
        self.assertEqual(args, before)

    def test_nested(self):
        args = (['manifest.json', 'a/manifest.json', 'a/sub/manifest.json'], ['a/sub/x.txt', 'a/y.txt', 'b/z.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'a/sub/x.txt': 'a/sub', 'a/y.txt': 'a', 'b/z.txt': ''})
        self.assertEqual(args, before)

    def test_prefix_collision(self):
        args = (['run/manifest.json'], ['run/x.txt', 'runner/x.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'run/x.txt': 'run', 'runner/x.txt': None})
        self.assertEqual(args, before)

    def test_sibling(self):
        args = (['a/b/manifest.json'], ['a/c/x.txt', 'a/b/x.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'a/c/x.txt': None, 'a/b/x.txt': 'a/b'})
        self.assertEqual(args, before)

    def test_duplicate_roots(self):
        args = (['a/manifest.json', 'a/manifest.json'], ['a/x.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'a/x.txt': 'a'})
        self.assertEqual(args, before)

    def test_manifest_is_file(self):
        args = (['a/manifest.json'], ['a/manifest.json'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'a/manifest.json': 'a'})
        self.assertEqual(args, before)

    def test_archive_root(self):
        args = (['manifest.json'], ['x.txt', 'a/b/y.txt'])
        before = deepcopy(args)
        self.assertEqual(assign_roots(*args), {'x.txt': '', 'a/b/y.txt': ''})
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
