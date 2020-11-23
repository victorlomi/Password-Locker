import pickle

from credentials import Credentials
from user import User
from banners import Banners
from password_locker import PasswordLocker

def get_stored_user():
    """Get user data if it's stored otherwise create a user account"""
    try:
        userdata_file = open(f"users/{password_locker.account.username}.pkl", "rb")
        stored_account = pickle.load(userdata_file)
    except FileNotFoundError:
        userdata_file = open(f"users/{password_locker.account.username}.pkl", "wb")
        password_locker.account.password = input("Password: ")
        pickle.dump(password_locker.account, userdata_file)
    else:
        password_locker.account.password = input("Password: ")

        if password_locker.account.password == stored_account.password:
            print(f"\n* Welcome back {stored_account.username} *")
            password_locker.account = stored_account

        userdata_file.close()

def get_stored_accounts():
    """Get the accounts associated with the user"""
    try:
        accounts_file = open(f"accounts/{password_locker.account.username}.pkl", "rb")
        stored_account = pickle.load(accounts_file)
        user.credentials.accounts = stored_account
    except FileNotFoundError:
        pass

def store_accounts():
    """Store the accounts in a serialized file"""
    accounts_file = open(f"accounts/{password_locker.account.username}.pkl", "wb")
    for key in user.credentials.accounts:
        pickle.dump(user.credentials.accounts, accounts_file)
    accounts_file.close()

# Initialize objects
banners = Banners()
credentials = Credentials()
user = User()
password_locker = PasswordLocker()

# Show the title card(Only show this card at the start of the program)
banners.show_title()

# Create/load Password Locker account
print("\n* Enter your information to Login *:\n")
password_locker.account.username = input("Username: ")

get_stored_user()
get_stored_accounts()

while True:
    password_locker.show_main_menu(user.get_accounts())
    choice = input("\nEnter one of the choices to proceed: ")

    if choice == 'a':
        user.view_add_account(choice)
    elif choice == 'b':
        user.view_remove_account(choice)
    elif choice == 'c':
        print("Quitting")
        break
    elif user.get_accounts()[int(choice) - 1]:
        user.view_account(int(choice))

    store_accounts()
