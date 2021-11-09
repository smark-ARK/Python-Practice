import random
import string
while (True):
adj = ['good', 'bad', 'black', 'white', 'lovely',
       'awful', 'caring', 'daring', 'ruthless', 'lazy']
noun = ['Sumeria', 'ayan', 'owais', 'riyan', 'Alisha',
        'Sultana', 'Aapi', 'jaan', 'laddu', 'pagal']
print('Welcome to the password picker :-)')
adj = random.choice(adj)
noun = random.choice(noun)
number = str(random.randrange(0, 1000))
spl_ch = random.choice(string.punctuation)

password = adj+noun+number+spl_ch

print('Password:', password)

user_res = input('would u like to get a new password??Type y if so or type n:')
