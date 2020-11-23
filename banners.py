class Banners:
    """Shows banner cards for different situations."""

    def __init__(self):
        pass

    def show_title(self):
        """Show the password locker title banner."""
        print("****************************************************")
        print("********** Welcome to Password Locker!  ************")
        print("* The best and simplest password manager available *")
        print("****************************************************")

    def show_main_menu(self):
        """Show the main menu title banner."""
        print("\n****************************************************")
        print("******************* Main Menu  *********************")
        print("****************************************************")

    def show_account(self, title):
        """Show the account title banner."""
        print("\n****************************************************")
        print(f"******************* {title.title()} *********************")
        print("****************************************************")

    def show_choices(self, choice):
        """Show either the add account or remove account page."""
        if choice == 'a':
            self.show_account("add account")
        else:
            self.show_account("remove account")

