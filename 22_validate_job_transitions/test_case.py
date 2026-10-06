"""Visible tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import validate_job_history
else:
    from main import validate_job_history


class TestCases(unittest.TestCase):

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({}, []))
        self.assertEqual(args, before)

    def test_success(self):
        args = ([('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'SUCCEEDED')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'SUCCEEDED'}, []))
        self.assertEqual(args, before)

    def test_invalid_then_valid(self):
        args = ([('a', 'RUNNING'), ('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'FAILED'), ('a', 'QUEUED')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'FAILED'}, [0, 4]))
        self.assertEqual(args, before)

    def test_interleaved(self):
        args = ([('a', 'QUEUED'), ('b', 'QUEUED'), ('a', 'CANCELLED'), ('b', 'RUNNING')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'CANCELLED', 'b': 'RUNNING'}, []))
        self.assertEqual(args, before)

    def test_duplicate(self):
        args = ([('a', 'QUEUED'), ('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'RUNNING')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'RUNNING'}, [1, 3]))
        self.assertEqual(args, before)

    def test_unknown(self):
        args = ([('a', 'UNKNOWN'), ('b', 'SUCCEEDED')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({}, [0, 1]))
        self.assertEqual(args, before)

    def test_skip_running(self):
        args = ([('a', 'QUEUED'), ('a', 'SUCCEEDED'), ('a', 'RUNNING')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'RUNNING'}, [1]))
        self.assertEqual(args, before)

    def test_terminal(self):
        args = ([('a', 'QUEUED'), ('a', 'RUNNING'), ('a', 'CANCELLED'), ('a', 'FAILED'), ('a', 'RUNNING')],)
        before = deepcopy(args)
        self.assertEqual(validate_job_history(*args), ({'a': 'CANCELLED'}, [3, 4]))
        self.assertEqual(args, before)


if __name__ == "__main__":
    unittest.main()
