"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

from main import merge_streams


class TestCases(unittest.TestCase):
    def test_interleaved(self):
        args = ([[(1, 'a'), (4, 'd')], [(2, 'b'), (3, 'c')]],)
        before = deepcopy(args)
        expected = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_ties(self):
        args = ([[(1, 'z'), (1, 'y')], [(1, 'a')]],)
        before = deepcopy(args)
        expected = [(1, 'z'), (1, 'y'), (1, 'a')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_no_streams(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_empty_streams(self):
        args = ([[], [], []],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_one_stream(self):
        args = ([[(0, 'a'), (0, 'b'), (9, 'c')]],)
        before = deepcopy(args)
        expected = [(0, 'a'), (0, 'b'), (9, 'c')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_mixed_empty(self):
        args = ([[], [(2, 'b')], [], [(1, 'a')]],)
        before = deepcopy(args)
        expected = [(1, 'a'), (2, 'b')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_incremental_consumption(self):
        consumed = [0, 0]
        def stream(index, timestamps):
            for timestamp in timestamps:
                consumed[index] += 1
                yield timestamp, str(index)
        merged = merge_streams([stream(0, range(0, 100, 2)), stream(1, range(1, 100, 2))])
        self.assertIs(iter(merged), merged)
        self.assertEqual(next(merged), (0, "0"))
        self.assertEqual(consumed, [1, 1])
        self.assertEqual(next(merged), (1, "1"))
        self.assertEqual(consumed, [2, 1])
        self.assertEqual(len(list(merged)), 98)


    def test_identical_events_are_not_deduplicated(self):
        args = ([[(0, 'a'), (0, 'a')], [(0, 'a')]],)
        before = deepcopy(args)
        expected = [(0, 'a'), (0, 'a'), (0, 'a')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_tie_then_future_events(self):
        args = ([[(0, 'z'), (2, 'z')], [(0, 'a'), (1, 'a')]],)
        before = deepcopy(args)
        expected = [(0, 'z'), (0, 'a'), (1, 'a'), (2, 'z')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_reversed_singleton_streams(self):
        args = ([[(3, 'c')], [(2, 'b')], [(1, 'a')]],)
        before = deepcopy(args)
        expected = [(1, 'a'), (2, 'b'), (3, 'c')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_tuple_backed_streams(self):
        args = ([((0, 'a'), (2, 'c')), ((1, 'b'),)],)
        before = deepcopy(args)
        expected = [(0, 'a'), (1, 'b'), (2, 'c')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_one_shot_streams(self):
        class OneShot:
            def __init__(self, values):
                self.values = values
                self.used = False
            def __iter__(self):
                if self.used:
                    raise AssertionError("Stream was restarted")
                self.used = True
                return iter(self.values)
        streams = [OneShot([(0, "a"), (2, "c")]), OneShot([(1, "b")])]
        self.assertEqual(list(merge_streams(streams)), [(0, "a"), (1, "b"), (2, "c")])

    def test_guard_against_eager_materialization(self):
        consumed = [0]
        allowed = [1]
        def guarded():
            for timestamp in range(100000):
                consumed[0] += 1
                if consumed[0] > allowed[0]:
                    raise AssertionError("Read beyond the next required head")
                yield timestamp, "a"
        merged = merge_streams([guarded()])
        self.assertEqual(next(merged), (0, "a"))
        allowed[0] = 2
        self.assertEqual(next(merged), (1, "a"))
        self.assertEqual(consumed[0], 2)

    def test_source_failure_is_deferred_until_needed(self):
        def failing_source():
            yield 0, "a"
            raise RuntimeError("source unavailable")
        merged = merge_streams([failing_source(), [(1, "b")]])
        self.assertEqual(next(merged), (0, "a"))
        with self.assertRaises(RuntimeError):
            next(merged)

    def test_large_timestamp_values(self):
        args = ([[(1000000000000000000, 'a')], [(999999999999999999, 'b')]],)
        before = deepcopy(args)
        expected = [(999999999999999999, 'b'), (1000000000000000000, 'a')]
        self.assertEqual(list(merge_streams(*args)), expected)
        self.assertEqual(args, before)

    def test_maximum_stream_count_with_empty_inputs(self):
        streams = [[] for _ in range(999)] + [[(0, "a")]]
        self.assertEqual(list(merge_streams(streams)), [(0, "a")])
        self.assertEqual(len(streams), 1000)

    def test_maximum_stream_count_interleaved(self):
        streams = [[(round_number * 1000 + index, str(index)) for round_number in range(100)] for index in range(1000)]
        self.assertEqual(list(merge_streams(streams)), [(timestamp, str(timestamp % 1000)) for timestamp in range(100000)])
        self.assertEqual(len(streams[0]), 100)

    def test_maximum_single_generator_stream(self):
        source = ((i, "a") for i in range(100000))
        self.assertEqual(list(merge_streams([source])), [(i, "a") for i in range(100000)])

    def test_large_uneven_stream_sizes(self):
        streams = [[(i, "long") for i in range(99999)], [(50000, "short")]]
        expected = [(i, "long") for i in range(50001)] + [(50000, "short")] + [(i, "long") for i in range(50001, 99999)]
        self.assertEqual(list(merge_streams(streams)), expected)

    def test_maximum_duplicate_timestamp_streams(self):
        streams = [[(0, str(index))] * 100 for index in range(1000)]
        self.assertEqual(list(merge_streams(streams)), [(0, str(index)) for index in range(1000) for _ in range(100)])


if __name__ == "__main__":
    unittest.main()
