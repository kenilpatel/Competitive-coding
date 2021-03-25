class Node(object):
    
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.first = None
        self.last = None
        self.cap = capacity
        self.filled = 0
        self.hashmap = defaultdict(lambda:None)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """  
        # print("get",key)
        node = self.hashmap[key]  
        if node == None:
            return -1
        else:
            val = node.val
            self.remove(node)
            self.put(key,val)
            return val
    
    def remove(self,node):
        key = node.key
        val = node.val   
        # print(node.val,node.key,self.first,self.last)
        if self.first == self.last and self.last == node:
            self.first = None
            self.last = None
            self.filled -= 1
            del self.hashmap[key]
        elif self.first == node:
            self.first = self.first.next
            self.filled -= 1
            del self.hashmap[key]
        elif self.last == node:
            self.last = self.last.prev
            self.filled -= 1
            del self.hashmap[key]
        else:
            prev = node.prev
            nex = node.next
            prev.next = nex
            nex.prev = prev
            self.filled -= 1
            del self.hashmap[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """     
        node = self.hashmap[key]  
        if node == None:
            node1 = Node(key,value) 
            if self.cap == self.filled:
                self.remove(self.last)
                self.put(key,value)
            else:
                if self.cap == 1:
                    self.last = node1
                    self.first = node1
                    self.filled += 1
                elif self.filled == 0:
                    self.first = node1
                    self.last = node1
                    self.filled += 1
                else:
                    node1.next = self.first 
                    self.first.prev = node1
                    self.first = node1
                    self.filled += 1
                self.hashmap[key] = node1
        else:
            self.remove(node)
            self.put(key,value) 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
