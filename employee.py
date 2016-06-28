from first_class import Person

# Demonstrating Inheritance 
class Employee(Person):

    def __init__(self, first_name, surname, tel, salary):
        Person.__init__(self, first_name, surname, tel)
        self.salary = salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount 
