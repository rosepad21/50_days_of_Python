# Day 11: Are they equal?

def equal_string(str1, str2):
    if len(str1) == len(str2): # checking if lengths are equal
        if set(str1) == set(str2): # checking if characters are the same
            return True
        else:
            return False
    else:
        return False


# Extra Challenge: Swap Values
def swap_values(li):
    if len(li) == 0:
        print('The list is empty')
    first = li[0]
    last = li[-1]
    li[0] = last
    li[-1] = first
    return li
