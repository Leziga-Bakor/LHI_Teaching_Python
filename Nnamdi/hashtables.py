
class Hashtable():
    def __init__(self,size):
        pass
    def __str__(self):
        pass
    
    def _hash(self,key):
        pass
    
    def put(self,key,value):
        pass

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
    h.put('apples', 700)
    print(h)
    print(h.get('grapes'))
    # print(h)
    # h.remove('apples')
    # print(h)
    # print(h.keys())
    # print(h.values())
