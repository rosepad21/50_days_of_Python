# Day 18: Any Number of Arguments

def any_number(*args):
    numbers_sum = 0
    for i in args:
        numbers_sum += i
    return numbers_sum / len(args)

# Extra Challenge: Add and Reverse
def add_reverse(li_1, li_2):
    li_3 = []
    if len(li_1) == len(li_2):
        for i in range(len(li_1)):
            li_3.append(li_1[i]+li_2[i])
    else:
        return 'The list are not of equal lengths'
    return li_3[::-1]
