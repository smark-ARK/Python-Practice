l = list(input('Enter the values specifying 0 as an End: '))
k = []
sum = 0
len = len(l)-1
if l[len] != '0':
    print('Zero de re last me!!!')
    exit()
else:
    for i in l[:(len)]:
        i = int(i)
        k.append(i)
for j in k:
    sum += j
a = k.__len__()
avg = sum/a
print('Average: ', avg)
