import random

def select_sex(): 
    sex = {0: 'male', 1:'female'}
    numb = random.randint(0, 1)

    return sex[numb]


print(select_sex())