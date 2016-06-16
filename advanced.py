from first_class import Person
from datetime import datetime

x = 12345.2345

print "x={:.2f}".format(x)

print "{:.3f}".format(x)

# Datetime Formatting 
d = datetime.now() 
print "{:%Y-%m-%d %H:%M:%S}".format(d) 


print ''

def calculate_temperature(kelvin):
    celsius = kelvin - 273.0
    fahrenheit = celsius * 9 / 5 + 32 
    return celsius, fahrenheit

c, f = calculate_temperature(340)

print c, f 

me = Person('Tim', 'Reilly', '503 314 3771')

fullname = me.full_name()
print fullname 

from employee import Employee

tim_employed = Employee('Tim', 'Reilly', '503 314 3771', 100000000)

print tim_employed.salary

tim_employed.give_raise(999)

print tim_employed.salary

print tim_employed


#Files!

f = open('test.txt', 'w') # w for overwrite
f.write('This file is now at Galvanize')
f.close()

f = open('test.txt')
s = f.read()
print s 
f.close() 

print ''
# Random numbers!
# and importing 

from random import randint 
print(randint(1, 50))

import random 
print random.choice(['turtles', 'giraffe', 'crocodile', 'penguin'])

# Web Requests 
