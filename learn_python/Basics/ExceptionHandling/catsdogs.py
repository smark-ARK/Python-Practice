def access(c, d):
    for i in c:
        print(i)
    for j in d:
        print(j)


try:
    with open("cats.txt") as cat:
        cats = cat.readlines()
    with open("dogs.txt") as dog:
        dogs = dog.readlines()
except FileNotFoundError:
    pass
else:
    access(cats, dogs)

