# Day 12: Count the Dots
def count_dots(strs):
    return list(strs).count('.')

print(count_dots('h.e.l.p'))

# Extra Challenge: Your age in minutes
def age_in_minutes():
    while True:
        inp = input('Enter your year of birth: ')
        if len(inp) > 4:
            print('Input invalid. Please input a valid year of birth.')
            continue
        else:
            break
    
    leap_years = (2022-int(inp)) // 4
    return 'You are ' + str(((2022-int(inp)-leap_years) * (60*24*365) + (leap_years * 60 * 24 * 366))) + ' minutes old'
