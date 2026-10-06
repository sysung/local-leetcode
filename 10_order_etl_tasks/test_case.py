"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import order_tasks
else:
    from main import order_tasks


class TestCases(unittest.TestCase):
    def test_pipeline(self):
        args = ({'extract': [], 'publish': ['transform'], 'transform': ['extract']},)
        before = deepcopy(args)
        expected = ['extract', 'transform', 'publish']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_alphabetical_choice(self):
        args = ({'b': ['a'], 'c': [], 'z': []},)
        before = deepcopy(args)
        expected = ['a', 'b', 'c', 'z']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ({},)
        before = deepcopy(args)
        expected = []
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_dependencies(self):
        args = ({'b': ['a', 'a']},)
        before = deepcopy(args)
        expected = ['a', 'b']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_diamond(self):
        args = ({'b': ['a'], 'c': ['a'], 'd': ['b', 'c']},)
        before = deepcopy(args)
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_cycle(self):
        args = ({'a': ['b'], 'b': ['a']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_self_cycle(self):
        args = ({'a': ['a']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_partial_cycle(self):
        args = ({'a': ['b'], 'b': ['a'], 'x': []},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)


    def test_single_isolated_task(self):
        args = ({'extract': []},)
        before = deepcopy(args)
        expected = ['extract']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_disconnected_chains(self):
        args = ({'b': ['a'], 'd': ['c']},)
        before = deepcopy(args)
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_three_node_cycle(self):
        args = ({'a': ['c'], 'b': ['a'], 'c': ['b']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_cycle_with_downstream_task(self):
        args = ({'a': ['b'], 'b': ['a'], 'publish': ['b']},)
        before = deepcopy(args)
        with self.assertRaises(ValueError):
            order_tasks(*args)
        self.assertEqual(args, before)

    def test_unicode_order(self):
        args = ({'A': [], 'é': [], 'Ω': []},)
        before = deepcopy(args)
        expected = ['A', 'é', 'Ω']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_case_sensitive_task_names(self):
        args = ({'A': [], 'B': ['A'], 'a': []},)
        before = deepcopy(args)
        expected = ['A', 'B', 'a']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_prerequisite_list_order_does_not_control_output(self):
        args = ({'publish': ['z', 'a', 'm']},)
        before = deepcopy(args)
        expected = ['a', 'm', 'z', 'publish']
        self.assertEqual(order_tasks(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_independent_tasks(self):
        dependencies = {f"task-{i:05d}": [] for i in range(9999, -1, -1)}
        self.assertEqual(order_tasks(dependencies), [f"task-{i:05d}" for i in range(10000)])
        self.assertEqual(next(iter(dependencies)), "task-09999")

    def test_maximum_depth_chain(self):
        dependencies = {f"task-{i:05d}": [f"task-{i-1:05d}"] for i in range(1, 10000)}
        self.assertEqual(order_tasks(dependencies), [f"task-{i:05d}" for i in range(10000)])

    def test_large_fan_in(self):
        prerequisites = [f"source-{i:05d}" for i in range(9999)]
        self.assertEqual(order_tasks({"zz-publish": prerequisites}), prerequisites + ["zz-publish"])
        self.assertEqual(len(prerequisites), 9999)

    def test_large_fan_out(self):
        dependencies = {f"task-{i:05d}": ["z-source"] for i in range(9999)}
        self.assertEqual(order_tasks(dependencies), ["z-source"] + [f"task-{i:05d}" for i in range(9999)])

    def test_dense_layered_dependencies(self):
        dependencies = {}
        for layer in range(10):
            previous = [f"L{layer - 1}-{i:03d}" for i in range(100)] if layer else []
            for index in range(100):
                dependencies[f"L{layer}-{index:03d}"] = previous.copy()
        expected = [f"L{layer}-{index:03d}" for layer in range(10) for index in range(100)]
        self.assertEqual(order_tasks(dependencies), expected)
        self.assertEqual(len(dependencies["L9-000"]), 100)


if __name__ == "__main__":
    unittest.main()
