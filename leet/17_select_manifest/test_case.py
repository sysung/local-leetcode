"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import select_manifest


class TestCases(unittest.TestCase):

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), None)
        self.assertEqual(args, before)

    def test_no_match(self):
        args = (['Manifest.json', 'summary.txt.bak'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), None)
        self.assertEqual(args, before)

    def test_priority_before_depth(self):
        args = (['output.txt', 'summary.txt', 'x/y/manifest.json'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'x/y/manifest.json')
        self.assertEqual(args, before)

    def test_depth(self):
        args = (['a/b/manifest.json', 'z/manifest.json'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'z/manifest.json')
        self.assertEqual(args, before)

    def test_lexical_tie(self):
        args = (['z/summary.txt', 'a/summary.txt'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'a/summary.txt')
        self.assertEqual(args, before)

    def test_root(self):
        args = (['a/manifest.json', 'manifest.json'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'manifest.json')
        self.assertEqual(args, before)

    def test_basename_only(self):
        args = (['manifest.json/data.txt', 'x/output.txt'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'x/output.txt')
        self.assertEqual(args, before)

    def test_fallback(self):
        args = (['x/output.txt', 'z/summary.txt'],)
        before = deepcopy(args)
        self.assertEqual(select_manifest(*args), 'z/summary.txt')
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
