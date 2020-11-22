from credentials import Credentials
from user import User
from banners import Banners

banners = Banners()
credentials = Credentials()
user = User()

def show_main_menu():
    # show the main menu banner
    banners.show_main_menu()
    
    # print out the available accounts
    print("Accounts:")
    i = 0
    for account in credentials.accounts:
        i += 1
        print(f"  {i}.{account.title()}")

    # print out the available actions
    print("Actions:")
    print("  a.Add Account")
    print("  b.Remove Account")


# Only show this card at the start of the program
banners.show_title()

# main application loop
while True:
    show_main_menu()
    choice = input("\nEnter one of the choices to proceed: ")

    if(choice == 1):
        user.view_account()
    else:
        break
