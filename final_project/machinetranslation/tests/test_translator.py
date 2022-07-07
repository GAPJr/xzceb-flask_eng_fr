"""
Testing Module
Developer: GP
"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    English to French class
    """
    def test_english_to_french(self):
        """
        English to French test cases
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('World'), 'Monde')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    """
    French to English class
    """
    def test_french_to_english(self):
        """
        French to English test cases
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Monde'), 'World')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

if __name__ == "__main__":
    unittest.main()
