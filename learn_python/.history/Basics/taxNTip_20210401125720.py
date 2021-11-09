def bill(price):
    tip = float(price*18/100)
    tax = float(price*20/100)
    totalBill = float(tip+tax+price)
    return tip, tax, totalBill


bill(float(input('Enter the price of the purchased Item: ')))
