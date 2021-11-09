import random
import string
l = ['sj', 'ark', 'mug']
p = string.punctuation
n = random.choice(range(0, 100))
q = ['Nalla', 'genius', 'bot']

eknaam = random.choice(l)+random.choice(p)+str(n)
print(eknaam)
