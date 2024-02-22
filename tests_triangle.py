import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(7, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_one_area(self):
	res = area(1, 8)
        self.assertEqual(res, 4)

    def test_rand_area(self):
	res = area(16, 3)
        self.assertEqual(res, 24)

    def test_zero_per(self):
        res = perimeter(0, 4, 2)
        self.assertEqual(res, 6)
       
    def test_same_per(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_one_per(self):
	res = perimeter(1, 1, 6)
        self.assertEqual(res, 8)

    def test_rand_per(self):
	res = perimeter(5, 11, 19)
        self.assertEqual(res, 35)