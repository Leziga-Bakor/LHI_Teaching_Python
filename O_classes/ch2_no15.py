
h = eval(input('Please supply height for the A: '))

'''

    *       ' 4 spaces 
   *s*        3 spaces 
  *sss*       2 spaces 
 *sssss*      1 space
*sssssss*     0

h//2

4 = 2.5
 
'''

print(' '*(h-1),'*')

for i in range(1,h):
    if i == h//2:
        print(' '*(h-i), '*','*'*(2*i-1), '*', sep='')
    else:
        print(' '*(h-i), '*',' '*(2*i-1), '*', sep='')