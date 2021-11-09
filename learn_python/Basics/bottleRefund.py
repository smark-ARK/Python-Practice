def bottleRefund():
    l = int(input("number of containers less than 1 litr: "))
    m = int(input("number of containers more than 1 litr: "))
    Refforl = float(l*0.10)
    Refform = float(m*0.25)
    totalRef = float(Refforl+Refform)
    print("Refund generated for small bottles: $", round(Refforl, 3))
    print("Refund generated for big bottles: $", round(Refform, 3))
    print("Total Refund generated : $", round(totalRef, 3))


bottleRefund()
