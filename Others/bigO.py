'''
Big O Asymptotic Analysis

The Big-O notation describes the worst-case running time of a program. 
We compute the Big-O of an algorithm by counting how many iterations an algorithm will take in the worst-case scenario with an input of N. 
We typically consult the Big-O because we must always plan for the worst case.

'''

'''
What is good code?

1. Readable
2. Scalable (Big O)

'''

import time
n = 100000000 # 1

# data_set = [] # 1
# for i in range(n): # n
#     data_set.append(i) # n

def findItem(arr):
    t1 = time.time() # 1
    for i in range(len(arr)): # n
        if arr[i] == 'name': # n
            print('found') # n or less
    t2 = time.time() # 1
    print(f'Finding items took {t2 - t1} seconds') # 1

# findItem(data_set) # 1

# 1+1+n+n+n+n+n+n+1+1+1
# 5+6n operations
# 6n
# n
# O(n) => Linear time


def getFirst(arr):
    t1 = time.time() # 1
    print(arr[-1]) # 1
    t2 = time.time() # 1
    print(f'Finding items took {t2 - t1} seconds')

# getFirst(data_set)

# 3
# O(1) => constant time


'''
Big O rules

1. Worst Case
2. Remove Constants
3. Different terms for different inputs
4. Drop non dominant term

'''

# for loop 1 a  
# for loop 2 b

# a + b
arr = [i for i in range(100000)]

def check(arr):
    t1 = time.time()
    for i in range(len(arr)): # n
        f = arr[i] # n
        # print() # n
        for j in range(len(arr)): # n*n
            g=arr[j] # n*n
            f*g # n*n
    t2 = time.time()
    print(f'Finding items took {t2 - t1} seconds')


check(arr)

# 3n + 3n**2
# 3n**2
# n**2
# O(n^2) => Quadratic time