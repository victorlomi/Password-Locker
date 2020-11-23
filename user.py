from credentials import Credentials
from banners import Banners
from account import Account
from password_locker import PasswordLocker
import password_generator as password_gen

class User():
    """Handle user interaction with credentials"""

    def __init__(self):
        """Store credentials and make banners instance"""
        self.credentials = Credentials()
        self.banners = Banners()
        self.password_locker = PasswordLocker()
        self.choices = ["instagram", "facebook", "twitch", "discord"]

    def get_account_name(self, index):
        account_keys = list(self.credentials.accounts.keys())
        return account_keys[index]

    def get_accounts(self):
        return list(self.credentials.accounts.keys())

    def view_account(self, index):
        """View a specific account's details and actions"""
        account_name = self.get_account_name(index - 1)
        account = self.credentials.accounts[account_name]

        self.banners.show_account(account_name)

        # show choices
        print("  1. Add login credentials")
        print("  2. Check login credentials")
        print("  3. Go back")

        # ask for input
        choice = input("Enter one of the choices to proceed: ")

        # respond to input
        if int(choice) == 1:
            print("\n* Add Login Credentials: *\n")
            username = input("Enter your username: ")

            # check to generate password
            password_choice = input("Do you want a generated password? (yes/no): ")
            if password_choice.lower() == 'yes':
                password = password_gen.generate_password()
            elif password_choice.lower() == 'no':
                password = input("Enter your password: ")

            self.credentials.accounts[account_name] = Account(username, password)
            self.view_account(index)
        elif int(choice) == 2:
            print("\n* Check Login Credentials: *\n")
            print(f"username: {self.credentials.accounts[account_name].username}")
            print(f"password: {self.credentials.accounts[account_name].password}")
            self.view_account(index)
        elif int(choice) == 3:
            print("* Going Back *")
            # self.password_locker.show_main_menu(self.get_accounts)

    def view_add_account(self, choice):
        """View the prompt for adding an account"""
        self.banners.show_choices(choice)

        choice_number = 0
        for choice_number in range(len(self.choices)):
            print(f"  {choice_number+1}.{self.choices[choice_number].title()}")
        print(f"  {choice_number+2}.Other")

        # add the account to the account list
        account_to_add = input("\nEnter one of the choices to proceed: ")

        if account_to_add == '1':
            self.credentials.add_account(self.choices[0], Account())
        elif account_to_add == '2':
            self.credentials.add_account(self.choices[1], Account())
        elif account_to_add == '3':
            self.credentials.add_account(self.choices[2], Account())
        elif account_to_add == '4':
            self.credentials.add_account(self.choices[3], Account())
        elif account_to_add == '5':
            account_name = input("\nEnter the name of the platform: ")
            self.credentials.add_account(account_name, Account())
        else:
            print("Invalid choice")


    def view_remove_account(self, choice):
        """View the prompt for removing an account"""
        pass

