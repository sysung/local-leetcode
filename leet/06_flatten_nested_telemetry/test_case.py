"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import flatten_telemetry


class TestCases(unittest.TestCase):
    def test_nested(self):
        args = ({'gpu': {'fan': {'rpm': 1200}, 'temperature': 80}, 'site': 'lab'},)
        before = deepcopy(args)
        expected = {'gpu.fan.rpm': 1200, 'gpu.temperature': 80, 'site': 'lab'}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_empty_nodes(self):
        args = ({'gpu': {}, 'healthy': True, 'reading': None},)
        before = deepcopy(args)
        expected = {'healthy': True, 'reading': None}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ({},)
        before = deepcopy(args)
        expected = {}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_flat(self):
        args = ({'label': 'x', 'temperature': 0},)
        before = deepcopy(args)
        expected = {'label': 'x', 'temperature': 0}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_same_leaf_names(self):
        args = ({'a': {'value': 1}, 'b': {'value': 2}},)
        before = deepcopy(args)
        expected = {'a.value': 1, 'b.value': 2}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_scalar_types(self):
        args = ({'a': -3, 'b': 1.5, 'c': False, 'd': ''},)
        before = deepcopy(args)
        expected = {'a': -3, 'b': 1.5, 'c': False, 'd': ''}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_deep_nesting(self):
        record = 7
        for _ in range(2000):
            record = {"x": record}
        self.assertEqual(flatten_telemetry(record), {".".join(["x"] * 2000): 7})
        node = record
        for _ in range(2000):
            self.assertEqual(list(node), ["x"])
            node = node["x"]
        self.assertEqual(node, 7)


if __name__ == "__main__":
    unittest.main()
