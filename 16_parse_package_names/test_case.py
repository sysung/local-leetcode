"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import parse_package_name


class TestCases(unittest.TestCase):

    def test_valid(self):
        args = ('team-A_unit7_003_PASS_0012.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), {'group': 'team-A', 'item': 'unit7', 'revision': 3, 'result': 'PASS', 'timestamp': 12})
        self.assertEqual(args, before)

    def test_zero(self):
        args = ('a_b_0_FAIL_0.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), {'group': 'a', 'item': 'b', 'revision': 0, 'result': 'FAIL', 'timestamp': 0})
        self.assertEqual(args, before)

    def test_invalid_0(self):
        args = ('',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_1(self):
        args = ('a_b_1_pass_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_2(self):
        args = ('a_b_1_PASS_2.ZIP',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_3(self):
        args = ('a_b_-1_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_4(self):
        args = ('a_b_1_PASS_2.zip\n',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_5(self):
        args = (' a_b_1_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_6(self):
        args = ('a__1_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_7(self):
        args = ('a_b_1_PASS_2_extra.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_8(self):
        args = ('folder/a_b_1_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_9(self):
        args = ('a_b_١_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_10(self):
        args = ('a_b_1_PASS_.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_11(self):
        args = ('a_b_1_PASS_2xzip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)

    def test_invalid_12(self):
        args = ('a_b_+1_PASS_2.zip',)
        before = deepcopy(args)
        self.assertEqual(parse_package_name(*args), None)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
