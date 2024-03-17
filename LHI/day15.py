'''
Scope

LEGB

- Built in Namespace
- Global Namespace
- Enclosed Namespace
- Local Namespace

'''


x = 1

def outer():
    # enclosed Namespace
    x = 2
    
    def inner():
        # local namespace
        global x
        x = 3
        print('inner', x)

    inner()

    print('outer', x)
   
outer()


print('global', x)











# x = 2

# def func():
#     print(x)
#     x = 3

# func()


# x = 2

