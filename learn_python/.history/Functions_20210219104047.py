def printme(str):
    print(str)


printme("ARK Loves Sumeria")

"Pass by reference"


def changeme(myList):
    print("values before change: ", myList)
    myList[2] = 50
    print("Values after change: ", myList)


myList = [10, 20, 30]

changeme(myList)

print("Values outside fuction", myList)


"keyword args"


def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)


# Now you can call printinfo function
printinfo(age=50, name="miki")
