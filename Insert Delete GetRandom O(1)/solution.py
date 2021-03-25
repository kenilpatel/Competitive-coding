import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.hashmap = defaultdict(lambda:-1)
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """  
        if self.hashmap[val] == -1:
            self.arr.append(val)
            self.hashmap[val] = self.size 
            self.size += 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """ 
        if self.hashmap[val] == -1:
            return False
        elif self.size == 1:
            del self.hashmap[val]
            self.arr.pop()
            self.size -= 1
            return True
        else:
            idx = self.hashmap[val]
            last_ele = self.arr[self.size - 1]
            self.arr[self.size - 1],self.arr[idx] = self.arr[idx],self.arr[self.size - 1] 
            self.hashmap[last_ele] = idx
            del self.hashmap[val] 
            self.size -= 1
            self.arr.pop()
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0,self.size - 1) 
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
