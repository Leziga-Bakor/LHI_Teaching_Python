# # if statement

# num = 10

# if num == 100:
#     print('Number is greater than 100')
# else:
#     print('number is less than 100')

# if num < 10:
#     pass
# elif num < 20:
#     pass
# else:
#     pass

# '''
# 80 - 100 -> A
# 60 - 79 -> B
# 50 - 59 -> C
# 40 - 49 -> D
# 30 - 39 -> E
# 0 - 29 -> F

# '''
# grd = eval(input("Please enter your score: "))

# if grd >= 80 and grd <= 100:
#     print('Your grade is A')
# elif grd >= 60 and grd < 80:
#     print('Your grade is B')
# elif grd >= 50 and grd < 60:
#     print('Your grade is C')
# elif grd >= 40 and grd < 50:
#     print('Your grade is D')
# elif grd >= 30 and grd < 40:
#     print('Your grade is E')
# else:
#     print('Your grade is F')
    



num = eval(input("Please enter the number to be factorized: "))
fact = 1
for i in range(1,num+1): # 0,1,2,...(num -1)
    fact = fact * i
print('The factorial of {} is {}'.format(num,fact))
print(f'The factorial of {num} is {fact}')
'''
1 * 1 = 1
1 * 2 = 2 
2 * 3 = 6
6 * 4 = 24
'''