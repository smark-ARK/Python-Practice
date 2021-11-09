def bottleRefund():
    l = int(input("number of containers less than 1 litr: "))
    m = int(input("number of containers more than 1 litr: "))
    Refforl = float(l*0.10)
    Refform = float(m*0.25)
    totalRef = float(Refforl+Refform)
    print("Refund generated for small bottles: $", round(Refforl, 2))
    print("Refund generated for big bottles: $", round(Refform, 2))
    print("Total Refund generated : $", round(totalRef, 2))


bottleRefund()
