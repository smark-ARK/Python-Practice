import random
import string
l = ['sj', 'ark', 'mug']
p = string.punctuation
n = random.random(range(0, 100))

eknaam = random.choice(l)+random.choice(p)
print(eknaam)
