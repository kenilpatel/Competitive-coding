# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans = 0
        self.low = low 
        self.high = high
        def dfs(root):
            if root != None:
                if self.low <= root.val <= self.high:
                    self.ans += root.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.ans
