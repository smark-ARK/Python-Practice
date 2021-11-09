def bottleRefund():
    l = int(input("number of containers less than 1 litr: "))
    m = int(input("number of containers more than 1 litr: "))
    Refforl = float(l*0.10)
    Refform = float(m*0.25)
    totalRef = float(Refforl+Refform)
    print("Refund generated for small bottles: $", Refforl)
    print("Refund generated for big bottles: $", Refform)
    print("Total Refund generated : $", totalRef)


bottleRefund()
