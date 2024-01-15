'''
More of List
'''

# List and the random module (choice(L), sample(L,n), shuffle(L))
from random import choice, sample, shuffle

l = ['Jan','Feb','Mar','Apr', 'May', 'Jun']
print(choice(l))

s = sample(l,2)

print(shuffle(l))

print(l)

#split
s = 'today is sunday'
l = s.split('is')
print(l)

l.sort()

print(l)

#join
n = ' '.join(l)
print(n)

# list comprehnsion ()

L=[]
for i in range(1,101):
    if i%2 == 0:
        L.append(i)

L = [i for i in range(1,101)]

L = [i*j for i in range(1,101) for j in range(1,3)]

L=[]
for i in range(1,101):
    for j in range(1,5): 
        L.append(i*j)

print(L)

# Two dimension list

l = [
    [1,2,3,4,5],
    [6,7,8,9,[10,21,22,23]],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

print(l[1][4][1])

n = eval(input('Enter a number? '))
for i in range(1,n+1):
    print(' '*(i-1),i)

e = input('Enter a string ')
for item in e:
    print(item*2)


split_char = 'a'
word = input("Enter a word: ")
index = word.find(split_char)
index +=1
left = word[:index]
right = word[index:]
print(left + '\n' + right)