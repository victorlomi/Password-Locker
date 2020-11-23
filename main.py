import pickle

from credentials import Credentials
from user import User
from banners import Banners
from password_locker import PasswordLocker

# Initialize import parts of the program
banners = Banners()
credentials = Credentials()
user = User()
password_locker = PasswordLocker()

# Only show this card at the start of the program
banners.show_title()

# create password locker account
# password_locker.store_account()
user_file = "user.txt"

print("\n* Enter your information to Login *:\n")
password_locker.account.username = input("Username: ")

# check if user already has account
try:
    user_file = open(f"users/{password_locker.account.username}.pkl", "rb")
    stored_account = pickle.load(user_file)
except FileNotFoundError:
    user_file = open(f"users/{password_locker.account.username}.pkl", "wb")
    password_locker.account.password = input("Password: ")
    pickle.dump(password_locker.account, user_file)
else:
    password_locker.account.password = input("Password: ")

    if password_locker.account.password == stored_account.password:
        print(f"\n* Welcome back {stored_account.username} *")
        password_locker.account = stored_account

    user_file.close()

# try to load in saved accounts
try:
    accounts_file = open(f"accounts/{password_locker.account.username}.pkl", "rb")
    stored_account = pickle.load(accounts_file)
    user.credentials.accounts = stored_account
except FileNotFoundError:
    pass

# main application loop
while True:
    password_locker.show_main_menu(user.get_accounts()) # remove this later because it it prints at end
    choice = input("\nEnter one of the choices to proceed: ")

    if choice == 'a':
        user.view_add_account(choice)
    elif choice == 'b':
        user.view_remove_account(choice)
    elif choice == 'c':
        print("Quitting")
        break
    elif user.get_accounts()[int(choice)-1]:
        user.view_account(int(choice))

    # Store the user's accounts
    accounts_file = open(f"accounts/{password_locker.account.username}.pkl", "wb")
    for key in user.credentials.accounts:
        pickle.dump(user.credentials.accounts, accounts_file)
    accounts_file.close()

