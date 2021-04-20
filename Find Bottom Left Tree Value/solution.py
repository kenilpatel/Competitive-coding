# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deep_l = 0 
        self.level = defaultdict(lambda:[])
        def dfs(root,l):
            if root:
                self.deep_l = max(self.deep_l,l)
                self.level[l].append(root)
                dfs(root.left,l + 1)
                dfs(root.right,l + 1)
        dfs(root,0)
        return self.level[self.deep_l][0].val
        
