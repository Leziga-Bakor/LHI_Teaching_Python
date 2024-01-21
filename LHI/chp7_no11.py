'''
Chapter 7
11. Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

'''

l_zero = []

for i in range(11):
    l_zero.append(1)
    z = [0 for j in range(i)]
    l_zero.extend(z)
l_zero.append(1)

print(l_zero)