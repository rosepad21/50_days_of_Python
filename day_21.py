# Day 21: List of Tuples
def make_tuples(li_1: list, li_2: list):
    if not len(li_1) == len(li_2):
        return "Lists are not equal"
    li_3 = []
    for i in range(len(li_1)):
        li_3.append((li_1[i], li_2[i]))
    return li_3

# Extra Challenge: Even Number or Average

def even_or_average():
    inp = input('Insert five numbers: ')
    numbers = map(int, inp.split())
    numbers = sorted(numbers, reverse=True)
    for i in numbers:
        if i % 2 == 0:
            return i
    return sum(numbers) / 5
