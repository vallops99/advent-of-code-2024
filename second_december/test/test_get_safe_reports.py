import unittest
from second_december.brute_force import brute_force_method
from second_december.get_safe_reports import get_safe_reports, get_almost_safe_reports


class TestGetSafeReports(unittest.TestCase):
    def test_get_safe_reports_zero(self):
        reports = [
            [2, 2],
            [1, 7],
            [1, 2, 2],
            [1, 2, 3, 2],
            [1, 2, 3, 7],
            [7, 6, 5, 5],
            [7, 1],
        ]
        self.assertEqual(get_safe_reports(reports), 0)

    def test_get_safe_reports_ten(self):
        reports = [
            [18, 15, 12, 9, 8],
            [8, 9, 12, 15, 18],
            [1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1],
            [1, 4, 7, 10, 13],
            [13, 10, 7, 4, 1],
            [100, 97, 95, 94],
            [94, 95, 97, 100],
            [1000, 999, 998],
            [998, 999, 1000],
        ]
        self.assertEqual(get_safe_reports(reports), 10)

    def test_get_safe_reports_example(self):
        reports = [
            [
                7,
                6,
                4,
                2,
                1,
            ],
            [
                1,
                2,
                7,
                8,
                9,
            ],
            [
                9,
                7,
                6,
                2,
                1,
            ],
            [
                1,
                3,
                2,
                4,
                5,
            ],
            [
                8,
                6,
                4,
                4,
                1,
            ],
            [
                1,
                3,
                6,
                7,
                9,
            ],
        ]
        self.assertEqual(get_safe_reports(reports), 2)

    def test_get_almost_safe_reports_zero(self):
        reports = [
            [2, 2, 2],
            [1, 7, 15],
            [15, 7, 1],
            [1, 2, 2, 2],
            [2, 2, 2, 1],
            [1, 2, 3, 2, 1],
            [7, 6, 5, 5, 6],
            [6, 5, 5, 5, 7],
            [7, 1, 7],
        ]
        self.assertEqual(brute_force_method(reports), brute_force_method(reports))

    def test_get_almost_safe_reports_ten(self):
        reports = [
            [18, 15, 15, 12, 9, 8],
            [8, 9, 12, 12, 15, 18],
            [1, 1, 2, 3, 4, 5, 6],
            [6, 5, 5, 4, 3, 2, 1],
            [1, 4, 7, 10, 8, 11, 13],
            [13, 10, 7, 7, 4, 1],
            [100, 97, 95, 94, 94],
            [94, 95, 97, 100, 100],
            [1000, 999, 998, 998, 997],
            [998, 999, 1000, 1000],
        ]
        self.assertEqual(brute_force_method(reports), brute_force_method(reports))

    def test_get_almost_safe_reports_example(self):
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertEqual(brute_force_method(reports), brute_force_method(reports))

    def test_get_almost_safe_reports_missed_vectors(self):
        reports = [
            [1, 1, 1],
            [1, 2, 1],
            [1, 3, 4, 5, 8, 10, 7],
            [1, 1, 2, 1],
            [10, 7, 8, 9, 10],
            [47, 50, 48, 45, 42, 39, 38],
            [73, 75, 77, 80, 81, 78, 81, 82],
        ]
        self.assertEqual(get_almost_safe_reports(reports), brute_force_method(reports))
