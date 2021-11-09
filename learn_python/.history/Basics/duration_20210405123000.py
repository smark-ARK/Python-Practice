dStr = input(
    'Enter the number of days,hours,minutes,seconds by seperating with spaces: ')
dspl = dStr.split()
print(dspl)
days = dspl[0]
hours = dspl[1]
mins = dspl[2]
secs = dspl[3]

durinSec = (days*24*60*60)+(hours*60*60)+(mins*60)+secs
