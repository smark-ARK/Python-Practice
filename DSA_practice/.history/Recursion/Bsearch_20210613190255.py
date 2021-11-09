raw_data = input('Enter elements seperating with spaces: ')
data = raw_data.split()
print(data)
list = 0
for i in data:
    data += int(i)
    print(data)
