import random

# Day 17: User Name Generator
def user_name():
    inp = input('Enter your name: ')
    generated_number = random.randint(0, 9)
    return inp[::-1] + str(generated_number)

# Extra Challenge: Sort by Name

def sort_length(li):
    return sorted(li, key=len)
