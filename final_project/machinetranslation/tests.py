import unittest

from .translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('World'), 'Monde')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Monde'), 'World')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()