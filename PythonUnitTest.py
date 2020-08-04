from validate_name import validate
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Johnny, Cage"
        expected = "Cage Johnny"
        self.assertEqual(validate(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = "Invalid input. First name and Last name must be composed of letters only. Follow this input format: last name, first name"
        self.assertEqual(validate(testcase), expected)

    def test_double_name(self):
        testcase = "Johnny, Cage M."
        expected = "Cage M. Johnny"
        self.assertEqual(validate(testcase), expected)

    def test_special_character(self):
        testcase = "Michael, /*"
        expected = "Invalid input. First name and Last name must be composed of letters only. Follow this input format: last name, first name"
        self.assertEqual(validate(testcase), expected)

unittest.main()