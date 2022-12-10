# Day 16: Sum the List

def sum_list(li):
    if len(li) == 0:
        return 0
    elements_sum = 0
    for i in li:
        elements_sum += sum(i)
    return elements_sum

# Extra Challenge: Unpack a Nest

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
def unpack_a_nest(li):
    return [li[0][1], li[0][3], li[1][2]]
  
result = unpack_a_nest(nested_list)
