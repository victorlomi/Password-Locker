from credentials import Credentials

credentials = Credentials()

def show_main_menu():
    # show the main menu banner
    print("\n****************************************************")
    print("******************* Main Menu  *********************")
    print("****************************************************")

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

def show_title_card():
    print("****************************************************")
    print("********** Welcome to Password Locker!  ************")
    print("* The best and simplest password manager available *")
    print("****************************************************")

# Only show this card at the start of the program
show_title_card()

# main application loop
while True:
    show_main_menu()
    choice = input("\nEnter one of the choices to proceed: ")