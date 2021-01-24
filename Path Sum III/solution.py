# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    count = None
    target = None

    def get(self):
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.target = sum
        self.dfs(root, [])
        return self.count

    def dfs(self, root, pl):
        if root != None:
            local = [root.val]
            if root.val == self.target:
                self.count += 1
            for i in pl:
                local.append(root.val + i)
                if root.val + i == self.target:
                    self.count += 1
            self.dfs(root.left, local)
            self.dfs(root.right, local)
        if root == None:
            return
