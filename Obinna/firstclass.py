'''

assign function to a variable
pass function as argument to a function
return a function

'''
# assign function to a variable
def square(num):
    
    return num*num

sq = square  
print(sq(5))

# pass function as argument to a function
def map(func, arr):
    a = []
    for item in arr:
        a.append(func(item))
    return a

new = map(square, [1,2,3,4,5])
print(new)

# return a function

def tag(m):
    def wrapper(msg):
        return f'<{m}>{msg}</{m}>'
    return wrapper

header1 = tag('h1')  # = wrapper(msg)
paragraph = tag('p')

header = header1('This is the main header')
p = paragraph('ghdfsghghthtrytggrtsdjyutsytytjsttytyhtjdtystyhtystwy')
p2 = paragraph('second paragraph')
print(header)
print(p)
print(p2)