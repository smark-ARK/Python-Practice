ls = input('Enter the numberes by seperating with space: ')
lss = ls.split()
print(lss)
sum = 0
lst = []
for i in lss:
    n = int(i)
    lst.append(n)
for j in lst:
    sum += j
avg = sum/len(lst)
print('Average: ', avg)
