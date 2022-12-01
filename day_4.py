def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


print(only_floats(12.1, 23.3))


def word_index(words):
    length = []
    for i in words:
        length.append(len(i))
    if length.count(max(length)) > 1:
        return 0
    else:
        return length.index(max(length))

print(word_index(['Hate', 'love']))