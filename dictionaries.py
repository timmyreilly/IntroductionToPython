# creating 
phone_numbers = {'Spam': '555 1234', 'Eggs': '555 4444', 'Kramer':'555 1177'}

print phone_numbers 

# finding 
print phone_numbers['Spam']

# adding 
phone_numbers['Bob'] = '555 5555'

print phone_numbers

# removing 
phone_numbers.pop('Bob')

print phone_numbers

# iterating 
for name in phone_numbers:
    print name