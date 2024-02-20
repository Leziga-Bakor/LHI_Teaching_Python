class Myarray():
    
    def __init__(self):
        self.lenght = 0
        self.data = []

    def push(self, item):
        self.data.append(item)
        self.lenght += 1

    def poplast(self):
        if self.lenght:
            self.data.pop()
            self.lenght -= 1
        else:
            print('Arr is empty')

    def delete(self, index):
        pass

    def find(self, item):
        pass

    def insert(self, item):
        pass

    def __str__(self):
        return str(self.data)
        


    
if __name__== '__main__':

    arr = Myarray()
    arr.push('a')
    arr.push('b')
    arr.push('c')
    arr.push('d')
    print(arr)  # ['a','b','c','d']
    arr.poplast()
    print(arr)  # ['a','b','c']

    