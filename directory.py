import os
from subprocess import call

def cls():
    _ = call('clear' if os.name == 'posix' else 'cls')
    
def cwd():
    cls()
    cwd = os.getcwd()
    print("Current working directory is: {}\n\n".format(cwd))

def cd():
    cls()
    new_directory = input("Type a path to change to: ")
    os.chdir(new_directory)
    cwd()

def mkdir():
    cls()
    directory_name = input("What will the new directory be named? ")
    os.mkdir(directory_name)
    print("Directory named {} created.\n\n".format(directory_name))
    
def dir_list():
    cls()
    path = os.getcwd()
    return_string = os.listdir(path)
    print("{}\n\n".format(return_string))

def del_dir():
    cls()
    directory_name = input("What directory would you like to delete? ")
    os.rmdir(directory_name)
    print("Directory named {} deleted.\n\n".format(directory_name))
    

cls()
running = True
while running == True:
    print("Thank you for using my directory tool. Please be careful.\n")
    print("cwd = get current working directory\n cd = change directory\n ls = list everything in current working directory\n mkdir = make directory\n del = delete directory \n quit = quit")
    command = input("\nType your command: ")
    if command == "cwd":
        cwd()
    elif command == "cd":
        cd()
    elif command == "ls":
        dir_list()
    elif command == "mkdir":
        mkdir()
    elif command == "del":
        del_dir()
    elif command == "quit":
        running = False
    else:
        print("Invalid command")
cls()
print("Hope you were careful...")