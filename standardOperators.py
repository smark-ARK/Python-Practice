"""
a = 10
b = 9
d = 10

# Arithmetic Operators
# Addition(+)
c = a+b
print('Addition of a and b:', c)
# Subtraction(-)
c = a-b
print('Subtraction of a and b:', c)

# Multiplication(*)
c = a*b
print('Multiplication of a and b:', c)

# Division(/)
c = a/b
print('Divivision of a and b:', c)

# Modular Division(%)
c = a % b
print('Modulus of a and b:', c)

# Exponent(**)
c = a**b
print('Exponent of a and b:', c)

# Floor Division(//)
c = a//b
print('Floor Division of a and b:', c)


# Comparison(Relational) Operators
# checking equality(==)
if(a == d):
    print('a is equal to b')
else:
    print('not equal')
# inequality (!=)
if(a != b):
    print('a is not equal to b')
else:
    print('equal')
# Greater than(>)
if(a > b):
    print('a is greater')
else:
    print(' a is no greater')
# Less than(<)
if(a < d):
    print('a is smaller')
else:
    print(' a is not smaller')
# Greater or qual(>=)
if(a >= b):
    print('a is greater or equal')
else:
    print('a is not greater or equal')
# Lesser or Equal(<=)
if(a <= b):
    print('a is lesser or equal')
else:
    print('a is not lesser or equal')


# Assignment Operators
# Assign(=)
x = 5
y = x
print('values of x and y', x, y)
# Add and assign(+=)
x += y  # x=x+y
print('value of x after x+=y', x)
# Subtract and Assign (-=)
x -= y  # x=x-y
print('value of x after x-=y:', x)
# multipy and assign(*=)
x *= y  # x=x*y
print('value of x after x*=y:', x)
# Divide and assign(/=)
x /= y  # x=x/y
print('value of x after x/=y:', x)
# Exponent and assign(**=)
x **= y  # x=x**y
print('value of x after x**=y:', x)
# Floor division and assign(//=)
x //= y  # x=x//y
print('value of x after x//=y:', x)
# Modulus and Assgn(%=)
x %= y  # x=x%y
print(x)



# Logical Operators
a = True
b = False
# Logical AND(and)
if(a and b):
    print("and: condition satisfied")
else:
    print("and:  not satisfied")
# Logical OR(or)
if(a or b):
    print("or: condition satisfied")
else:
    print("or: not satisfied")
# Logical NOT(not)
if(not(a and b)):
    print("Not: condition satisfied")
else:
    print("Not: not satisfied")

# Membership opertors
l = [10, 20, 14, 50, 'ARK', 'SM']
a = 10
b = 200/10
c = 'ARK'
d = 'Ayan'
# in
if(c in l):
    print('in:present')
else:
    print('in:not present')
# not in
if(c not in l):
    print('not in:not present')
else:
    print('not in:present')


# Identity opertors
a = [10]
b = [10]
print(id(a), id(b))

# is
c = bool(a is b)
print(c)
# is not
c = bool(a is not b)
print(c)

ad = hex(id(a))
print(ad)
"""

# Bitwise Operators
a = 25
b = 30  # 11111
bina = bin(a)
binb = bin(b)
print("bin of a :", bina)
print("bin of b :", binb)

# & (bitwise AND)
aandb = a & b
print("result of and:", aandb)
print("bin value:", bin(aandb))
# | (bitwise OR)
aorb = a | b
print("result of OR:", aorb)
print("bin value:", bin(aorb))
# ~ (bitwise NOT)
anotb = ~a

""" ~a = ~11001
= -(11001 + 1)
= -(11010)
= -26 (Decimal)
 """
print("result of not:", anotb)
print("bin value:", bin(anotb))
# ^ (bitwise XOR)
axorb = a ^ b
print("result of xor:", axorb)
print("bin value:", bin(axorb))
# << (bitwise left shift)
ls = a << 2
print("result of lshift:", ls)
print("bin value:", bin(ls))
# >> (bitwise right shift)
rs = a >> 2
print("result of rshift:", rs)
print("bin value:", bin(rs))
