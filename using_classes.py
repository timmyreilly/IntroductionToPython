from first_class import Person
from employee import Employee


me = Person('Tim', 'Reilly', '503 314 3771')

fullname = me.full_name()
print fullname 

tim_employed = Employee('Tim', 'Reilly', '503 314 3771', 100000000)

print tim_employed.salary

tim_employed.give_raise(999)

print tim_employed.salary

print tim_employed