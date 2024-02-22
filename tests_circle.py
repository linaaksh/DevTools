import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
	res = area(1)
        self.assertEqual(res, 3.14159)

    def test_rand_area(self):
	res = area(5)
        self.assertEqual(res, 78.53982)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_per(self):
	res = perimeter(1)
        self.assertEqual(res, 6.283184)

    def test_rand_per(self):
	res = perimeter(5)
        self.assertEqual(res, 31.41592)