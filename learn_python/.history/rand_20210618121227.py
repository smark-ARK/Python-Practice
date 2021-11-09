import random
import string
ls = "sj ark mug"
l = ls.split()
p = string.punctuation
n = random.choice(range(0, 100))
q = ['Nalla', 'genius', 'bot']

eknaam = random.choice(l)+random.choice(p)+str(n)+random.choice(q)
print(eknaam)
