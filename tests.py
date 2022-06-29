import unittest
from helpers import create_person_id, text_matches, get_quote

class TestHelperMethods(unittest.TestCase):

    def test_create_person_id(self):
        self.assertEqual(create_person_id("Angelica Ross"), "angelica_ross")

    def test_text_matches(self):
        match_phrase = "hello"
        self.assertTrue(text_matches("hello", match_phrase))
        self.assertTrue(text_matches("Hello", match_phrase))
        self.assertTrue(text_matches("hello!", match_phrase))
        self.assertTrue(text_matches("HelLo!", match_phrase))

    def test_get_guotes(self):
        self.assertEqual(get_quote(), 200)

if __name__ == '__main__':
    unittest.main()