import unittest
from text_tools import *

class TestTextTools(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels(""), 0)
        self.assertRaises(TypeError, count_vowels, 123)
        
unittest.main()