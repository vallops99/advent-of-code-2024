from first_december.get_distance import get_distance
import unittest


class TestGetDistance(unittest.TestCase):
    def test_must_be_zero(self):
        ordered_list = [0, 1, 2, 3, 4, 5]
        self.assertEqual(get_distance(ordered_list, ordered_list), 0)

    def test_must_be_10(self):
        left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(get_distance(left, right), 10)
