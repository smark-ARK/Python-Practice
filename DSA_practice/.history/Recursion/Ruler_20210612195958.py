def draw_line(tick_leangth, tick_label=''):
    line = '-'*tick_leangth
    if tick_label:
        line += ' '+tick_label
    print(line)
