import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(dicts.get_val({"a": "A", "b": "B", "c": "C"}, "b"), "B")
        self.assertEqual(dicts.get_val({"a": "A", "b": "B", "c": "C"}, "b", "o_O"), "B")
        self.assertEqual(dicts.get_val({"a": "A", "b": "B", "c": "C"}, "s", "o_O"), "o_O")
