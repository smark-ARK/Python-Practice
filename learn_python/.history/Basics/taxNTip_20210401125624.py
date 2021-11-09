def bill(price):
    tip = price*18/100
    tax = price*20/100
    totalBill = tip+tax+price
    return tip, tax, totalBill


bill(float(input('Enter the price of the purchased Item: ')))
