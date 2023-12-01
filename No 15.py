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
print(' '*h,'*')
for i in range(h):
    print(' '*(h-i),'*',' *'*i,sep='')


print('    ','*')
print('   ','* *')
print('  ','*****')
print(' ','*     *')
print('','*       *')