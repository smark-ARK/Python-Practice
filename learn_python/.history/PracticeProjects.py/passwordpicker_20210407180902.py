import random
import string

adj = ['good', 'bad', 'black', 'white', 'lovely',
       'awful', 'caring', 'daring', 'ruthless', 'lazy']
noun = ['Sumeria', 'ayan', 'owais', 'riyan', 'Alisha',
        'Sultana', 'Aapi', 'jaan', 'laddu', 'pagal']
print('Welcome to the password picker :-)')
adj = random.choice(adj)
noun = random.choice(noun)
number = random.randrange(0, 1000)
spl_ch = random.choice(string.punctuation)
