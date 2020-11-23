import unittest
from password_locker import PasswordLocker

class TestPasswordLocker(unittest.TestCase):
    """These are tests for the class PasswordLocker"""

    def test_store_account(self):
        """Test that accounts are stored"""
        password_locker = PasswordLocker()
        password_locker.store_account()

        self.assertEqual(password_locker.account.username, "victor")
        self.assertEqual(password_locker.account.password, "123")


unittest.main()
