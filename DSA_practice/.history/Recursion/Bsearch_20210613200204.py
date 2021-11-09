n = int(input('No of elements you want in your list: '))
target = int(input('value to find: '))
lst = []
for i in range(0, n):
    raw = int(input('Enter the Elements in list: '))
    lst.append(int(raw))
data = lst
low = 0
high = 6


def Bsearch(data, target, high, low):

    if low > high:
        return 'value not found'
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return 'value found'
        elif target < data[mid]:
            return Bsearch(data, target, mid-1, low)
        else:
            return Bsearch(data, target, high, mid+1)


print(Bsearch(data, target, high, low))
