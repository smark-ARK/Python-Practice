
n = int(input('Enter the number of disks: '))
p1 = []
p2 = []
p3 = []
for i in range(0, n):
    p1.append(i)

print('p1: ', p1)


def hanoi(n):
    if n == 0:
        return
