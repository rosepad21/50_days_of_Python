# Day 7: A string range
def string_range(n): # given a number, we return a string of its range separated by dots
    strs = ''
    for i in range(n):
        strs += str(i)
        strs += '.'
    return strs.rstrip('.') # since a last dot would be added after the last number, we remove it

# Extra Challenge: Dictionary of Names
def dictionary_names(li):
    di = dict()
    if len(li) == 0:
        return 'The list is empty'
    for i in li:
        if i.startswith('S'): # we have to return all the names that start with S and how many times they appear in the list
            di[i] = di.get(i, 0) + 1
    return di
