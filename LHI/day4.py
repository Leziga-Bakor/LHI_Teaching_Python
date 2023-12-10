# ''''
# if statement
# > greater than
# <
# >=
# <=
# !=
# '''
# num = 10

# if num > 100: # false or true
#     print()

# #############################################################

# if num > 100: # false or true
#     print('Yes')
# else:
#     print('No')

# ############################################################
# score = eval(input('Enter your score: '))

# if score >= 80 : 
#     print('Your grade is A')
# elif score >= 60 and score < 80:
#     print('Your grade is B')
# elif score >= 50 and score < 60:
#     print('Your grade is C')
# elif score >= 40 and score < 50:
#     print('Your grade is D')
# elif score >= 30 and score < 40:
#     print('Your grade is E')
# elif score < 30:
#     print('Your grade is F')

#
# #
# # #    
'''
1. Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.

'''

length = eval(input('Enter lenght in cm: '))

if length < 0:
    print('You entered an invalid number')
else: 
    inch = length/2.54
    print('{} cm is equal to {} inches'.format(length*2, inch))

    print(f'{length*2} cm is equal to {inch} inches')