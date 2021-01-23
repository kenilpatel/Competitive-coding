# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    no_child = None
    max1 = 0

    def getv(self):
        return 0

    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.no_child = defaultdict(self.getv)
        self.sum_child = defaultdict(self.getv)
        self.avg = defaultdict(self.getv)
        x = self.dfs(root)
        return self.max1

    def dfs(self, root):
        if root == None:
            return (0, 0)
        right = self.dfs(root.right)
        left = self.dfs(root.left)
        self.no_child[root] = 1 + right[0] + left[0]
        self.sum_child[root] = root.val + right[1] + left[1]
        self.avg[root] = float(self.sum_child[root] / self.no_child[root])
        if self.max1 < self.avg[root]:
            self.max1 = self.avg[root]
        return float(self.no_child[root]), float(self.sum_child[root])
