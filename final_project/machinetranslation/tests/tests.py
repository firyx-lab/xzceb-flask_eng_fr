import unittest
from machinetranslation.translator import english_to_french, french_to_english
from ibm_cloud_sdk_core.api_exception import ApiException

class TestTranslator(unittest.TestCase):
    def test_english_to_french_null(self):
        with self.assertRaises(ApiException):
                english_to_french('')
    
    def test_french_to_english_null(self):
        with self.assertRaises(ApiException):
                french_to_english('')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french('Cat'), 'Dog')

    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english('madame'), 'husband')

if __name__ == "__main__":
    unittest.main()