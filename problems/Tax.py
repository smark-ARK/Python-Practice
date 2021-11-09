# Reading cost of meal
cost = float(input('Enter the Base cost: '))
# compute tip (lets say 18% of actual cost)
tip = (cost)*18/100
# compute tax (15% as per a search result)
tax = (cost)*15/100
# computing total bill (cost + tax + tip)
totalbill = cost+tip+tax
# print Everything by formatting in two decimal places
print('Tip:', round(tip, 2))
print('tax', round(tax, 2))
print("total bill", round(totalbill, 2))
