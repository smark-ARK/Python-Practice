def sum_digits(num):
    assert type(num) is int and num > 0, "number must be a possitive integer!"
    if num<10:
        return num
    else:
        return num%10 + sum_digits(num//10)

print(sum_digits(122667))