"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import summarize_tests


class TestCases(unittest.TestCase):
    def test_mixed(self):
        args = ([{'device_id': 'gpu', 'status': 'PASS'}, {'device_id': 'gpu', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'gpu': {'failures': 1, 'pass_rate': 0.5, 'total': 2}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_multiple_devices(self):
        args = ([{'device_id': 'a', 'status': 'FAIL'}, {'device_id': 'b', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 1, 'pass_rate': 0.0, 'total': 1},
         'b': {'failures': 0, 'pass_rate': 1.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        expected = {}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_all_pass(self):
        args = ([{'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'a', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 0, 'pass_rate': 1.0, 'total': 3}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_all_fail(self):
        args = ([{'device_id': 'a', 'status': 'FAIL'}, {'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 2, 'pass_rate': 0.0, 'total': 2}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_fraction(self):
        args = ([{'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 2, 'pass_rate': 0.3333333333333333, 'total': 3}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
