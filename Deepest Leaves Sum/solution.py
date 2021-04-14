# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = defaultdict(lambda:[])
        self.ml = 0
        def dfs(root,l):
            if root != None:
                level[l].append(root.val)
                dfs(root.left,l + 1)
                dfs(root.right,l + 1)
                self.ml = max(self.ml,l)
        dfs(root,0)
        return sum(level[self.ml])
        
