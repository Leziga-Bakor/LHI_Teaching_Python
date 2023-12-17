import math


number = float(input('Enter a naumber'))
print(number)

# Counting

count = 0
for i in range(1,1001):
    if i%7 == 0:
        count = count + 1
        # count += 1
print(count)

'''
count = count - 1  count -= 1

1,2,3,4,5

s = 0 
for loop    
    s = 0 + 1
    s = 1 + 2 =3
    s = 3 + 3 = 6
    s = 6 + 4 = 10
    s = 10 + 5 = 15

'''

# summing

sum_odd = 0
for i in range(1,101):
    if i%2 != 0:
        sum_odd = sum_odd + i

# swapping
x = 3
y = 7

temp = x  # temp = 3
x = y     # x = 7
y = temp  # y = 3

x,y = y,x

# flag variables

flag = False

for i in range(10):
    if i%7 == 0:
        flag = True

# if flag == True:

if flag:
    pass
else:
    pass

num = eval(input('Enter number: '))
flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1

if flag == 1:
    print('Not prime')
else:
    print('Prime')

# max and min

max = eval(input('Enter number: ')) # make the first input to be the max
for _ in range(4):
    num = eval(input('Enter number: '))
    print(num)
    if num > max:
        max = num
print(f'The maximum number is {max}')

_max = 0
max2 = 1
Max = 1

# comments

'''
What makes a code good?
1. Readable
2. Scaleable

'''
# simple debugging
print ()

math.sqrt(4)

s=2351
s=str(s) #  = '2351'
int(s[1:2]) # 35

mid = int(str(s)[1:2])