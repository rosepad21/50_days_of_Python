# Division and Square root
import math

def divide_or_square(n):
    if n % 5 == 0:
        return round(math.sqrt(n), 2)
    else:
        return n % 5


#print(divide_or_square(9))

def longest_value(di):
    return max(di.values(), key=len)

print(longest_value({'fruit': 'apple', 'color':'green'}))

