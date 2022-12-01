def convert_add(str):
    if len(str) == 0:
        return 0
    count = 0
    for i in str:
        count += int(i)
    return count

print(convert_add(['1','3','5']))


def check_duplicates(str):
    dup = set()
    for i in str:
        if str.count(i) > 1:
            dup.add(i)
        else:
            continue
    if len(dup) == 0:
        return "No duplicates"
    else:
        return dup

print(check_duplicates(['apple', 'orange', 'banana']))