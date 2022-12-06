# Day 14: Flatten the List

def flat_list(li):
    if len(li) == 0:
        return 'List is empty'
    return li[0]

# Extra Challenge: Teacher's Salary

def your_salary():
    name = input('Enter your name: ')
    periods = int(input('Enter the number of periods taught in a month: '))
    rate = int(input('Enter the rate per period: '))
    overtime_rate = rate + 5
    if periods > 100:
        gross_salary = (periods - 100)*overtime_rate + 100*rate
    else:
        gross_salary = periods * rate
    output = print(f'Teacher: {name},\nPeriods: {periods},\nGross Salary: {gross_salary}')
    return output
