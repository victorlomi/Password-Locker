def show_main_menu():
    print("\n****************************************************")
    print("******************* Main Menu  *********************")
    print("****************************************************")

    print("Accounts:")
    print("  1.Twitter")
    print("Actions:")
    print("  2.Add Account")
    print("  3.Remove Account")

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