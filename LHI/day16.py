'''
Object Oriented Programming OOP

'''

class Employees:
    
    num_employees = 0
    pay_raise = 1.05
    company_name = 'LHI'

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employees.num_employees += 1

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    def raise_pay(self):
        self.pay = self.pay * self.pay_raise


print(Employees.num_employees)

emp_1 = Employees("John","Greg",100000)
emp_2 = Employees("Anthony","Amadi",50000)

print(Employees.num_employees)

print(emp_1.pay)
emp_1.pay_raise = 1.12
emp_1.raise_pay()
print(emp_1.pay)

print(emp_2.pay)
emp_2.raise_pay()
print(emp_2.pay)


print(emp_1.company_name)
print(emp_1.pay_raise)
print(emp_2.pay_raise)

'''
LEBG

'''

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employees.__dict__)