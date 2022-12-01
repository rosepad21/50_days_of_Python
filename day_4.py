# Day 4: Only Floats
def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2 # returning 2 if both arguments are floats
    elif isinstance(a, float) or isinstance(b, float):
        return 1 # returning 1 if only one argument is a float
    else:
        return 0 # returning 0 if none are floats

# Extra challenge: Index of the Longest Word
def word_index(words):
    length = []
    for i in words:
        length.append(len(i)) # appending lengths of all the words in the list
    if length.count(max(length)) > 1:
        return 0
    else:
        return length.index(max(length)) # returning the index of the longest word
