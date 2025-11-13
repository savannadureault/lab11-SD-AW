# https://github.com/savannadureault/lab11-SD-AW.git
# Partner 1: Savanna Dureault
# Partner 2: Abigail Welsh

import math
from unittest import TestCase
from calculator import *

class test_calculator(TestCase):
    def test_multiply(self):
        # This is a simple test case using the assertEqual method
        self.assertEqual(mul(2, 3), 6)

    #def test_divide(self):
        #self.assertEqual(div(-1, -1), 1)

    def test_log_invalid_argument(self):
        self.assertEqual(log(10, 3), 0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self):
        self.assertEqual(square_root(1, 1), 1)


