
class Hashtable():
    def __init__(self,size):
        self.size = size
        self.hashtable = [[] for i in range(self.size)] #[[],[[key,value],[key2,value2]],[]]

    def __str__(self):
        return str(self.hashtable)
    
    def _hash(self,key):
        return len(key) % self.size
    
    def put(self,key,value):
        loc = self._hash(key)
        items = self.hashtable[loc]
        for item in items:
            if item[0] == key:
                item[1] = value
                return
        items.append([key,value])
        return


    def get(self, key):
        pass

    def remove(self, key):
        pass

    def keys(self):
        pass

    def values(self):
        pass
    
if __name__ == "__main__":

    h = Hashtable(12)
    h.put('grapes', 1000)
    h.put('apples', 10)
    h.put('ora', 300)
    h.put('banana', 200)
    # h.put('apples', 700)
    # print(h)
    # print(h.get('grapes'))
    # print(h)
    # h.remove('apples')
    # print(h)
    # print(h.keys())
    # print(h.values())
