"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import deduplicate_events
else:
    from main import deduplicate_events


class TestCases(unittest.TestCase):
    def test_newest(self):
        args = ([{'event_id': 'b', 'payload': 'old', 'timestamp': 1},
          {'event_id': 'a', 'payload': 'a', 'timestamp': 3},
          {'event_id': 'b', 'payload': 'new', 'timestamp': 2}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 'a', 'timestamp': 3},
         {'event_id': 'b', 'payload': 'new', 'timestamp': 2}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_ties(self):
        args = ([{'event_id': 'a', 'payload': 'first', 'timestamp': 4},
          {'event_id': 'a', 'payload': 'last', 'timestamp': 4}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 'last', 'timestamp': 4}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty(self):
        args = ([],)
        before = deepcopy(args)
        expected = []
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_older_arrives_last(self):
        args = ([{'event_id': 'a', 'payload': None, 'timestamp': 8},
          {'event_id': 'a', 'payload': 0, 'timestamp': 1}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': None, 'timestamp': 8}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_single(self):
        args = ([{'event_id': 'x', 'payload': {'value': 3}, 'source': 'station', 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'x', 'payload': {'value': 3}, 'source': 'station', 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_distinct(self):
        args = ([{'event_id': 'z', 'payload': 0, 'timestamp': 0},
          {'event_id': 'b', 'payload': 1, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'b', 'payload': 1, 'timestamp': 0},
         {'event_id': 'z', 'payload': 0, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)


    def test_three_way_timestamp_tie(self):
        args = ([{'event_id': 'a', 'payload': 0, 'timestamp': 3},
          {'event_id': 'a', 'payload': 1, 'timestamp': 3},
          {'event_id': 'a', 'payload': 2, 'timestamp': 3}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 2, 'timestamp': 3}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_null_payload(self):
        args = ([{'event_id': 'a', 'payload': None, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': None, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_nested_payload_preserved(self):
        args = ([{'event_id': 'a', 'payload': {'samples': [1, 2]}, 'timestamp': 1}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': {'samples': [1, 2]}, 'timestamp': 1}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_zero_timestamp_tie(self):
        args = ([{'event_id': 'a', 'payload': False, 'timestamp': 0},
          {'event_id': 'a', 'payload': True, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': True, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_large_timestamps(self):
        args = ([{'event_id': 'a', 'payload': 'new', 'timestamp': 1000000000000000000},
          {'event_id': 'a', 'payload': 'old', 'timestamp': 999999999999999999}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 'new', 'timestamp': 1000000000000000000}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_numeric_looking_ids_sort_as_strings(self):
        args = ([{'event_id': '2', 'payload': 0, 'timestamp': 0},
          {'event_id': '10', 'payload': 0, 'timestamp': 0},
          {'event_id': '1', 'payload': 0, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': '1', 'payload': 0, 'timestamp': 0},
         {'event_id': '10', 'payload': 0, 'timestamp': 0},
         {'event_id': '2', 'payload': 0, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_identifiers(self):
        args = ([{'event_id': 'Ω', 'payload': 0, 'timestamp': 0},
          {'event_id': 'é', 'payload': 0, 'timestamp': 0},
          {'event_id': 'A', 'payload': 0, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'A', 'payload': 0, 'timestamp': 0},
         {'event_id': 'é', 'payload': 0, 'timestamp': 0},
         {'event_id': 'Ω', 'payload': 0, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_extra_fields_follow_selected_record(self):
        args = ([{'event_id': 'a', 'payload': 0, 'source': 'old', 'timestamp': 1},
          {'event_id': 'a', 'extra': True, 'payload': 0, 'source': 'new', 'timestamp': 2}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'extra': True, 'payload': 0, 'source': 'new', 'timestamp': 2}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_same_payload_different_ids(self):
        args = ([{'event_id': 'b', 'payload': 7, 'timestamp': 1},
          {'event_id': 'a', 'payload': 7, 'timestamp': 1}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 7, 'timestamp': 1},
         {'event_id': 'b', 'payload': 7, 'timestamp': 1}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_prefix_ids_are_distinct(self):
        args = ([{'event_id': 'gpu-10', 'payload': 0, 'timestamp': 0},
          {'event_id': 'gpu-1', 'payload': 0, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'gpu-1', 'payload': 0, 'timestamp': 0},
         {'event_id': 'gpu-10', 'payload': 0, 'timestamp': 0}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_descending_versions(self):
        args = ([{'event_id': 'a', 'payload': 5, 'timestamp': 5},
          {'event_id': 'a', 'payload': 4, 'timestamp': 4},
          {'event_id': 'a', 'payload': 3, 'timestamp': 3},
          {'event_id': 'a', 'payload': 2, 'timestamp': 2},
          {'event_id': 'a', 'payload': 1, 'timestamp': 1}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 5, 'timestamp': 5}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_interleaved_versions(self):
        args = ([{'event_id': 'a', 'payload': 1, 'timestamp': 1},
          {'event_id': 'b', 'payload': 3, 'timestamp': 3},
          {'event_id': 'a', 'payload': 2, 'timestamp': 2},
          {'event_id': 'b', 'payload': 0, 'timestamp': 0}],)
        before = deepcopy(args)
        expected = [{'event_id': 'a', 'payload': 2, 'timestamp': 2},
         {'event_id': 'b', 'payload': 3, 'timestamp': 3}]
        self.assertEqual(deduplicate_events(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_distinct_batch(self):
        events = [{"event_id": f"id-{i:06d}", "timestamp": i, "payload": i} for i in range(99999, -1, -1)]
        result = deduplicate_events(events)
        self.assertEqual(result, list(reversed(events)))
        self.assertEqual(events[0]["event_id"], "id-099999")

    def test_maximum_hot_key_batch(self):
        events = [{"event_id": "a", "timestamp": i, "payload": i} for i in range(100000)]
        self.assertEqual(deduplicate_events(events), [{"event_id": "a", "timestamp": 99999, "payload": 99999}])
        self.assertEqual(events[0]["timestamp"], 0)


if __name__ == "__main__":
    unittest.main()
