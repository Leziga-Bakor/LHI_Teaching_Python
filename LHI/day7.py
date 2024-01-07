'''
Python LIST

'''

# creating list

l = ['a','b','c']

s = list('iterable')
# print(s)


# - empty list
e =[] # false, 0, ''

# - list data types
name = 'james'
d = ['a', 2, 3.2, ['a',['i','t']], name]


# similarities to String
# - joining(concatenation) and repetition
l1 = ['apple','banana', 'cake']
l2 = [1,2,3]
l3 = l1 *4

# print(l3)

# - Iterable

# for item in l1:
#     print(item)

# - in operator
# if item in l1:
#     print('do something')

cl = 'CSS'

if cl in ['python']:
    pass

# - indexing
la = ['apple','banana', 'cake']
#        0       1         2

# print(la[2])

# - slicing 
lp = la[1:2]


# Mutable

la = ['apple','banana', 'cake']

la[0] = 'boy'

print(la)

st2='John'

# print(st2[0])
# st2[0] = 'h'

# g =  st2

# st2 = st2[0:2] + 'p' + st2[-1] # jopn

# print(st2)
# print(g)

# st2 =st2.replace('h','p')


# list methods (replace, sort, append)

la = ['Z','apple','banana', 'cake']

# la.append([1,2,3])
# la.extend([1,2,3])

la.insert('orange')

la.sort()
la2 = sorted(la)

print(la)