import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """Tests for the class Credentials."""

    def test_add_account(self):
        """Test that an account can be added."""
        credentials = Credentials()
        credentials.add_account({"facebook": {}})

        self.assertTrue("facebook" in credentials)
    
    def test_remove_account(self):
        """Test that an account can be removed"""
        credentials = Credentials()
        credentials.remove_account("twitter")

        self.assertFalse("twitter" in credentials)



unittest.main()

