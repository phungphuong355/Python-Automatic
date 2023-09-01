#! /usr/bin/env python

from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEquals(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEquals(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEquals(rearrange_name(testcase), expected)

    def test_invaid(self):
        self.assertRaises(TypeError, rearrange_name, 88)


if __name__ == "__main__":
    unittest.main()
