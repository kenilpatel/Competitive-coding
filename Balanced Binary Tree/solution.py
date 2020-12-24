# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.flag = 0

    def DFS(self, root):
        if(root == None):
            return [0, 0]
        x = self.DFS(root.left) if root.left != None else [0, 0]
        y = self.DFS(root.right) if root.right != None else [0, 0]
        l = max(x) + 1
        r = max(y) + 1
        diff = l - r
        if (diff == 1 or diff == 0 or diff == -1) == False:
            self.flag = self.flag + 1
        return [l, r]

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        child = self.DFS(root)
        diff = child[0] - child[1]
        return True if (diff == 1 or diff == 0 or diff == -1) and self.flag == 0 else False
