'''

'''

# str, int, float, and list 

s = '12345'
s1 = 'text'

i=int(s) # 12345

s = str(i) # '12345'

l=list(s)

print(float(s))

num=11.23
inum = int(num) # 11

decimal_p = num - inum # 0.23

# BOOLEAN  True or False

b = bool(s)  

flag = False

if flag == False: # True
    pass

if not flag: 
    pass

a = 3
p = a > 10

# shortcuts

a = a + 1
a +=1 

b = b - 1
b -= 1

b = b * a
b *= a


a = 1
b = 1
c = 1

a=b=c=1

l = [8,9,10]
a = l[0] # 8
b = l[1] # 9
c = l[2] # 10

a,b,c = l

x = 1
y = 9

temp = x
x = y 
y = temp

x, y = y ,x

# short circuiting

a = 17

if a < 10 and not z:
    pass

b =  b%a
b %= a

b = 7
a = 2 

print(b%a)
b %= a
print(b)

# Continuation
# PEP8

if a == b and a > 10 and a <100 and \
    a >= b:
    pass

for i in [1,1,1,7,2,3,4,5,6,8,
          7,8]:
    pass

# string formatting

p = 22/7

print('The answer is {:.2f}'.format(p))



'''


'''