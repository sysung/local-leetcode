"""Visible practice tests; run with python3 -m unittest -v test_case.py."""

import unittest
from copy import deepcopy

if __package__:
    from .main import enrich_events
else:
    from main import enrich_events


class TestCases(unittest.TestCase):
    def test_matched_and_unknown(self):
        args = ([{'device_id': 'a', 'value': 7}, {'device_id': 'x', 'value': 8}],
         [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'GPU', 'site': 'lab', 'value': 7},
         {'device_id': 'x', 'model': None, 'site': None, 'value': 8}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_duplicate_metadata(self):
        args = ([{'device_id': 'a'}],
         [{'device_id': 'a', 'model': 'old', 'site': 'one'},
          {'device_id': 'a', 'model': 'new', 'site': 'two'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'new', 'site': 'two'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty_events(self):
        args = ([], [{'device_id': 'a', 'model': 'x', 'site': 'y'}])
        before = deepcopy(args)
        expected = []
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty_metadata(self):
        args = ([{'device_id': 'a'}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_existing_fields(self):
        args = ([{'device_id': 'a', 'model': 'stale', 'site': 'old'}],
         [{'device_id': 'a', 'model': 'new', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'new', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_preserve_order(self):
        args = ([{'device_id': 'b'}, {'device_id': 'a'}, {'device_id': 'b'}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'b', 'model': None, 'site': None},
         {'device_id': 'a', 'model': None, 'site': None},
         {'device_id': 'b', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)


    def test_single_match(self):
        args = ([{'device_id': 'a'}], [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_orphan_metadata_ignored(self):
        args = ([{'device_id': 'a'}],
         [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'},
          {'device_id': 'b', 'model': 'CPU', 'site': 'other'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_unknown_overwrites_stale_fields(self):
        args = ([{'device_id': 'x', 'model': 'old', 'site': 'old'}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'x', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_empty_metadata_values(self):
        args = ([{'device_id': 'a'}], [{'device_id': 'a', 'model': '', 'site': ''}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': '', 'site': ''}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_unicode_device_match(self):
        args = ([{'device_id': '板'}], [{'device_id': '板', 'model': 'board', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': '板', 'model': 'board', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_case_sensitive_join(self):
        args = ([{'device_id': 'A'}], [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'A', 'model': None, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_nested_payload_preserved(self):
        args = ([{'device_id': 'a', 'payload': {'samples': [1, None]}}], [])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': None, 'payload': {'samples': [1, None]}, 'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_results_are_event_copies(self):
        event = {"device_id": "a"}
        result = enrich_events([event, event], [])
        self.assertEqual(result, [{"device_id": "a", "model": None, "site": None}] * 2)
        self.assertIsNot(result[0], event)
        self.assertIsNot(result[1], event)
        self.assertIsNot(result[0], result[1])
        self.assertEqual(event, {"device_id": "a"})

    def test_three_metadata_versions(self):
        args = ([{'device_id': 'a'}],
         [{'device_id': 'a', 'model': '0', 'site': 'lab'},
          {'device_id': 'a', 'model': '1', 'site': 'lab'},
          {'device_id': 'a', 'model': '2', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': '2', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_metadata_extra_fields_not_added(self):
        args = ([{'device_id': 'a'}],
         [{'device_id': 'a', 'model': 'GPU', 'owner': 'x', 'site': 'lab'}])
        before = deepcopy(args)
        expected = [{'device_id': 'a', 'model': 'GPU', 'site': 'lab'}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_wide_event_preserved(self):
        args = ([{'device_id': 'a',
           'f0': 0,
           'f1': 1,
           'f2': 2,
           'f3': 3,
           'f4': 4,
           'f5': 5,
           'f6': 6,
           'f7': 7,
           'f8': 8,
           'f9': 9}],
         [])
        before = deepcopy(args)
        expected = [{'device_id': 'a',
          'f0': 0,
          'f1': 1,
          'f2': 2,
          'f3': 3,
          'f4': 4,
          'f5': 5,
          'f6': 6,
          'f7': 7,
          'f8': 8,
          'f9': 9,
          'model': None,
          'site': None}]
        self.assertEqual(enrich_events(*args), expected)
        self.assertEqual(args, before)

    def test_maximum_distinct_join(self):
        events = [{"device_id": str(i), "value": i} for i in range(100000)]
        devices = [{"device_id": str(i), "model": "GPU", "site": "lab"} for i in range(99999, -1, -1)]
        self.assertEqual(enrich_events(events, devices), [{"device_id": str(i), "value": i, "model": "GPU", "site": "lab"} for i in range(100000)])
        self.assertEqual(events[0], {"device_id": "0", "value": 0})
        self.assertEqual(devices[0]["device_id"], "99999")

    def test_maximum_repeated_device(self):
        events = [{"device_id": "a", "value": i} for i in range(100000)]
        devices = [{"device_id": "a", "model": "GPU", "site": "lab"}]
        self.assertEqual(enrich_events(events, devices), [{"device_id": "a", "value": i, "model": "GPU", "site": "lab"} for i in range(100000)])

    def test_large_unused_metadata_index(self):
        devices = [{"device_id": str(i), "model": "GPU", "site": "lab"} for i in range(100000)]
        self.assertEqual(enrich_events([{"device_id": "99999"}], devices), [{"device_id": "99999", "model": "GPU", "site": "lab"}])


if __name__ == "__main__":
    unittest.main()
