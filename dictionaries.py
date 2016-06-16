phone_numbers = {'Spam': '555 1234', 'Eggs': '555 4444', 'Kramer':'555 1177'}

print phone_numbers 

print phone_numbers['Spam']

phone_numbers['Bob'] = '555 5555'

print phone_numbers

phone_numbers.pop('Bob')

print phone_numbers

for name in phone_numbers:
    print name