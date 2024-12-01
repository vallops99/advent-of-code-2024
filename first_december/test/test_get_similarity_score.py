import unittest
from first_december.get_similarity_score import get_similarity_score


class TestGetSimilarityScore(unittest.TestCase):
    def test_must_be_zero(self):
        left = [0, 1, 2, 3, 4, 5, 6, 7]
        right = [8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(get_similarity_score(left, right), 0)

    def test_must_be_10(self):
        left = [1, 2, 3, 4]
        right = [1, 2, 3, 4]
        self.assertEqual(get_similarity_score(left, right), 10)
