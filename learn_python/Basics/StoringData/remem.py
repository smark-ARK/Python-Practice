import json


def readj():
    try:
        with open("Basics/StoringData/username.json") as uname:
            user = json.load(uname)
    except FileNotFoundError:
        print("No users found")
        writej()
    else:
        con = input(f"Enter y if {user} is your username: ")
        if con == "y":
            return f"Welcome back {user}"
        else:
            return writej()


def writej():
    with open("Basics/StoringData/username.json", "w") as wname:
        user = input("Enter the name: ")
        json.dump(user, wname)
        return "Have a nice day"


print(readj())
