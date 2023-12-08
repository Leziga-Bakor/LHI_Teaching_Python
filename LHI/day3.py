"""
No. 9: A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.

"""




food_price = eval(input("Enter the meal amount: "))
tip  = eval(input("Enter the tip you want to leave in percentage: "))
total = food_price + food_price*tip/100

print("The tip was ", tip, 'percent and the total bill is ', total)

print(f"The tip was {tip}% and the total is N{total}")


# / - forward
# \ - backward

# ctrl + /

# x=eval('10000.23')'*

# print('*******************')
# print('*                 *')
# print('*                 *')
# print('*******************')

# print('*'*19)
# print('*',' '*17, '*',sep='%')
# print('*',' '*17, '*', sep='%')
# print('*'*19)

# # For loops 

# print('*******************')
# print('*******************')
# print('*******************')
# print('*******************')

for i in range(20,0,-1):
    print('A'*i)

# range(start=0, stop =4,step=1):
# range(6)
