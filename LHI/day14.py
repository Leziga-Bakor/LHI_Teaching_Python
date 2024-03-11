'''Function in Python Continued'''


def addnum(*a):
    num_sum = 0
    for num in a:
        num_sum += num
    return num_sum

total = addnum(30,40,60,70)
print(total)
# 30 + 40 + 60 + 70



def names(**b):
    print(b)   
    # print(f'first name is {a} and second name is {b}')

# t = names(t='James', b='Peter', age = 10, height = '1.75m')

# {'t': 'James', 'b': 'Peter', 'age': 10, 'height': '1.75m'}


def my_func(*args, **kwargs):
    pass


def print_box(width,height=4):
    for i in range(height):
        print('*' * width)

def print_box():
    print('*' * 19)
    print('*' * 19)
    print('*' * 19)
    print('*' * 19)

print_box()
print()
print_box()




'''
Create a 5 × 5 list of numbers. Then write a program that creates a dictionary whose keys are
the numbers and whose values are the how many times the number occurs. Then print the
three most common numbers.

from random import randint

list_num = [[1, 1, 3, 5, 3], [1, 2, 2, 5, 1], [1, 2, 2, 4, 4], [5, 2, 1, 2, 5]]

dict_count = {}

for l in list_num:
    for num in l:
        if num in dict_count:
            dict_count[num] = dict_count[num] + 1
        else:
            dict_count[num] = 1

kv = list(dict_count.items())

kv = sorted(kv, key= lambda x:x[1])

print(kv)

# [(1, 6), (3, 2), (5, 4), (2, 6), (4, 2)]

# [(3, 2), (4, 2), (5, 4), (1, 6), (2, 6)]

# print(dict_count)

# dict1 = {'name' : 2}

# print(dict1)

# dict1['name'] = dict1['name'] + 1

# print(dict1)


'''