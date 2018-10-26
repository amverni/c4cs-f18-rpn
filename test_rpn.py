import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.caclulate('1 1 +')
        self.assertEqual(2, result)

    def test_sub(self):
        result = rpn.caclulate('4 3 -')
        self.assertEqual(1, result)

