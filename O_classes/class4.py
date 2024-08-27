'''
Control Flow in python
if statements
'''
num = 10

if True:
    pass
else:
    pass

# continue


'''
70 = A
60 - 69 = B
50 - 59 = C
40 - 59 = D
30 - 39 = E
< 30    = F

'''


score = 80

# if score >= 70:
#     grade = 'A'
# if score >= 60 and score < 70:
#     grade = 'B'
# if score >= 50 and score < 60:
#     grade = 'C'
# if score >= 40 and score < 50:
#     grade = 'D'
# if score >= 30 and score < 40:
#     grade = 'E'
# if score < 30:
#     grade = 'F'



if score >= 70:
    # grade = 'A'
    print('A')
elif score >= 60 and score < 70:
    # grade = 'B'
    print('B')
elif score >= 50 and score < 160:
    # grade = 'C'
    print('C')
elif score >= 40 and score < 50:
    # grade = 'D'
    print('D')
elif score >= 30 and score < 40:
    # grade = 'E'
    print('E')
else:
    # grade = 'F'
    print('F')

# print(grade)