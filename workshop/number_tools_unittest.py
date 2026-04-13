import unittest
from number_tools import *

class TestNumberTools(unittest.TestCase):

    def test_is_even(self):
        # Test even integer
        self.assertEqual(is_even(10), True)
        # Test odd integer
        self.assertEqual(is_even(7), False)
        # Test zero
        self.assertEqual(is_even(0), True)
        # Test errors
        self.assertRaises(TypeError, is_even, 3.5)

    def test_average(self):
        self.assertEqual(average([2,4,6,8]), 5)
        self.assertAlmostEqual(average([1.5,2.5,3.5]), 2.5)
        self.assertRaises(TypeError, average, "not a list")
        self.assertRaises(ValueError, average, [])
        self.assertRaises(TypeError, average, [1, 2, "three"])
        

unittest.main()
