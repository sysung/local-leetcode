"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import filter_records
else:
    from main import filter_records


class TestCases(unittest.TestCase):

    def test_precedence(self):
        args = ([{'ready', 'failed'}, {'ready'}, {'urgent'}, set()], 'ready & !failed | urgent')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [1, 2])
        self.assertEqual(args, before)

    def test_parentheses(self):
        args = ([{'a'}, {'b'}, set()], '!(a | b)')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [2])
        self.assertEqual(args, before)

    def test_double_not(self):
        args = ([{'a'}, set()], '!!a')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [0])
        self.assertEqual(args, before)

    def test_not_chain(self):
        args = ([{'a'}, set()], '!!!a')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [1])
        self.assertEqual(args, before)

    def test_nested_not(self):
        args = ([{'b', 'a'}, {'a'}, {'b'}, set()], '!(!a | !b)')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [0])
        self.assertEqual(args, before)

    def test_whitespace_label(self):
        args = ([{'job_1'}, {'job'}], ' \tjob_1 ')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [0])
        self.assertEqual(args, before)

    def test_valid_empty_records(self):
        args = ([], 'a | !b')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_deep_nesting(self):
        args = ([{'a'}, set()], '((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((a))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [0])
        self.assertEqual(args, before)

    def test_invalid_0(self):
        args = ([], '')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_1(self):
        args = ([], ' ')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_2(self):
        args = ([], 'a b')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_3(self):
        args = ([], 'a(b)')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_4(self):
        args = ([], '()')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_5(self):
        args = ([], '(a')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_6(self):
        args = ([], 'a)')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_7(self):
        args = ([], '&a')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_8(self):
        args = ([], 'a|')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_9(self):
        args = ([], 'a&&b')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_10(self):
        args = ([], 'a!')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_11(self):
        args = ([], 'a ^ b')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_12(self):
        args = ([], 'A')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_13(self):
        args = ([], '1a')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_14(self):
        args = ([], '!')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)

    def test_invalid_15(self):
        args = ([], '(a|)')
        before = deepcopy(args)
        self.assertEqual(filter_records(*args), [])
        self.assertEqual(args, before)


    def test_invalid_with_records(self):
        queries = ('', ' ', 'a b', 'a(b)', '()', '(a', 'a)', '&a',
                   'a|', 'a&&b', 'a!', 'a ^ b', 'A', '1a', '!', '(a|)')
        for query in queries:
            with self.subTest(query=query):
                args = ([{'a', 'b'}, set()], query)
                before = deepcopy(args)
                self.assertEqual(filter_records(*args), [])
                self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
