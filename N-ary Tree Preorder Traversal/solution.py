"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans
        stack = [root]
        while stack:
            top = stack.pop()
            ans.append(top.val)
            for c in top.children[::-1]:
                stack.append(c)
        return ans
