def bill(price):
    tip = float(price*18/100)
    tax = float(price*20/100)
    totalBill = float(tip+tax+price)
    return round(tip, 2), round(tax, 2), round(totalBill, 2)


bill(float(input('Enter the price of the purchased Item: ')))
