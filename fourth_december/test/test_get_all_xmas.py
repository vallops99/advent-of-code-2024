import unittest
from fourth_december.get_all_xmas import get_all_xmas


class TestGetAllXmas(unittest.TestCase):
    def test_get_all_xmas_example(self):
        vector = [
            "....XXMAS.",
            ".SAMXMS...",
            "...S..A...",
            "MSA.A.MS.X",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(get_all_xmas(vector), 18)
