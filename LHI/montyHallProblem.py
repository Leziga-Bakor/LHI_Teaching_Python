from random import shuffle, choice

ch = ['g1','p','g2'] # 1 = prize, 2 and 3 are goat
ch = shuffle(ch)  # shuffle the list [g,p,g]

correct_ans = ch.index('p')  # gets the index of p from shuffled list
fg = ch.index('g1')
sg = ch.index('g2')

user = eval(input('Enter a choice from 1 to 3: ')) # 0, 1, 2
user -= 1
flag = False

if user == correct_ans:
    rm = choice([sg,fg])
    
    if rm == sg: 
        other = fg # 2
    else: 
        other = sg 

    q = input('Do you wish to change your choice? ')
    if q.lower() == 'yes':
        user = other

    if user == correct_ans:
        flag = True

elif user == sg:
    rm = fg
    other = correct_ans

    q = input('Do you wish to change your choice? ')
    if q.lower() == 'yes':
        user = correct_ans

    if user == correct_ans:
        flag = True

elif user == fg:
    rm = sg
    other = correct_ans

    q = input('Do you wish to change your choice? ')

    if q.lower() == 'yes':
        user = correct_ans

    if user == correct_ans:
        flag = True

if flag:
    print('Got the answer')