import unittest

from example_package_speg03.example import add_one


class TestAddOne(unittest.TestCase):
    def test_one(self):
        self.assertEqual(add_one(1), 2)

    def test_two(self):
        self.assertEqual(add_one(2), 3)

    def test_three(self):
        self.assertEqual(add_one(3), 4)
