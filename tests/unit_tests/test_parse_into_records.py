import unittest
from v1.keep_alive_estimates import parse_into_records


class TestParseIntoRecords(unittest.TestCase):

    def test_parse_into_records_single_file(self):
        files = ["data/test_short.json"]
        result = parse_into_records(files)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, [('0', 0, 2), ('1', 0, 3), ('2', 1, 2)])

    def test_parse_with_missing_value(self):
        files = ["data/test_with_missing_value.json"]
        result = parse_into_records(files)

        self.assertEqual(len(result), 1)
        self.assertEqual(result, [('0', 0, 10)])


if __name__ == '__main__':
    unittest.main()
