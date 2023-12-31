'''
Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000.

sum_odd - sum_even

1+3+7...+1999
-2-4-6...-2000

'''

sum_odd = 0
sum_even = 0
for i in range(1,2001):
    if i%2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i

ans = sum_odd - sum_even

print(ans)

sum_all = 0
for i in range(1,2001):
    if i%2 == 0:
        sum_all -= i
    else:
        sum_all += i

print(sum_all)