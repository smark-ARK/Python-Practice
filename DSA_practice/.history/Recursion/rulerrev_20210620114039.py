ml = int(input('Enter the length of major tick: '))
ni = int(input('Enter the length of ruler: '))


def line(l, label=''):
    if l > 0:
        line = '-'*l
    if label:
        line += ' '+label
    print(line)
