import unittest
from translator import englishToFrench, frenchToEnglish

class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Suis')
        self.assertNotEqual(englishToFrench("None"), "")

class test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Proud')
        self.assertNotEqual(frenchToEnglish("None"), "")

unittest.main()
