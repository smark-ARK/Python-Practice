def bill(price):
    tip = float(price*18/100)
    tax = float(price*20/100)
    totalBill = float(tip+tax+price)
    return 'tip: ', round(tip, 2), '\n', 'Tax: ', round(tax, 2), '\n', 'Total bill to  be paid: ', round(totalBill, 2)


print(bill(float(input('Enter the price of the purchased Item: '))))
