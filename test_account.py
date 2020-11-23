import unittest
from account import Account

class TestAccount(unittest.TestCase):
    """Tests for the class Account."""

    def test_account_creation(self):
        """Test that accounts can be created."""
        account = Account("user1", "123")
        self.assertEqual(account.username, "user1")
        self.assertEqual(account.password, "123")

unittest.main()
