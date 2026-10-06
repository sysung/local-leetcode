"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import parse_logs
else:
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


    def test_blank_and_whitespace_lines(self):
        args = (['', '   ', '\t\n'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_empty_timestamp(self):
        args = ([',gpu,PASS', ' ,gpu,FAIL'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_nondecimal_timestamps(self):
        args = (['1e3,gpu,PASS', '0x10,gpu,PASS', 'NaN,gpu,FAIL'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_non_ascii_digits(self):
        args = (['١,gpu,PASS', '１,gpu,FAIL'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_internal_timestamp_whitespace(self):
        args = (['1 0,gpu,PASS', '+ 2,gpu,FAIL'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_embedded_device_spaces(self):
        args = (['1, gpu board 1 ,PASS'],)
        before = deepcopy(args)
        expected = [{'device_id': 'gpu board 1', 'status': 'PASS', 'timestamp': 1}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_extra_delimiters(self):
        args = (['1,gpu,PASS,', ',1,gpu,PASS', '1,gpu,,PASS'],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_line_endings(self):
        args = (['1,gpu,PASS\r\n', '2,gpu,FAIL\n'],)
        before = deepcopy(args)
        expected = [{'device_id': 'gpu', 'status': 'PASS', 'timestamp': 1},
         {'device_id': 'gpu', 'status': 'FAIL', 'timestamp': 2}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_large_timestamp_digits(self):
        text = "9" * 990
        self.assertEqual(parse_logs([text + ",a,PASS"]), [{"timestamp": int(text), "device_id": "a", "status": "PASS"}])

    def test_leading_zeros(self):
        args = (['00012,a,PASS', '+000,a,FAIL'],)
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'status': 'PASS', 'timestamp': 12},
         {'device_id': 'a', 'status': 'FAIL', 'timestamp': 0}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_lines_remain(self):
        args = (['1,a,PASS', '1,a,PASS'],)
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'status': 'PASS', 'timestamp': 1},
         {'device_id': 'a', 'status': 'PASS', 'timestamp': 1}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_unsorted_input_preserves_order(self):
        args = (['9,GPU,PASS', '1,gpu,FAIL'],)
        before = deepcopy(args)
        expected = [{'device_id': 'GPU', 'status': 'PASS', 'timestamp': 9},
         {'device_id': 'gpu', 'status': 'FAIL', 'timestamp': 1}]
        self.assertEqual(parse_logs(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_valid_batch(self):
        lines = [f"{i},gpu-{i % 10},PASS" for i in range(100000)]
        result = parse_logs(lines)
        self.assertEqual(result, [{"timestamp": i, "device_id": f"gpu-{i % 10}", "status": "PASS"} for i in range(100000)])
        self.assertEqual(lines[0], "0,gpu-0,PASS")
        self.assertEqual(lines[-1], "99999,gpu-9,PASS")

    def test_large_mostly_invalid_batch(self):
        lines = ["broken"] * 99999 + ["0,a,FAIL"]
        self.assertEqual(parse_logs(lines), [{"timestamp": 0, "device_id": "a", "status": "FAIL"}])
        self.assertEqual(lines.count("broken"), 99999)


if __name__ == "__main__":
    unittest.main()
