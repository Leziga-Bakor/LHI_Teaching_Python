""" Functions in python """

def my_function(name):
    return f'Hello, {name} How are you?'

# print(my_function('Faith'))
# print(my_function('James'))
# print(my_function('Paul'))

def addnum(a,b=10):
    num_sum = a + b
    return num_sum

total = addnum(3)
total2 = addnum(10)
total3 = addnum(30,40)

print(total, total2, total3, sep='---')

print()