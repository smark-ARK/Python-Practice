with open("TextFiles/guest.txt", "w") as guestname:
    while True:
        name = input("Enter your Name: ")
        if name == "":
            break
        guestname.write(f"\nWelcome {name}")
