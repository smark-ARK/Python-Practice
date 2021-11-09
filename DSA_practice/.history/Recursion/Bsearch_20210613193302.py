raw_data = input('Enter elements seperating with spaces in asxending order: ')
data = raw_data.split()
lst = []
for i in data:
    lst.append(int(i))
print(lst)
