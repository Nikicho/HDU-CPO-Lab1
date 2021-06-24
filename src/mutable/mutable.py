#Author: Zhou Xinyu
#Separate chaining implemented:
#Put keyword values with the same hash address in the same single linked list
class Node(object):
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

    
class HashMap(object):
    init = object()
    def __init__(self, dict = None, length=5):
        if dict is not None:
            self.hashmap_from_dict(self,dict)
            
        self.keyList = []
        self.data = [self.init for i in range(length)]
        self.length = length
        self.index = 0

    def hashFunction(self, value):
        hash_value = value % self.length #mod
        return hash_value

    # 1. add
    def add(self, key, value):
        hash_value = self.hashFunction(key)
        NewNode = Node(key, value)
        
        if self.data[hash_value] == self.init:
            self.data[hash_value] = NewNode
            self.keyList.append(key)
        else:
            head = self.data[hash_value]
            #loop to find the Void Node
            while head.next != None: 
                #key Judge
                if head.key == key:
                    head.value = value
                    return
                head = head.next
            #Now find the Void Node 
            #key Judge
            if head.key == key:
                head.value = value
                return
            head.next = NewNode
            self.keyList.append(key)
        return

    # 2. remove
    def remove(self, value):          
        for i in range(self.length):
            head = self.data[i]
            #if self.data[hash_value] is void
            if head == self.init:
                continue
            #if head.value is the value
            elif head.value == value:
                self.data[i] = head.next
                self.keyList.remove(head.key)
                return True
        
            #head.value is not value
            pre = self.data[i]
            nxt = self.data[i].next
            while nxt.next is not None:
                if nxt.value == value:
                    pre.next = nxt.next
                    self.keyList.remove(nxt.key)
                    return True
                pre = nxt
                nxt = nxt.next
        #all the elements have been checked
        raise Exception("WE DONT HAVE THIS VALUE")
        return
    
    #get value
    def get(self, key):
        dict = self.hashmap_to_dict()
        value = dict[key]
        return value
    
    # 3. size
    def get_size(self):
        size = len(self.keyList)
        return size
    
    # 4. conversion
    def hashmap_from_dict(self, dict):
        for key, value in dict.items():
            self.add(key, value)
    #list dont have key, so use the order of value 
    def hashmap_from_list(self, list):
        for key, value in enumerate(list):
            self.add(key, value)

    def hashmap_to_dict(self):
        Output = {}
        #whether the hashmap is void
        if len(self.keyList) == 0:
            return Output
        #convert one by one set
        for i in range(self.length):
            if self.data[i] != self.init:
                head = self.data[i]
                while head != None:
                    Output[head.key] = head.value
                    head = head.next
        return Output
    # hashmap_to_list may lose the key info
    def hashmap_to_list(self):
        list = []
        dict = self.hashmap_to_dict()
        #value = dict[key]
        for key, value in dict.items():
            list.append(value)
        return list

    # 5. ﬁnd: return the even value list
    def find_even(self):
        dict = self.hashmap_to_dict()
        even_list = []
        for key, value in dict.items():
            if value % 2 == 0:
                even_list.append(value)
        return even_list

    # 6. ﬁlter: return the values' list except even value
    def filter_even(self):
        list = self.hashmap_to_list()
        no_even_list = []
        for value in list:
            if value % 2 != 0:
                no_even_list.append(value)
        return no_even_list
    
    # 7.map(func)
    def map(self, func):
        listOut = []
        list = self.hashmap_to_list()
        for value in list:
            value = func(value)
            listOut.append(value)
        return listOut
    
    # 8.reduce
    def reduce(self, func):
        a = 1
        for key in self.keyList:
            value = self.get(key)
            a = func(a, value)
        return a
    
    # 10. mempty and mconcat
    def mempty(self):
        return None

    def mconcat(self, x, y):
        #judge input
        if x is None:
            return y
        if y is None:
            return x
        
        for key in y.keyList:
            value = y.get(key)
            x.add(key, value)
        return x
    
    # 9.iteration
    def __iter__(self):
        list = []
        for key in self.keyList:
            list.append(Node(key, self.get(key)))
        return iter(list)
    