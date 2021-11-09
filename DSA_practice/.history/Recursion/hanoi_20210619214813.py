
n = int(input('Enter the number of disks: '))
p1 = []
p2 = []
p3 = []
for i in range(0, n):
    p1.append(i)

print('p1: ', p1)


def hanoi(n):
    if len(p3) == n:
        return p3
    else:
        p2.append(p1[0])
