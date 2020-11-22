from account import Account

class Credentials():
    """Keeps track of the user's accounts and their credentials."""

    def __init__(self):
        """Store the accounts the user has added(Twitter by default)."""
        self.accounts = {"twitter": Account()};

    def add_account(self, name, account):
        """Add an account and its credentials to the accounts."""
        self.accounts[name] = account

    def remove_account(self, name):
        """Remove an account and its credentials to the accounts."""
        del self.accounts[name]