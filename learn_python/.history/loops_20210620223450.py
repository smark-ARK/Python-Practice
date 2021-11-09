""" # while loop
n = 0
while n < 10:

    n += 1
    print(n)
else:
    print('Loop terminated as n==10')

# For Loop
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    print(i)
    sum += i
else:
    print(sum)
 """

# Nested Loops
for i in range(1, 10):
    for j in range(1, 10):
        k = i*j
        print(k, end=' | ')
    print()
