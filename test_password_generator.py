import unittest
from password_generator import *


class TestPasswordGenerator(unittest.TestCase):
    """Tests for password generator functions"""

    def setUp(self):
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        self.symbols = ["@", "$", "#", "*", "-"]


    def test_get_random_letter(self):
        """Test that a random letter is returned"""
        self.assertTrue(get_random_letter() in self.letters)

    def test_get_random_symbol(self):
        """Test that a random symbol is returned"""
        self.assertTrue(get_random_symbol() in self.symbols)

    def test_generate_password(self):
        """Test that a 10 character password is returned"""
        self.assertTrue(len(generate_password()) == 10)


unittest.main()
