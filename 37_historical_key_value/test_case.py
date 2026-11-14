"""Visible tests import the learner implementation, never the reference."""
import unittest

if __package__:
    from .main import TimeMap
else:
    from main import TimeMap


class TestCases(unittest.TestCase):
    def test_boundaries(self):
        store = TimeMap()
        store.set('a', 'old', 3)
        store.set('a', 'new', 8)
        self.assertEqual([store.get('a', t) for t in (2, 3, 7, 8, 99)], [None, 'old', 'old', 'new', 'new'])

    def test_interleaved_keys(self):
        store = TimeMap()
        store.set('a', 'A', 10)
        store.set('b', 'B', 1)
        self.assertEqual(store.get('a', 10), 'A')
        self.assertEqual(store.get('b', 1), 'B')
        self.assertIsNone(store.get('missing', 100))

    def test_empty_value_and_zero_timestamp(self):
        store = TimeMap()
        store.set('a', '', 0)
        self.assertEqual(store.get('a', 0), '')

    def test_rejected_write_preserves_history(self):
        store = TimeMap()
        store.set('a', 'good', 5)
        for timestamp in (5, 4):
            with self.assertRaises(ValueError):
                store.set('a', 'bad', timestamp)
        self.assertEqual(store.get('a', 5), 'good')
        store.set('a', 'later', 6)
        self.assertEqual(store.get('a', 6), 'later')

    def test_instances_are_independent(self):
        a, b = TimeMap(), TimeMap()
        a.set('x', 'one', 1)
        self.assertIsNone(b.get('x', 1))

    def test_many_versions_against_scan(self):
        store = TimeMap()
        for t in range(0, 100, 3):
            store.set('a', str(t), t)
        for query in range(105):
            eligible = [t for t in range(0, 100, 3) if t <= query]
            self.assertEqual(store.get('a', query), str(max(eligible)) if eligible else None)


if __name__ == "__main__":
    unittest.main()
