import emoji

# Day 13: Pay your tax
def your_vat():
    while True:
        price = input('Enter the item price: ')
        vat = input('Enter VAT: ').strip('%')
        try:
            price = float(price)
            vat = float(vat)
            break
        except ValueError:
            print('The input is not a valid number. Please insert another number')
    
    return price + (price * vat / 100)
 
# Extra Challenge: Pyramid of Snakes
def python_snakes(n):
    strs = emoji.emojize(':snake:')

    for i in range(n):
        space = ' ' * (n - i)
        print((space + (strs*i)).center(n))
