raw_data = input('Enter elements seperating with spaces: ')
data = raw_data.split()
lst = []
for i in data:
    lst.append(int(i))
print(lst)
