# Day 15: Same in Reverse
def same_in_reverse(strs):
    return strs == strs[::-1]

# Extra Challenge: What's my age?
def your_age():
    names_age = {'jane' : 23, 'kerry' : 45, 'tim' : 34, 'peter' : 27}
    name = (input('Enter your name: ')).lower()
    if name not in names_age.keys():
        age = int(input("I'm sorry, your name is not in our database. Please enter your age: "))
        names_age[name] = age
    
    return f'Hi, {name.capitalize()}, you are {names_age[name]} years old.'
