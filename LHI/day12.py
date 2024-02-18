# # File objects in python

# f = open('our_file.txt', 'r')
# f1 = open('new.txt', 'w')
# f1.write('This is the second file\n')

# for line in f:
#     f1.write(line)

# print(file = f1)
# print('I have finished copying. bye', file=f1)

# f1.close()
# f.close()

# '''
# You are given a file called grades.txt, where each line of the file contains a one-word student
# username and three test scores separated by spaces, like below:.

#     GWashington 83 77 54
#     JAdams 86 69 90

# Write code that scans through the file and determines how many students passed all three
# tests.

# '''


# # Modes
# # Read -- r
# # write - w
# # append - a
# # read/write  r+

'''
SET

list, tuple, dictionary, set
'''

l = [1,1,2,3,3,4,5,5,5]
first = set(l)  # {1, 2, 3, 4, 5}
l = list(first)

second = {1,5,6,7}

print(first | second) # {1, 2, 3, 4, 5, 6, 7}
print(first & second)  # {1, 5}
print(first - second)
print(second - first)