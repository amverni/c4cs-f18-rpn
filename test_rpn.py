import unittest
import rpn
from fractions import Fraction

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)

    def test_mult(self):
        result = rpn.calculate('2 5 *')
        self.assertEqual(10, result)

    def test_div(self):
        result = rpn.calculate('25 5 /')
        self.assertEqual(5, result)

    def test_chain(self):
        result = rpn.calculate('1 1 + 2 *')
        self.assertEqual(4, result)

    def test_exponent(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)

    def test_fraction(self):
        result = rpn.calculate('1 2 /')
        result = rpn.calculate('d2f')
        self.assertEqual(Fraction(0.5), result)
        result = rpn.calculate('d2f')
        self.assertEqual(Fraction(0.5), result)
        result = rpn.caclulate('f2d')
        self.assertEqual(0.5, result)
        result = rpn.caclulate('f2d')
        self.assertEqual(0.5, result)

#    def test_repeat(self):
