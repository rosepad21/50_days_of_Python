# Day 6: User Name Generator
def user_name():
    inp = input('Enter an email: ') # we ask the user for a mail
    if inp.find('@') == -1:
        return 'Not a valid email'
    else:
        return inp[:inp.find('@')] # we return the username

# Extra Challenge: Zero both ends
def zeroed(li):
    if len(li) == 0:
        return -1
    # given a list of numbers, we change the first and the last numbers to zero
    li[0] = 0
    li[-1] = 0
    return li
