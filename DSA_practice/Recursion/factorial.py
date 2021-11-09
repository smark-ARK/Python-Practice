def fact(n):
    if n == 1:
        return 1
    else:
        factorial = n*fact(n-1)
        return factorial


print("factorial of the given number is", fact(
    int(input("Enter a possitive integer: "))))
