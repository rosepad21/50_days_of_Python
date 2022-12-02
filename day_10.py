# Day 10: Hide my Password
def hide_password():
    inp = input('Enter a password: ')
    password = '*' * len(inp)
    return f'{password} (The passowrd is {len(inp)} character(s) long).'

# Extra Challenge: A Thousand Separator
def convert_numbers(li):    
    converted = []
    for i in li:
        temp = list(str(i))
        for j in range(2, len(temp), 4):
            j += 1 # every time we add a comma, the index moves so we add 1 to the iteration variable
            temp.insert(-(j), ',')
        converted.append(''.join(temp))
    return converted
