
n = int(input('Enter the number of disks: '))
p1 = []
p2 = []
p3 = []
for i in range(0, n):
    p1.append(i)

print('p1: ', p1)


def hanoi(a, b, c):
    if len(p3) == n:
        return p3
    else:
        if len(p2) != 0:
            if p1[0] > p2[0]:
                p3.insert(0, p1[0])
                p1.remove(p1[0])
                return hanoi(p1, p2, p3)
            else:
                p2.insert(0, p1[0])
        else:
            p2.insert(0, p1[0])
            p1.remove(p1[0])
            return hanoi(p1, p2, p3)
