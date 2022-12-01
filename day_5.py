# Day 5: My Discount
def my_discount():
    inp1 = float(input('Enter the price: ')) # asking the user to input the price
    inp2 = float(input('Enter the discount: ').strip('%')) # and the discount. we remove the %
    return inp1 - (inp1 * inp2 / 100) # calculating discounted price

# Extra challenge: Tuple of Student Sex
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
    return new # returning a list of two tuple containing the number of male and female students
