from credentials import Credentials
from banners import Banners
from account import Account
from password_locker import PasswordLocker

class User():
    """Handle user interaction with credentials"""

    def __init__(self):
        """Store credentials and make banners instance"""
        self.credentials = Credentials()
        self.banners = Banners()
        self.password_locker = PasswordLocker()

    def get_account_name(self, index):
        account_keys = list(self.credentials.accounts.keys())
        return account_keys[index]

    def view_account(self, index):
        """View a specific account's details and actions"""
        account_name = self.get_account_name(index-1)
        account = self.credentials.accounts[account_name]

        self.banners.show_account(account_name)

        # show choices
        print("  1. Add login credentials")
        print("  2. Check login credentials")
        print("  3. Go back")

        # ask for input
        choice = input("Enter one of the choices to proceed: ")

        # respond to input
        if(int(choice) == 1):
            print("\nEnter your username and password:\n")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.credentials.accounts[account_name] = Account(username, password)
        elif(int(choice) == 2):
            print("\nHere are your login credentials\n")
            print(f"username: {self.credentials.accounts[account_name].username}")
            print(f"password: {self.credentials.accounts[account_name].password}")
        elif(int(choice) == 3):
            print("Going back")
            self.password_locker.show_main_menu()


    def view_add_account(self):
        """View the prompt for adding an account"""
        pass

    def view_remove_account(self):
        """View the prompt for removing an account"""
        pass