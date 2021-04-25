# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root,maxt,mint):
            if root:
                maxt = max(maxt,root.val)
                mint = min(mint,root.val)
                dfs(root.left,maxt,mint)
                dfs(root.right,maxt,mint)
            else:
                self.ans = max(self.ans,abs(maxt - mint))
        dfs(root,float('-inf'),float('inf'))
        return self.ans
