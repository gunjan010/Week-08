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

unittest.main()
