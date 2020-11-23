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
    with open(user_file) as f_obj:
        stored_data = f_obj.readlines()
        stored_username = stored_data[0].strip()
        stored_password = stored_data[1].strip()
except FileNotFoundError:
    with open(user_file, 'w') as f_obj:
        password_locker.account.password = input("Password: ")
        f_obj.write(f"{password_locker.account.username}\n{password_locker.account.password}")
else:
    password_locker.account.password = input("Password: ")

    if password_locker.account.password == stored_password:
        print(f"\n* Welcome back {stored_username} *")
        password_locker.account.username = stored_username
        password_locker.account.password = stored_password
    else:
        password_locker.store_account()

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
    else:
        break
