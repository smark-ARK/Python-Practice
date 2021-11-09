def bill(price):
    tip = float(price*18/100)
    tax = float(price*20/100)
    totalBill = float(tip+tax+price)
    print('Tip: ', round(tip, 2))
    print('Tax: ', round(tax, 2))
    print('Total Bill to be Paid', round(totalBill, 2))
    return 'Thank u for Eating Here, Visit again :-)'


print(bill(float(input('Enter the price of the purchased Item: '))))
