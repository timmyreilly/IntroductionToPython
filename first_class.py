class Person:
    '''This Class Represents a person object'''

    def __init__(self, first_name, surname, tel):
        self.first_name = first_name
        self.surname = surname 
        self.tel = tel 

    def full_name(self):
        return self.first_name + " " + self.surname


