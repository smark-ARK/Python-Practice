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


"Default arguments"


def printinfo(name, age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)


# Now you can call printinfo function
printinfo(age=50, name="miki")
printinfo(name="miki")


# Function definition is here
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
        return


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)

# Anonymous func


def sum(arg1, arg2): return arg1 + arg2


# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))


# Return stmt
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)
