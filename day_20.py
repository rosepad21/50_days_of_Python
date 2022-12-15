# Day 20: Capitalize First Letter
def capitalize(strs):
    capitalized_strs = [x.capitalize() for x in strs.split()]
    return ' '.join(capitalized_strs)

# Extra Challenge: Reversed List

def reverse_list(strs):
    return [x[::-1] for x in strs.split() if not x.islower()]
