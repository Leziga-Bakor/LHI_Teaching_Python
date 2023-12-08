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



h = eval(input(' what is the height of A? ' ))
print(' '*h,'*', sep ='')

for i in range(1,h):
    if i == h//2:
        print(' '*(h-i),'*','*'*(2*i-1), '*',sep='')
    else:
        print(' '*(h-i),'*',' '*(2*i-1), '*',sep='')


# print('    ','*')
# print('   ','* *')
# print('  ','*****')
# print(' ','*     *')
# print('','*       *')

'''
Chapter 5, Number 4

Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000.

-2-4-6-8-10....-2000
1+3+5+7+9 .... +1999

'''
sum_even = 0
for i in range(2,2001,2):
    sum_even -= i
    # sum_even = sum_even - i

sum_odd = 0
for j in range(1,2001,2):
    sum_odd += j

overall_sum = sum_odd + sum_even

print(sum_even)
print(sum_odd)
print(overall_sum)
    