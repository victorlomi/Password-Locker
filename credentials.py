from account import Account

class Credentials():
    """Keeps track of the user's accounts and their credentials."""

    def __init__(self):
        """Store the accounts they user as added(Twitter by default)."""
        self.accounts = {"twitter": Account()};

    def add_account(self, account):
        """Add an account and its credentials to the accounts."""
        pass

    def remove_account(self, account):
        """Remove an account and its credentials to the accounts."""
        pass
