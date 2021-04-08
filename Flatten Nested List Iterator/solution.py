# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatlist(nestedList):
            ans = []
            if not nestedList.isInteger(): 
                for i in nestedList.getList():
                    if i.isInteger():
                        ans.append(i.getInteger())
                    else:
                        ans += flatlist(i)
            else:
                ans.append(nestedList.getInteger())
            return ans
        self.valf = []
        for x in nestedList:
            self.valf += flatlist(x)   
        self.n = len(self.valf)
        self.curi = -1
        
    def next(self):
        """
        :rtype: int
        """
        self.curi += 1
        return self.valf[self.curi]
            
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curi + 1 < self.n:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
