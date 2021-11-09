import random


#The choice() method returns a random item from a list, tuple, or string.
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1,
2, 3, 5, 9]))

""" The randrange() method returns a randomly selected element from range(start, stop,
step). """
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
print ("randrange(100) : ", random.randrange(100))

# The random() method returns a random floating point number in the range [0.0, 1.0].
# First random number
print ("random() : ", random.random())
# Second random number
print ("random() : ", random.random())

#Value of a
random.seed()
print ("random number with default seed", random.random())
random.seed(10)
print ("random number with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())