# Day 2: Strings to Integers
def convert_add(strs):
    if len(strs) == 0:
        return 0
    count = 0
    for i in strs:
        count += int(i) # we convert the numbers in the list into integers and we sum them
    return count

# Extra challenge: Duplicate names
def check_duplicates(li):
    dup = set() # initiating a set for duplicate values, so that they get stored only once
    for i in li:
        if li.count(i) > 1: # if the list has duplicates we add them to the set
            dup.add(i)
        else:
            continue
    if len(dup) == 0:
        return "No duplicates" 
    else:
        return dup
