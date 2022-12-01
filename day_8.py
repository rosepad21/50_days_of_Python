def odd_even(li):
    if len(li) == 0:
        return 0
    sorted_list = sorted(li, reverse=True)
    for i in range(len(sorted_list)):
        if sorted_list[i] % 2 == 0 or sorted_list[i] == 0:
            for j in range(1, len(sorted_list)):
                if sorted_list[-j] % 2 != 0 or sorted_list[-j] == 1:
                    return sorted_list[i] - sorted_list[-j]
                else:
                    continue
        else:
            continue

print(odd_even([4,7,3,9,10,4]))