raw_data = input('Enter elements seperating with spaces: ')
data = raw_data.split()
print(data)
for i in data:
    data += int(i)
