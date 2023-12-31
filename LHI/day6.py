''''
STRINGS
'''

st = 'string'

# Concatenation and repetition
st1 = 'My name is '
st2 = 'John'

st3 = st1 + st2
# print(st3)

st4 = st2 * 10
# print(st4)

# Interable (Indexing and in operator)
st2='John'

st2[0]
# print(st2[1])
# print(st2[2])

print(st2[1:3])   # [start,end,step]

print(st2[-2])

if 'o' in st2:
    print('yes')

if 'i' not in st2:
    print('I not in string')


vowels = 'aeiou'

l = 'z'

if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    print('it is a vowel')

if l in 'aeiou':
    print('it is a vowel')



# Slices
# Changing individual characters of a string

'''NB: Strings are immutable '''

st2='John'

st2 = st2[0:2] + 'p' + st2[-1] # jopn

print(st2)

# st2[2] = 'p'

# Looping

for item in st2:
    print(item)

for j in range(len(st2)):
    print(st2[j])


# String methods

st2 = st2.replace('p','h')

st2.upper()

print(st2)

s='1234'

# Escape characters \
s = 'i\'m here \n'
s = " He said \"I can't go \""

country = 'South Africa'
st2='John'

detail = f'My name is {st2} and I am from {country}'

detail = 'My name is {} and I am from {}'.fomat(st2,country)


''' 
syntax

'''