import unittest
from helpers import create_person_id

class TestHelperMethods(unittest.TestCase):

    def test_create_person_id(self):
        self.assertEqual(create_person_id("Angelica Ross"), "angelica_ross")

if __name__ == '__main__':
    unittest.main()