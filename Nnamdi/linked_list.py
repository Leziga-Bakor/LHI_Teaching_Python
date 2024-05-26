# z --> a -> b -> c -> d ....

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LindedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        if self.head == None: 
            self.head = new_node 
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node 
            self.tail = new_node
            self.length += 1
                                  #  n.next
    def prepend(self,data): # z -> a -> b -> c -> d -> e -> f 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def insert(self,index,data):
        
        if index >= self.length:
            self.append(data)
            return
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        i = 0 
        temp = self.head
        while i < self.length: # 4
            if i == index-1:
                new_node.next = temp.next
                temp.next = new_node
                self.length +=1
            temp = temp.next
            i+=1

 
    def delete(self,index):
        pass

    def replace(self,index,data):
        pass

    def reverse(self):
        pass 

    def printL(self):
        pass

if __name__=='__main__':
    
    l = LindedList()
    l.append(10)
    l.append(8)
    l.append(9)
    l.append(5)