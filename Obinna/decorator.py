def decorator_function(func):
    def wrapper(*args, **kwargs):
        print('Do this before running the function passed as an argument')
        func(*args, **kwargs)
        print('i ran after the passed function')
    return wrapper


# def display():
#     print('display function ran')

# display = decorator_function(display)
# display()

@decorator_function
def display(m):
    print(f'display function ran {m}')

display('Nnamdi')

@decorator_function
def display_info(name, age):
    print('display_info ran with argments {}. {}'.format(name,age))
display_info('john',25)