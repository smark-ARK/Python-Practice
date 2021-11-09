# if
var = 400
if var > 101:
    print('greater')

# if-else
if var > 100:
    print('greater')
else:
    print('lesser')

# if-elif-else
if var > 100:
    print('greater')
elif var == 100:
    print('equal')
else:
    print('lesser')
# nested if-else

if var > 100:
    print('greater than 100')
    if var < 500:
        print("Less than 500")
    else:
        print('Greater than 500')
else:
    print('lesser than 100')
