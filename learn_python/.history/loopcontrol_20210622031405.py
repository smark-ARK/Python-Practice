for i in 'Hello World':
    print(i)
    if i == 'o':
        break
a = int(input('number:'))
l = [1, 2, 4, 5, 6, 9, 100]
for i in l:
    if i == a:
        print('Element found')
        break
    else:
        print('not foun')
