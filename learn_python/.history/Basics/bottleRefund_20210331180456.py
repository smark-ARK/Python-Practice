def bottleRefund():
    l = int(input("number of containers less than 1 litr: "))
    m = int(input("number of containers more than 1 litr: "))
    Refforl = float(l*0.10)
    Refform = float(m*0.25)
    totalRef = float(Refforl+Refform)
