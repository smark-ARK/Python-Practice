major_leangth = int(
    input('Enter leangth of the tick per inch(as no. of hyphens): '))
num_inches = int(input('How many inches do you want to print on Ruler: '))


def draw_line(tick_leangth, tick_label=''):
    line = '-'*tick_leangth
    if tick_label:
        line += ' '+tick_label
    print(line)


def draw_interval(center_leangth):
    if center_leangth > 0:
        draw_interval(center_leangth-1)
        draw_line(center_leangth)
        draw_interval(center_leangth-1)


def draw_ruler(num_inches, major_leangth):
    draw_line(major_leangth, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_leangth-1)
        draw_line(major_leangth, str(j))


draw_ruler(major_leangth, num_inches)
