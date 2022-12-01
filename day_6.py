def user_name():
    inp = input('Enter an email: ')
    return inp[:inp.find('@')]

print(user_name())

def zeroed(li):
    li[0] = 0
    li[-1] = 0
    return li

print(zeroed([2,3,4,5,1]))