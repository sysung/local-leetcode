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


    def test_single_pass(self):
        args = ([{'device_id': 'a', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 0, 'pass_rate': 1.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_single_fail(self):
        args = ([{'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 1, 'pass_rate': 0.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_interleaved_devices(self):
        args = ([{'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'b', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'b', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 1, 'pass_rate': 0.5, 'total': 2},
         'b': {'failures': 1, 'pass_rate': 0.5, 'total': 2}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_two_thirds_pass(self):
        args = ([{'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'a', 'status': 'PASS'},
          {'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 1, 'pass_rate': 0.6666666666666666, 'total': 3}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_device(self):
        args = ([{'device_id': '板', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'板': {'failures': 1, 'pass_rate': 0.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_case_sensitive_ids(self):
        args = ([{'device_id': 'A', 'status': 'PASS'}, {'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'A': {'failures': 0, 'pass_rate': 1.0, 'total': 1},
         'a': {'failures': 1, 'pass_rate': 0.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_prefix_ids(self):
        args = ([{'device_id': 'gpu-1', 'status': 'PASS'}, {'device_id': 'gpu-10', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'gpu-1': {'failures': 0, 'pass_rate': 1.0, 'total': 1},
         'gpu-10': {'failures': 0, 'pass_rate': 1.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_extra_fields_ignored(self):
        args = ([{'device_id': 'a', 'source': 'lab', 'status': 'PASS'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 0, 'pass_rate': 1.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_repeated_records_counted(self):
        args = ([{'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'},
          {'device_id': 'a', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'a': {'failures': 7, 'pass_rate': 0.0, 'total': 7}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_numeric_looking_ids(self):
        args = ([{'device_id': '01', 'status': 'PASS'}, {'device_id': '1', 'status': 'FAIL'}],)
        before = deepcopy(args)
        expected = {'01': {'failures': 0, 'pass_rate': 1.0, 'total': 1},
         '1': {'failures': 1, 'pass_rate': 0.0, 'total': 1}}
        self.assertEqual(summarize_tests(*args), expected)
        self.assertEqual(args, before)

    def test_many_small_groups(self):
        records = [{"device_id": str(i), "status": "PASS"} for i in range(1000)]
        self.assertEqual(summarize_tests(records), {str(i): {"total": 1, "failures": 0, "pass_rate": 1.0} for i in range(1000)})

    def test_maximum_hot_device(self):
        records = [{"device_id": "a", "status": "FAIL" if i % 4 == 0 else "PASS"} for i in range(100000)]
        self.assertEqual(summarize_tests(records), {"a": {"total": 100000, "failures": 25000, "pass_rate": 0.75}})
        self.assertEqual(records[0], {"device_id": "a", "status": "FAIL"})

    def test_maximum_distinct_devices(self):
        records = [{"device_id": str(i), "status": "FAIL"} for i in range(100000)]
        self.assertEqual(summarize_tests(records), {str(i): {"total": 1, "failures": 1, "pass_rate": 0.0} for i in range(100000)})

    def test_skewed_group_sizes(self):
        records = [{"device_id": "a", "status": "PASS"}] * 90000 + [{"device_id": "b", "status": "FAIL"}] * 10000
        self.assertEqual(summarize_tests(records), {"a": {"total": 90000, "failures": 0, "pass_rate": 1.0}, "b": {"total": 10000, "failures": 10000, "pass_rate": 0.0}})


if __name__ == "__main__":
    unittest.main()
