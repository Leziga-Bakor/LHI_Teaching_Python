'''
1 3 5 7

odd numbers

   *        space h-1, 1
  ***       space h-2, 3
 *****      space h-3, 5
*******     space h-4, 7

 *****      space h-3, 5
  ***       space h-2, 3
   *        space h-1, 1


2n-1 = 5 3 1
'''
# (start=0, stop, step=1)

h = eval(input('Please enter height: '))
for i in range(h): # 0, 1, 2, 3
    print(' '*(h-(i+1)),'*'*((2*i)+1), sep='')
for i in range(h-1,0,-1): #3, 2, 1
    print(' '*(h-i),'*'*((2*i)-1), sep='')