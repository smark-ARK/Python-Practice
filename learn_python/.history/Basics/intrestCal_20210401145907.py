def intrest(amount):
    iPerAnn = (4/100)
    yr1 = float(amount+(amount*iPerAnn))
    yr2 = float(yr1+(yr1*iPerAnn))
    yr3 = float(yr2+(yr2*iPerAnn))
    print('Total amount in account after 1 year: ', round(yr1, 2))
    print('Total amount in account after 2 year: ', round(yr2, 2))
    print('Total amount in account after 3 year: ', round(yr3, 2))
