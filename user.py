from credentials import Credentials

class User():
    """Handle user interaction with credentials"""

    def __init__(self):
        """Store credentials"""
        self.credentials = Credentials()

    def view_account(self):
        """View a specific account's details and actions"""
        pass

    def view_add_account(self):
        """View the prompt for adding an account"""
        pass

    def view_remove_account(self):
        """View the prompt for removing an account"""
        pass