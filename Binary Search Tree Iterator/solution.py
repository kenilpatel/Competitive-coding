# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left   
        

    def next(self):
        """
        :rtype: int
        """
        x = self.stack.pop()
        itr = x.right
        while itr != None:
            self.stack.append(itr)
            itr = itr.left
        return x.val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
