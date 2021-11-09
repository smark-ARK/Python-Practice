def intrest(amount):
    iPerAnn = (4/100)
    yr1 = float(amount+(amount*iPerAnn))
    yr2 = float(yr1+(yr1*iPerAnn))
    yr3 = float(yr2+(yr2*iPerAnn))
    print('Total amount in account after 1 year: ',)
