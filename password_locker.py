from banners import Banners
from account import Account

class PasswordLocker():

	def __init__(self):
		self.banners = Banners()
		self.account = Account()

	def show_main_menu(self):
		# show the main menu banner
		self.banners.show_main_menu()

		# print out the available accounts
		print("Accounts:")

		# print out the available actions
		print("Actions:")
		print("  a.Add Account")
		print("  b.Remove Account")

	def store_account(self):
		"""Store a account for the password locker"""
		print("\nEnter your information to create a Password Locker Account:\n")
		self.account.username = input("Username: ")
		self.account.password = input("Password: ")