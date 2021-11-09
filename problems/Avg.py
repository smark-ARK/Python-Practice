n = int(input('How many values do u have: '))
lst = []
for i in range(0, n):
    ls = int(input('Enter the values one by one: '))
    lst.append(ls)
    print(lst)
print(lst)
sum = 0
for j in lst:
    sum = sum + j
Avg = sum/n

print('Average of the given sequence is', Avg)
