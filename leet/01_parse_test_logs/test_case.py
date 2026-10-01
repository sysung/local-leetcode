"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import parse_logs


class TestCases(unittest.TestCase):
    def test_valid_and_invalid(self):
        args = (['10,gpu-1,PASS', 'broken', '12,gpu-2,FAIL'],)
        before = deepcopy(args)
        expected = [{'device_id': 'gpu-1', 'status': 'PASS', 'timestamp': 10},
         {'device_id': 'gpu-2', 'status': 'FAIL', 'timestamp': 12}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_whitespace(self):
        args = ([' 0 , board-1 , FAIL '],)
        before = deepcopy(args)
        expected = [{'device_id': 'board-1', 'status': 'FAIL', 'timestamp': 0}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_invalid_fields(self):
        args = (['-1,gpu,PASS', '1,,PASS', '1,gpu,pass', '1.5,gpu,FAIL'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_wrong_field_count(self):
        args = (['1,gpu', '1,gpu,PASS,extra', ''],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_signed_timestamps(self):
        args = (['+2,gpu,PASS', '-0,gpu,FAIL', '1_0,gpu,PASS', '++,gpu,PASS'],)
        before = deepcopy(args)
        expected = [{'device_id': 'gpu', 'status': 'PASS', 'timestamp': 2},
         {'device_id': 'gpu', 'status': 'FAIL', 'timestamp': 0}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
