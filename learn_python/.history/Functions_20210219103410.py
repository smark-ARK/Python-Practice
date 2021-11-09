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
