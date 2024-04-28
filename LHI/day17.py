'''
OOP
'''

class Person:

    current_year = 2024

    def __init__(self, fname, lname, year, location):
        self.firstName = fname
        self.lastName = lname
        self.yearOfBirth = year
        self.location = location

    def age(self):
        return Person.current_year - self.yearOfBirth
    
    def fullname(self):
        return f'{self.firstName} {self.lastName}'
    
    def travel(self, loc):
        self.location = loc

    @classmethod
    def change_year(cls, yr):
        Person.change_year = yr

    @classmethod
    def from_string(cls,details_str):
        fname, sname, year, location = details_str.split('-')
        return Person(fname, sname, year, location)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Employees(Person):
    
    num_employees = 0
    pay_raise = 1.05
    company_name = 'LHI'

    def __init__(self, fname, lname, year, location, pay):
        super().__init__( fname, lname, year, location)
        self.pay = pay
        self.email = f"{fname}.{lname}@company.com"
        Employees.num_employees += 1
 
    def apply_raise(self):
        self.pay = self.pay * self.pay_raise


class Manager(Employees):
    pay_raise = 1.07

    def __init__(self, fname, lname, pay):
        self.firstName = fname
        self.lastName = lname
        self.pay = pay
        
    def fullname(self):
        return f'Manager: {self.firstName} {self.lastName}'
    
    # def __repr__(self):
    #     return f'Manager: {self.firstName} {self.lastName}'
    
    def __str__(self):
        """
        
        
        """
        return f'Manager str method: {self.firstName} {self.lastName}'
    
    def __add__(self, other):
        return self.pay + other.pay

'''
Maggic Methods

__methodname__ >>>> Dunder methods

__add__

__str__

__repr__

__gt__

'''

'''
Class Inheritance
'''

emp_1 = Manager('Mickel', 'Obi', 50000)
emp_2 = Manager('Harry', 'Potter', 120000)
print(emp_1)

# print(emp_1 > emp_2)

# str.__add__('a','b')  # 'ab'
# int.__add__(1,2)  # 3

print(help(Manager))