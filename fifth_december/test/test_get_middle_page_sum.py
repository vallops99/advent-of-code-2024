import unittest
from fifth_december.get_middle_page_sum import (
    get_middle_page_sum,
    get_middle_fixed_page_sum,
)


class TestGetMiddlePageSum(unittest.TestCase):
    def test_get_middle_page_sum_example(self):
        rules = {
            "47": [53, 13, 61, 29],
            "97": [13, 61, 47, 29, 53, 75],
            "75": [29, 53, 47, 61, 13],
            "61": [13, 53, 29],
            "29": [13],
            "53": [29, 13],
        }
        data = [
            [
                75,
                47,
                61,
                53,
                29,
            ],
            [
                97,
                61,
                53,
                29,
                13,
            ],
            [
                75,
                29,
                13,
            ],
            [
                75,
                97,
                47,
                61,
                53,
            ],
            [
                61,
                13,
                29,
            ],
            [
                97,
                13,
                75,
                29,
                47,
            ],
        ]

        self.assertEqual(get_middle_page_sum(rules, data), 143)

    def test_get_middle_fixed_page_sum_example(self):
        rules = {
            "47": [53, 13, 61, 29],
            "97": [13, 61, 47, 29, 53, 75],
            "75": [29, 53, 47, 61, 13],
            "61": [13, 53, 29],
            "29": [13],
            "53": [29, 13],
        }
        data = [
            [
                75,
                47,
                61,
                53,
                29,
            ],
            [
                97,
                61,
                53,
                29,
                13,
            ],
            [
                75,
                29,
                13,
            ],
            [
                75,
                97,
                47,
                61,
                53,
            ],
            [
                61,
                13,
                29,
            ],
            [
                97,
                13,
                75,
                29,
                47,
            ],
        ]

        self.assertEqual(get_middle_fixed_page_sum(rules, data), 123)
