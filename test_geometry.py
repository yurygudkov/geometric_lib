import unittest
import math
import random
import sys
import os

sys.path.append(os.path.dirname(__file__))

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(0), 0)


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10)
        self.assertEqual(rectangle_perimeter(1, 1), 4)


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(0), 0)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(0), 0)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(4, 2), 4)
        self.assertEqual(triangle_area(0, 10), 0)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)












class TestNegativeValues(unittest.TestCase):

    def test_circle_negative(self):
        self.assertAlmostEqual(circle_area(-3), math.pi * 9)
        self.assertAlmostEqual(circle_perimeter(-2), -4 * math.pi) 

    def test_square_negative(self):
        self.assertEqual(square_area(-4), 16)
        self.assertEqual(square_perimeter(-4), -16)


class TestInvalidInput(unittest.TestCase):

    def test_circle_invalid(self):
        with self.assertRaises(TypeError):
            circle_area("abc")
        with self.assertRaises(TypeError):
            circle_perimeter(None)

    def test_triangle_invalid(self):
        with self.assertRaises(TypeError):
            triangle_area("5", "3")


class TestEdgeCases(unittest.TestCase):

    def test_circle_zero(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_perimeter(0), 0)

    def test_small_values(self):
        self.assertAlmostEqual(circle_area(1e-6), math.pi * (1e-6)**2)
        self.assertAlmostEqual(rectangle_perimeter(1e-3, 2e-3), 2 * (1e-3 + 2e-3))


class TestRandomized(unittest.TestCase):

    def test_circle_area_random(self):
        for _ in range(5):
            r = random.uniform(0, 100)
            expected = math.pi * r * r
            self.assertAlmostEqual(circle_area(r), expected)
    def test_rectangle_perimeter_random(self):
        for _ in range(5):
            a, b = random.uniform(1, 50), random.uniform(1, 50)
            expected = 2 * (a + b)
            self.assertAlmostEqual(rectangle_perimeter(a, b), expected)


if __name__ == 'main':
    unittest.main(verbosity=2)