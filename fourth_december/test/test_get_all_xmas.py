import unittest
from fourth_december.get_all_xmas import get_all_xmas, get_all_mas_x_shaped


class TestGetAllXmas(unittest.TestCase):
    def test_get_all_xmas_example(self):
        vector = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(get_all_xmas(vector), 18)

    def test_get_all_mas_x_shaped_example(self):
        vector = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(get_all_mas_x_shaped(vector), 9)
