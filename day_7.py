def string_range(n):
    strs = ''
    for i in range(n):
        strs += str(i)
        strs += '.'
    return strs.rstrip('.')

print(string_range(6))

def dictionary_names(li):
    di = dict()
    for i in li:
        if i.startswith('S'):
            di[i] = di.get(i, 0) + 1
    return di

print(dictionary_names(["Joseph","Nathan", "Sasha", "Kelly",
 "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]))