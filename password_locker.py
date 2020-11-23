from banners import Banners
from account import Account

class PasswordLocker:
	"""Show the menu menu and store accounts."""

	def __init__(self):
		"""Store a banners object and an account object."""
		self.banners = Banners()
		self.account = Account()

	def show_main_menu(self, account_list):
		"""Show the main menu with the options available."""
		# show the main menu banner
		self.banners.show_main_menu()

		# print out the available accounts
		print("Accounts:")
		for i in range(len(account_list)):
			print(f"  {i+1}.{account_list[i].title()}")

		# print out the available actions
		print("Actions:")
		print("  a.Add Account")
		print("  b.Remove Account")
		print("  c.Quit")

	def store_account(self):
		"""Store a account for the password locker."""
		print("\nEnter your information to create a Password Locker Account:\n")
		self.account.username = input("Username: ")
		self.account.password = input("Password: ")

