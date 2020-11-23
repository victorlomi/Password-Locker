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
password_locker.store_account()

# main application loop
while True:
    password_locker.show_main_menu(user.get_accounts())
    choice = input("\nEnter one of the choices to proceed: ")

    if user.get_accounts()[int(choice)-1]:
        user.view_account(int(choice))
    else:
        break
