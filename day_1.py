# Day 1: Division and Square root
import math

def divide_or_square(n):
    if n % 5 == 0: # if the number is divisible by 5 we return its square root
        return round(math.sqrt(n), 2)
    else: # else we return its remainder
        return n % 5


# Extra Challenge: Longest Value
def longest_value(di):
    return max(di.values(), key=len) # finding the longest first value in a dictionary

