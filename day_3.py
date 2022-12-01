# Day 3: Register Check
def register_check(di):
    count = 0
    for value in di.values():
        if value == 'yes': # checking students that are in school
            count += 1
    return count # returning the sum of students that are in school

# Extra Challenge: Lowercase Names
def lower_names(names):
    lower = []
    for i in names:
        if i.islower():
            lower.append(i) # creating a list of all names in the list that are lowercase
        else:
            continue
    return tuple(lower) # returning it as a tuple
