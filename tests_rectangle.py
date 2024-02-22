import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_one_area(self):
	res = area(1, 7)
        self.assertEqual(res, 7)

    def test_rand_area(self):
	res = area(16, 19)
        self.assertEqual(res, 304)

    def test_zero_per(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
       
    def test_square_per(self):
        res = perimeter(100, 100)
        self.assertEqual(res, 400)

    def test_one_per(self):
	res = perimeter(9, 1)
        self.assertEqual(res, 20)

    def test_rand_per(self):
	res = perimeter(5, 11)
        self.assertEqual(res, 32)