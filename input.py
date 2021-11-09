'''
Traditionally:
input(): quoted data as string otherwise number
raw_input(): always treats as string
in python3:
raw_input deprecated
input(): always treats data as string
'''
a = input('Ishaaq is a mugloo Enter his age: ')
print(type(a))
# int()
a = int(a)
print(type(a))
# float()
a = float(a)
print(type(a))
# str()
a = str(a)
print(type(a))
# complex()
#a = complex(a)
# list()
a = list(a)
print(type(a))
# tuple()
a = tuple(a)
print(type(a))
a = ((2, 'key1'), (3, 'key2'))
# dict()
a = dict(a)
print(type(a))
