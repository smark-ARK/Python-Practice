raw_data = input('Enter elements seperating with spaces in asxending order: ')
data = raw_data.split()
lst = []
for i in data:
    lst.append(int(i))
data = lst


def Bsearch(data, target, high, low):

    if low > high:
        return 'value not found'
    else:
        mid = (low+high)//2
        if target == data[data]:
            return 'value found'
        elif target < data[mid]:
            return Bsearch(data, target, mid-1, low)
        else:
            return Bsearch(data, target, high, low)
