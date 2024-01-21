'''
Chapter 7
11. Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

'''

# l_zero = []

# for i in range(11):
#     l_zero.append(1)
#     z = [0 for j in range(i)]
#     l_zero.extend(z)
# l_zero.append(1)

# print(l_zero)


'''
While Loops

Infinite loops 

The break statement 
The else statement
'''

# for 
# while condition

# i = 0
# while i<=10:
#     print(i,'yes')
#     i += 1

# for i in range(11):
#     print(i,'yes')

# a='hhhhhhhhhhhhhhhhhhh'
# for i in a:
#     print(i,'yes')

# n = eval(input('Enter a positive number and negative number to quit: '))
# while True:
#     if n<0:
#         break
#     print(n)
#     n = eval(input('Enter a number and negative number to quit: '))

# break statement
n = 15
# for i in range(2,n):
#     print(i)
#     if n%i == 0:
#         print('not prime')
#         break
i=2
while i<n:
    print(i)
    if n%i == 0:
        print('not prime')
        break
    i+=1
else: 
    print('prime')

if True:
    pass
else:
    pass