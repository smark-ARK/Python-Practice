raw_data = input('Enter elements seperating with spaces: ')
data = raw_data.split()
print(data)
lst = []
for i in data:
    i = int(i)
    lst = lst.append(i)
    print(lst)
