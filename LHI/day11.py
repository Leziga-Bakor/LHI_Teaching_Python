'''
Tuple
DICTIONARY - Working with key-value pairs

'''

# list mutable
# tuple immutable
l = []

t = (1,2,3,4,5,6,2)

t1 = list(t)
t1.append(7)
t = tuple(t1)

dict ={'key':'value', 0:1, 1 : 2, }


# Syntax/Declaration

empty_dict = {}

person = {
    'Name': 'John',
    'age' : 23,
    'country':'United KINGDOM',
    'points' : [2,5,6,7,8,9],
    'job' : {'company': 'FG', 'salary': 100000}
}

# print(person['job']['salary'])
# print(person.get('age'))


# Dictionary keys 

# Only immutable data types can be keys in dictionary eg. tuble, string, integer

# Setting and updating values
person['age'] = 30
person['height'] = 1.8

person.update({'weight': 80})


# Removing key-value pairs del,pop

del person['height']

a = person.pop('age')



# keys, values, items



# print(person.keys())
# print(person.values())
# print(person.items())


# looping

for key, value in person.items():
    print(key)
    print(value)

# for k in person.keys():
#     print(k)

# for x in person:
#     print(x)
#     person[x]

# copying dictionary
    
p = person.copy()