import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
	res = area(1)
        self.assertEqual(res, 1)

    def test_rand_area(self):
	res = area(5)
        self.assertEqual(res, 25)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_per(self):
	res = perimeter(1)
        self.assertEqual(res, 4)

    def test_rand_per(self):
	res = perimeter(6)
        self.assertEqual(res, 24)