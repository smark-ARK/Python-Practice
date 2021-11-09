dStr = input(
    'Enter the number of days,hours,minutes,seconds by seperating with spaces: ')
dspl = dStr.split()
print(int(dspl))
days = int(dspl[0])
hours = int(dspl[1])
mins = int(dspl[2])
secs = int(dspl[3])

durinSec = (days*24*60*60)+(hours*60*60)+(mins*60)+secs
print('Duration in seconds:', durinSec)
