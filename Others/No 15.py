# h = eval(input(' what is the height ' ))
# for i in range(h):
#     print(' '*(h-i),'*'*((2*i)+1),sep='')
# for i in range(h-2, -1, -1):
#     print(' '*(h-i),'*'*((2*i)+1),sep='')

# h = eval(input(' what is the height ' ))
# for i in range(h):
#     print(' '*(h-i) + '*'*(h*2-1-2*(h-i)))


#  for i in range(size):
#         left_space = abs(size - i)
#         right_space = size * 2 - 1 - 2 * left_space
#         print(" " * left_space + "*" * right_space)



# h = eval(input(' what is the height of A? ' ))
# print(' '*h,'*', sep ='')

# for i in range(1,h):
#     if i == h//2:
#         print(' '*(h-i),'*','*'*(2*i-1), '*',sep='')
#     else:
#         print(' '*(h-i),'*',' '*(2*i-1), '*',sep='')



# '''
# Chapter 5, Number 4

# Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000.

# -2-4-6-8-10....-2000
# 1+3+5+7+9 .... +1999

# '''
# sum_even = 0
# for i in range(2,2001,2):
#     sum_even -= i
#     # sum_even = sum_even - i

# sum_odd = 0
# for j in range(1,2001,2):
#     sum_odd += j

# overall_sum = sum_odd + sum_even

# print(sum_even)
# print(sum_odd)
# print(overall_sum)

# # Second Solution 
# sum_even2 = 0
# sum_odd2  = 0
# for i in range(1,2001):
#     if i%2 == 0:
#         sum_even2 += i
#     else:
#         sum_odd2 += i
# total_sum = sum_odd2 - sum_even2
# print(total_sum)


##################################################################

'''

Chapter 5 Number 7.

An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.

'''
import math
flag = True
num = eval(input('Enter the number: '))
for i in range(2,num):
    if num%i==0:
        sqr = math.sqrt(i)
        if float(sqr).is_integer():
            print(i)
            flag = False
            break
# if flag:
if flag == True: 
    print(f'Number {num} is squarefree')
else:
    print(f'Number {num} is not squarefree')