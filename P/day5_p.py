# Counting

# count number divisible by 7 from 1 to 1000
# a = 1
# count = 0
# for i in range(1,1001):
#     if i%7 == 0:
#         count = count + 1 
#         # count += 1
# print(f'Total numbers divisble by 7 is {count}') # f string
# print('{} Total numbers divisble by 7 is {}'.format(count,a))

# Summing
# sum number divisible by 7 from 1 to 1000

sum_7 = 0

for i in range(1,1001):
    if i%7 == 0:
        sum_7 = sum_7 + i
print(f'Sum of numbers divisble by 7 is {sum_7}')

# LEGB -> Local, Enclosed, Global, Builtin

# swapping
x = 3
y = 7

temp = x  # 3
x = y     # 7
y = temp  # 3

x,y = y,x

# flag variables

num = eval(input('Enter number to check if prime: '))
flag = True # 
for i in range(2,num):
    if num%i == 0:
        flag = False

if flag == False: 
    print('Number not prime')
else:
    print('Prime Number')

# max and min

# 2,10,3,78,9
'''
max = eval(input('Enter number'))
for i in range(4):
    n = eval(input('Enter number'))
    if n > max: 
        max = n
print(f'The max is {max}')
'''
# comments

'''
What is a good code?
1. Readable
2. Scaleable

'''

# simple debugging
print