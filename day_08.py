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

# Extra Challenge: List of Prime Numbers

def isprime(n): # let's define a function to determine whether a number is prime
    for num in range(2, int(n**0.5)+1):
        if n%num == 0:
            return False
    return True

def prime_number(n):
    prime_numbers = []
    for i in range(2, n):
        if isprime(i):
            prime_numbers.append(i)
        else:
            continue
    return prime_numbers
