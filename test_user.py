import unittest

from user import User

class TestUser(unittest.TestCase):
    """Tests for class User."""
    
    def test_get_account_name(self):
        """Test that user can use index to get the key of account."""
        user = User()
        self.assertEqual(user.get_account_name(0), "twitter")

unittest.main()