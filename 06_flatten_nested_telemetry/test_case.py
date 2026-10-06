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


    def test_single_null_leaf(self):
        args = ({'value': None},)
        before = deepcopy(args)
        expected = {'value': None}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_only_empty_branches(self):
        args = ({'a': {'b': {}}, 'c': {}},)
        before = deepcopy(args)
        expected = {}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_and_space_keys(self):
        args = ({'板': {'fan speed': 7}},)
        before = deepcopy(args)
        expected = {'板.fan speed': 7}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_numeric_looking_keys(self):
        args = ({'0': {'01': 1}},)
        before = deepcopy(args)
        expected = {'0.01': 1}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_leaf_and_branch_siblings(self):
        args = ({'gpu': {'value': 3}, 'value': 4},)
        before = deepcopy(args)
        expected = {'gpu.value': 3, 'value': 4}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_shared_subtree_at_two_paths(self):
        shared = {"value": 3}
        record = {"a": shared, "b": shared}
        self.assertEqual(flatten_telemetry(record), {"a.value": 3, "b.value": 3})
        self.assertIs(record["a"], record["b"])
        self.assertEqual(shared, {"value": 3})

    def test_case_sensitive_paths(self):
        args = ({'GPU': {'T': 1}, 'gpu': {'t': 2}},)
        before = deepcopy(args)
        expected = {'GPU.T': 1, 'gpu.t': 2}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_prefix_keys_do_not_collide(self):
        args = ({'a': {'b': 1}, 'ab': 2},)
        before = deepcopy(args)
        expected = {'a.b': 1, 'ab': 2}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_zero_false_and_empty_string(self):
        args = ({'a': 0, 'b': False, 'c': ''},)
        before = deepcopy(args)
        expected = {'a': 0, 'b': False, 'c': ''}
        self.assertEqual(flatten_telemetry(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_wide_dictionary(self):
        record = {f"reading-{i}": i for i in range(10000)}
        before = record.copy()
        self.assertEqual(flatten_telemetry(record), before)
        self.assertEqual(record, before)

    def test_large_balanced_tree(self):
        record = {f"device{i}": {f"sensor{j}": i * 10 + j for j in range(9)} for i in range(1000)}
        expected = {f"device{i}.sensor{j}": i * 10 + j for i in range(1000) for j in range(9)}
        self.assertEqual(flatten_telemetry(record), expected)
        self.assertEqual(len(record), 1000)

    def test_deep_chain_with_sibling_leaves(self):
        record = {"reading": 5}
        for level in range(1500):
            record = {"next": record, "level": level}
        expected = {"next." * depth + "level": 1499 - depth for depth in range(1500)}
        expected["next." * 1500 + "reading"] = 5
        self.assertEqual(flatten_telemetry(record), expected)
        self.assertEqual(record["level"], 1499)

    def test_long_path_components(self):
        key = "sensor_" + "x" * 100
        record = {key: {key: {key: 3}}}
        self.assertEqual(flatten_telemetry(record), {".".join([key] * 3): 3})


if __name__ == "__main__":
    unittest.main()
