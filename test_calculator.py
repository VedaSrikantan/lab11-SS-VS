# https://github.com/VedaSrikantan/lab11-SS-VS.git
# Partner 1: Sarah Spellman
# Partner 2: Veda Srikantan

import unittest
from calculator import *
#https://github.com/VedaSrikantan/lab11-SS-VS.git
#Partner 1: Sarah Spellman
#Partner 2: Veda Srikantan


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,5),8)
        self.assertEqual(add(7,-3),4)
        self.assertEqual(add(-4,-6),-10)
    #     fill in code

    def test_subtract(self):
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(7, -3), 10)
        self.assertEqual(subtract(-4, -6), 2)
    # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,5),0)
        self.assertEqual(mul(-1,10),-10)
        self.assertEqual(mul(5,11),55)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,2),0.5)
        self.assertEqual(div(5,10),2)
        self.assertEqual(div(-1,5),-5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
    #     fill in code

    def test_logarithm(self):
        self.assertEqual(logarithm(1,11),0)
        self.assertEqual(logarithm(1,9),0)
        self.assertEqual(logarithm(1,10),0)
    # 3 assertions
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0,10)
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(4,3),5)
        self.assertAlmostEqual(hypotenuse(6,7),9.2195,places=3)
        self.assertAlmostEqual(hypotenuse(1,7),7.0710,places=3)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(6),2.4495,places=3)
        self.assertEqual(square_root(4),2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()