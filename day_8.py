# Day 8: Odd and Even
def odd_even(li):
    if len(li) == 0:
        return 0
    sorted_list = sorted(li, reverse=True)
    # we sorted the list so that the highest numbers appear first
    for i in range(len(sorted_list)):
        if sorted_list[i] % 2 == 0 or sorted_list[i] == 0:
            # if the number is even we check for an odd number at the end of the list
            for j in range(1, len(sorted_list)):
                if sorted_list[-j] % 2 != 0 or sorted_list[-j] == 1:
                    return sorted_list[i] - sorted_list[-j] # and we return the subtraction
                else:
                    continue
        else:
            continue
