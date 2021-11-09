kmno = int(input('Enter the no. of kilometers: '))


def fare(kmno):
    base = 4
    plus = 0.25
    kmmtr = kmno*1000

    fpkm = kmmtr/140+plus
    totalfare = 4+fpkm
