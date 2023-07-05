import unittest
from v1.keep_alive_estimates import keep_alive_estimates


class TestKeepAliveEstimates(unittest.TestCase):
    def test_estimates_with_keepalive_0(self):
        files = ["data/test_short.json"]
        result = keep_alive_estimates(files, 0)

        expected_dict = {0: 2, 1: 3, 2: 3, 3: 2}
        self.assertEqual(4, len(result))
        self.assertDictEqual(expected_dict, result)

    def test_estimates_mergable_keepalive_0(self):
        files = ["data/test_short_mergable.json"]
        result = keep_alive_estimates(files, 0)

        expected_dict = {0: 1, 1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: 1, 11: 1, 12: 1}
        self.assertEqual(13, len(result))
        self.assertDictEqual(expected_dict, result)

    def test_estimates_mergable_keepalive_1(self):
        files = ["data/test_short_mergable.json"]
        result = keep_alive_estimates(files, 1)

        expected_dict = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 0, 9: 0, 10: 1, 11: 1, 12: 1, 13: 1}
        self.assertEqual(len(result), 14)
        self.assertDictEqual(expected_dict, result)

    def test_estimates_mergable_keepalive_3(self):
        files = ["data/test_short_mergable.json"]
        result = keep_alive_estimates(files, 3)

        expected_dict = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1}
        self.assertEqual(16, len(result))
        self.assertDictEqual(expected_dict, result)


if __name__ == '__main__':
    unittest.main()
