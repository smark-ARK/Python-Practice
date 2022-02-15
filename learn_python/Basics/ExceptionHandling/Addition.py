def addition(a, b):

    c = a + b
    return c


while True:
    try:
        n1 = int(input("Enter value of a: "))
        n2 = int(input("Enter value of b: "))
    except ValueError:
        print("Kindly enter integer values: ")
    else:
        break
print(addition(n1, n2))
