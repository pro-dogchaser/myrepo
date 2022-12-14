#!/usr/bin/env python3
import os
import tarfile
import shutil
from subprocess import call
import re

def cls():
    _ = call('clear' if os.name == 'posix' else 'cls')

def was_removed(dst):
	print("{} was removed.".format(dst))

def not_found(dst):
	print("{} not found. Skipping Step.".format(dst))

def remove_discord():
	dst = "/opt/Discord"
	if os.path.isdir(dst) == True:
		shutil.rmtree(dst)
		was_removed(dst)
	else:
		not_found(dst)

def unlink():
	dst = "/usr/bin/Discord"
	if os.path.isfile(dst) == True:
		os.unlink(dst)
		was_removed(dst)
	else:
		not_found(dst)

def menu_remove():
	dst = "/usr/share/applications/discord.desktop"
	if os.path.isfile(dst) == True:
		os.remove(dst)
		was_removed(dst)
	else:
		not_found(dst)

def extractfile(file):
	remove_discord()
	print("Extracting files.")
	with tarfile.open(file) as tar:
		tar.extractall("/opt")
	print("Files extracted.")

def symlink():
	unlink()
	print("Creating symbolic link.")
	src = "/opt/Discord/Discord"
	dst = "/usr/bin/Discord"
	os.symlink(src, dst)

def icon_menu_entry():
	print("Creating desktop icon and menu entry.")
	new_string = ""
	src = "/opt/Discord/discord.desktop"
	dst = "/usr/share/applications/discord.desktop"
	with open(src, "r+") as desktop:
		for line in desktop:
			if "Exec=" in line:
				new_string += "Exec=/usr/bin/Discord\n"
			elif "Icon=" in line:
				new_string += "Icon=/opt/Discord/discord.png\n"
			else:
				new_string += line
			desktop.write(new_string)
	shutil.copyfile(src, dst)

def filecheck(file):
	tarcontents = []
	checkforfiles = ["Discord", "Discord/discord.desktop", "Discord/discord.png"]
	fileschecked = 0
	with tarfile.open(file) as tar:
		for tarinfo in tar:
			tarcontents.append(tarinfo.name)
	for file in checkforfiles:
		if file in tarcontents:
			fileschecked += 1
	if fileschecked < 3:
		return False
	return True

def install_discord():
	running = True
	while running == True:
		cwd = os.getcwd()
		print("Your current working directory is: {}\nWhat is the file location?\nFile must be a Discord .tar.gz with its original name!\n\nType 'quit' to exit.".format(cwd))
		file = input("\n: ")
		file_filter = re.search(r"(discord)-[0-9.]*(.tar.gz)$", file)
		if file.lower() == "quit":
			running = False
		elif os.path.isfile(file) == False:
			cls()
			print("'{}' not found\n".format(file))
		elif file_filter == None or file_filter[1] + file_filter[2] != "discord.tar.gz":
			cls()
			print("You entered '{}'\nFile is not a Discord .tar.gz with its original name!\n".format(file))
		elif filecheck(file) == False:
			cls()
			print("You entered '{}'\nThe proper files were not found in the .tar.gz\n".format(file))
		else:
			cls()
			print("Installing '{}'\n".format(file))
			extractfile(file)
			symlink()
			icon_menu_entry()
			print("\nInstall complete.")
			running = False

def uninstall_discord():
	remove_discord()
	unlink()
	menu_remove()
	print("\nDiscord was uninstalled.")

#Intial Menu
running = True
while running == True:
	cls()
	print("Only use this to install Discord from .tar.gz!\nFile must have its original name.\n\nCommands:\n'1' to install (it will remove any old files)\n'2' to uninstall\n'quit' to exit")
	choice = input("\n: ")
	if choice == "1":
		cls()
		install_discord()
		running = False
	elif choice == "2":
		cls()
		print("Are you sure you want to uninstall discord?\n\nType 'yes' to continue\nType anything else to quit")
		choice = input("\n: ")
		if choice.lower() == "yes":
			cls()
			uninstall_discord()
			running = False
		else:
			running = False
	elif choice.lower() == "quit":
		running = False
	else:
		print("{} is an invalid command\n".format(choice))