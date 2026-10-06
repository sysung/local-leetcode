"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import parse_fields
else:
    from main import parse_fields


class TestCases(unittest.TestCase):

    def test_quoted(self):
        args = ('id=a message="sensor too hot" code=X=7',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {'id': 'a', 'message': 'sensor too hot', 'code': 'X=7'})
        self.assertEqual(args, before)

    def test_duplicate_and_empty(self):
        args = ('id=a id=b note=""',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {'id': 'b', 'note': ''})
        self.assertEqual(args, before)

    def test_whitespace(self):
        args = (' \tid=a\tmsg="  x  "  ',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {'id': 'a', 'msg': '  x  '})
        self.assertEqual(args, before)

    def test_blank(self):
        args = (' \t ',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {})
        self.assertEqual(args, before)

    def test_empty(self):
        args = ('',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {})
        self.assertEqual(args, before)

    def test_quoted_equals(self):
        args = ('msg="a=b=c"',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), {'msg': 'a=b=c'})
        self.assertEqual(args, before)

    def test_invalid_0(self):
        args = ('id=',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_1(self):
        args = ('id="unfinished',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_2(self):
        args = ('id="a"tail',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_3(self):
        args = ('id=a"b"',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_4(self):
        args = ('id =a',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_5(self):
        args = ('id= a',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_6(self):
        args = ('1id=a',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_7(self):
        args = ('ID=a',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_8(self):
        args = ('id=a broken',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_9(self):
        args = ('id="a"next=b',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_10(self):
        args = ('=a',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)

    def test_invalid_11(self):
        args = ('id="a"=b',)
        before = deepcopy(args)
        self.assertEqual(parse_fields(*args), None)
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
