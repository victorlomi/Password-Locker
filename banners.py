class Banners():
    "Shows banner cards for different situations"

    def __init__(self):
        pass

    def show_title(self):
        print("****************************************************")
        print("********** Welcome to Password Locker!  ************")
        print("* The best and simplest password manager available *")
        print("****************************************************")

    def show_main_menu(self):
        print("\n****************************************************")
        print("******************* Main Menu  *********************")
        print("****************************************************")

    def show_account(self, title):
        print("\n****************************************************")
        print(f"******************* {title} *********************")
        print("****************************************************")
