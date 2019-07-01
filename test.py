import unittest
import numpy
from MyLib import *

class TestPolynomial(unittest.TestCase):
    def test_correct_polynomial(self):
        '''
        This test checks that the function computing the value of the two dimensional polynomial
        correctly.
        '''
        x = numpy.linspace(-1, 1)
        X, Y = numpy.meshgrid(x, x)
        c = [1, 1, 1, 1, 1, 1]
        t1 = c[1] * X
        t2 = c[2] * Y
        t3 = c[3] * X * Y
        t4 = c[4] * X ** 2
        t5 = c[5] * Y ** 2
        result0 = c[0] + t1 + t2 + t3 + t4 + t5

        result1 = GeneralPolynomial(c, X, Y)

        self.assertEqual(result1.all(), result0.all(), 'Function should equal the handwritten expression')

if __name__ == 'main':
    unittest.main()