# Day 9: Biggest Odd Number
def biggest_odd(strs):
    numbers = [int(x) for x in strs] # using list comprehension
    return max(numbers)
 
# Extra Challenge: Zeros to the end
def zeros_last(li):
    if not 0 in li:
        return sorted(li) # if there are no zeros, we return the sorted list
    else:
        for i in li:
            if i == 0: # for every zero, we remove it and append it at the end of the list
                li.remove(0)
                li.append(0)
    return li
