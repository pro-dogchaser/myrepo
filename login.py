#!/usr/bin/env python3
from subprocess import call
import os
import hashlib
import getpass
import pickle
import re

def cls():
    _ = call('clear' if os.name == 'posix' else 'cls')

def accounts():
	if os.path.isfile("accounts.bin") == True:
		with open("accounts.bin", "rb") as accounts:
			accounts_dict = pickle.load(accounts)
	else:
		accounts_dict = {}
	return accounts_dict

def password_filter(password):
	pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
	match = re.search(pattern, password)
	if match:
		return True
	else:
		return False

def new_account_entry(accounts_dict):
	cls()
	running = True
	while running == True:
		print("Please create a new account.\nEnter your new username or 'quit' to go to the main menu.\n")
		new_username = input("New username: ")
		if new_username in accounts_dict.keys():
			cls()
			print("{} already taken.\n".format(new_username))
			running = False
		elif new_username == "quit":
			running = False
			cls()
		elif new_username == "new_account":
			cls()
			print("Invalid username.\n")
		else:
			cls()
			print("Hello {}! Enter your new password.\nPassword must have one number, one uppercase and lowercase letter, one symbol, and must be between 6 - 20 characters long.\n".format(new_username))
			new_password = getpass.getpass("New password: ")
			if password_filter(new_password) == False:
				cls()
				print("Invalid password.\n")
			else:
				cls()
				print("Please confirm new password")
				password_confirm = getpass.getpass("\nConfirm password: ")
				if new_password == password_confirm:
					salt = os.urandom(32)
					key = hashlib.pbkdf2_hmac("sha256", new_password.encode("utf-8"), salt, 100000)
					accounts_dict[new_username] = {"salt": salt, "key": key}
					with open("accounts.bin", "wb") as accounts:
						pickle.dump(accounts_dict, accounts)
					running = False
					cls()
					print("Account created\n")
				else:
					cls()
					print("Passwords didn't match\n")
					
def main():
	cls()
	running = True
	while running == True:
		accounts_dict = accounts()
		if os.path.isfile("accounts.bin") == False:
			new_account_entry(accounts_dict)
		print("Please enter your user name. If you need to create an account, enter 'new_account'\nType 'quit' to quit.")
		user_login = input("\nUsername: ")
		if user_login == "quit":
			running = False
		elif user_login == "new_account":
			new_account_entry(accounts_dict)
		elif user_login in accounts_dict.keys():
			attempts = 0
			while attempts < 3:
				cls()
				print("Hello {}! Please enter your password.\nAttempt {}/3".format(user_login, attempts))
				user_password = getpass.getpass("\nPassword: ")
				salt = accounts_dict[user_login]["salt"]
				key = accounts_dict[user_login]["key"]
				new_key = hashlib.pbkdf2_hmac("sha256", user_password.encode("utf-8"), salt, 100000)
				if key == new_key:
					cls()
					print("Welcome {}! You have succesfully authenticated!".format(user_login))
					break
				else:
					cls()
					print("Incorrect password. Try again.\n")
					attempts += 1
			if attempts == 3:
				cls()
				print("Too many incorrect attempts.")
			running = False
		else:
			cls()
			print("{} not found.\n".format(user_login))
main()