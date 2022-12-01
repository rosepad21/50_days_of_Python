def my_discount():
    inp1 = float(input('Enter the price: '))
    inp2 = float(input('Enter the discount: ').strip('%'))
    return inp1 - (inp1 * inp2 / 100)


#print(my_discount())

def tuple_student(li):
    new = []
    male_count = 0
    female_count = 0
    for i in li:
        if i.lower() == 'male':
            male_count += 1
        else:
            female_count += 1
    new.append(tuple(['male', male_count]))
    new.append(tuple(['female', female_count]))
    return new

print(tuple_student(['Male', 'Female', 'female', 'male', 'male', 'male',
 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']))