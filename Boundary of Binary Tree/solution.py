# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    left = []
    right = []
    root_l = []
    child = []

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.left = []
        self.right = []
        self.child = []
        self.root_l = [root.val]
        if root.left != None:
            self.goleft(root.left)
        if root.right != None:
            self.goright(root.right)
        if root.left != None or root.right != None:
            self.dfs(root)
        return self.root_l + self.left + self.child + self.right[::-1]

    def dfs(self, root):
        if root != None:
            if root.left == None and root.right == None:
                self.child.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)

    def goleft(self, root):
        if root != None:
            if root.left != None or root.right != None:
                self.left.append(root.val)
            if root.left != None:
                self.goleft(root.left)
            else:
                self.goleft(root.right)

    def goright(self, root):
        if root != None:
            if root.left != None or root.right != None:
                self.right.append(root.val)
            if root.right != None:
                self.goright(root.right)
            else:
                self.goright(root.left)
