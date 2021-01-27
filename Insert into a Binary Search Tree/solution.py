# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        self.dfs(root, val)
        return root

    def dfs(self, root, val):
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.dfs(root.left, val)
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.dfs(root.right, val)
