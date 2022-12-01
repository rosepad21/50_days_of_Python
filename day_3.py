def register_check(di):
    count = 0
    for value in di.values():
        if value == 'yes':
            count += 1
    return count

print(register_check({'Michael':'yes','John': 'no', 
 'Peter':'yes', 'Mary': 'yes'}))




def lower_names(names):
    lower = []
    for i in names:
        if i.islower():
            lower.append(i)
        else:
            continue
    return tuple(lower)

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(lower_names(names))